#!/usr/bin/env bash

set -u

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REPORT_DIR="$ROOT_DIR/review-reports"
REPORT_FILE="$REPORT_DIR/education-review-latest.md"

mkdir -p "$REPORT_DIR"

PASS_COUNT=0
WARN_COUNT=0
FAIL_COUNT=0

command_exists() {
    command -v "$1" >/dev/null 2>&1
}

paperclip_health_check() {
    if command_exists curl; then
        curl -fsS http://127.0.0.1:3100/api/health >/dev/null 2>&1
        return
    fi

    if command_exists python3; then
        python3 - <<'PY' >/dev/null 2>&1
import sys
import urllib.request

try:
    with urllib.request.urlopen("http://127.0.0.1:3100/api/health", timeout=5) as response:
        if response.status != 200:
            raise RuntimeError(f"unexpected status: {response.status}")
except Exception:
    sys.exit(1)
PY
        return
    fi

    return 127
}

pass() {
    PASS_COUNT=$((PASS_COUNT + 1))
    printf -- "- PASS: %s\n" "$1" >> "$REPORT_FILE"
}

warn() {
    WARN_COUNT=$((WARN_COUNT + 1))
    printf -- "- WARN: %s\n" "$1" >> "$REPORT_FILE"
}

fail() {
    FAIL_COUNT=$((FAIL_COUNT + 1))
    printf -- "- FAIL: %s\n" "$1" >> "$REPORT_FILE"
}

run_target_build() {
    local target="$1"
    local log_file

    if ! command_exists cmake; then
        warn "Skipped CMake target '$target' because 'cmake' is not installed in this runtime."
        return
    fi

    log_file="$(mktemp)"
    if cmake --build "$ROOT_DIR/build" --target "$target" -j2 >"$log_file" 2>&1; then
        pass "CMake target '$target' builds cleanly."
    else
        fail "CMake target '$target' failed to build. Tail: $(tail -n 5 "$log_file" | tr '\n' ' ' | sed 's/[[:space:]]\+/ /g')"
    fi
    rm -f "$log_file"
}

check_markdown_file() {
    local file="$1"
    local fence_count
    local file_issue=0
    local line_no=0
    local line
    local link_regex='\[[^][]+\]\(([^)]+)\)'
    local rest
    local match
    local target
    local cleaned_target
    local resolved_target
    local display_path

    fence_count=$(grep -c '^[[:space:]]*```' "$file" || true)
    if (( fence_count % 2 != 0 )); then
        fail "Unmatched fenced code block in ${file#$ROOT_DIR/}."
        file_issue=1
    fi

    while IFS= read -r line || [[ -n "$line" ]]; do
        line_no=$((line_no + 1))
        rest="$line"
        while [[ "$rest" =~ $link_regex ]]; do
            match="${BASH_REMATCH[0]}"
            target="${BASH_REMATCH[1]}"
            rest="${rest#*"$match"}"

            case "$target" in
                http://*|https://*|mailto:*|ftp://*|\#*)
                    continue
                    ;;
            esac

            cleaned_target="${target%%#*}"
            cleaned_target="${cleaned_target#<}"
            cleaned_target="${cleaned_target%>}"
            cleaned_target="${cleaned_target%% \"*}"
            cleaned_target="${cleaned_target%% \'*}"

            if [[ -z "$cleaned_target" ]]; then
                continue
            fi

            resolved_target="$(realpath -m "$(dirname "$file")/$cleaned_target")"
            if [[ ! -e "$resolved_target" ]]; then
                display_path="${file#$ROOT_DIR/}"
                fail "Broken local link in $display_path:$line_no -> $cleaned_target"
                file_issue=1
            fi
        done
    done < "$file"

    if (( file_issue == 0 )); then
        pass "Markdown checks passed for ${file#$ROOT_DIR/}."
    fi
}

syntax_check_collection() {
    local label="$1"
    shift
    local compiler=("$@")
    local -a files=()
    local -a failures=()
    local file
    local log_file

    while IFS= read -r file; do
        files+=("$file")
    done

    if (( ${#files[@]} == 0 )); then
        warn "$label: no files found to syntax check."
        return
    fi

    if ! command_exists "${compiler[0]}"; then
        warn "$label: skipped because '${compiler[0]}' is not installed in this runtime."
        return
    fi

    for file in "${files[@]}"; do
        log_file="$(mktemp)"
        if ! "${compiler[@]}" "$file" >"$log_file" 2>&1; then
            failures+=("${file#$ROOT_DIR/}: $(head -n 2 "$log_file" | tr '\n' ' ' | sed 's/[[:space:]]\+/ /g')")
        fi
        rm -f "$log_file"
    done

    if (( ${#failures[@]} == 0 )); then
        pass "$label: ${#files[@]} files passed syntax-only compilation."
    else
        fail "$label: ${#failures[@]} of ${#files[@]} files failed syntax-only compilation."
        printf -- "\n### %s failures\n" "$label" >> "$REPORT_FILE"
        printf -- "%s\n" "${failures[@]}" | sed 's/^/- /' >> "$REPORT_FILE"
    fi
}

{
    printf '# Education Review Report\n\n'
    printf 'Generated from %s\n\n' "$(date -Iseconds)"
    printf '## Paperclip\n'
} > "$REPORT_FILE"

if paperclip_health_check; then
    pass "Paperclip API is reachable at http://127.0.0.1:3100/api/health."
else
    case $? in
        127)
            warn "Paperclip API check skipped because neither 'curl' nor 'python3' is installed in this runtime."
            ;;
        *)
            warn "Paperclip API is not reachable. Start 'Paperclip: Start Local Server' for orchestrated runs."
            ;;
    esac
fi

printf '\n## Documentation Checks\n' >> "$REPORT_FILE"

while IFS= read -r markdown_file; do
    check_markdown_file "$markdown_file"
done < <(
    {
        printf '%s\n' "$ROOT_DIR/README.md"
        find "$ROOT_DIR/doc" -type f -name '*.md' | sort
        find "$ROOT_DIR/c_example" -type f -name '*.md' | sort
        find "$ROOT_DIR/ds" -type f -name '*.md' | sort
        find "$ROOT_DIR/network" -type f -name '*.md' | sort
        find "$ROOT_DIR/atmega128" -maxdepth 1 -type f -name '*.md' | sort
        find "$ROOT_DIR/bowling" -maxdepth 1 -type f -name '*.md' | sort
    } | uniq
)

printf '\n## Build Checks\n' >> "$REPORT_FILE"
run_target_build bowling
run_target_build mqttPub
run_target_build atmega128_project
run_target_build pico_project

printf '\n## Syntax Checks\n' >> "$REPORT_FILE"
syntax_check_collection \
    "Host example sources" \
    gcc -std=c11 -Wall -Wextra -I"$ROOT_DIR" -fsyntax-only \
    < <(find "$ROOT_DIR/c_example" -type f -name '*.c' | sort)

syntax_check_collection \
    "Data structure examples" \
    gcc -std=c11 -Wall -Wextra -I"$ROOT_DIR" -fsyntax-only \
    < <(find "$ROOT_DIR/ds" -type f -name '*.c' | sort)

printf '\n## Summary\n' >> "$REPORT_FILE"
printf -- '- PASS: %d\n' "$PASS_COUNT" >> "$REPORT_FILE"
printf -- '- WARN: %d\n' "$WARN_COUNT" >> "$REPORT_FILE"
printf -- '- FAIL: %d\n' "$FAIL_COUNT" >> "$REPORT_FILE"

cat "$REPORT_FILE"

if (( FAIL_COUNT > 0 )); then
    exit 1
fi
