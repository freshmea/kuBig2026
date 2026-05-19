const nameEl = document.getElementById('name');
const scoreEl = document.getElementById('score');
const submitButton = document.getElementById('submit');
const resultEl = document.getElementById('result');

function clientErrors() {
    const errors = [];
    if (nameEl.value.trim().length === 0) {
        errors.push('프론트 검증: 이름을 입력하세요.');
    }
    if (scoreEl.value === '') {
        errors.push('프론트 검증: 점수를 입력하세요.');
    }
    return errors;
}

function renderErrors(errors) {
    resultEl.className = 'result error';
    resultEl.innerHTML = errors.map((error) => `<p>${error}</p>`).join('');
}

async function validate() {
    const errors = clientErrors();
    if (errors.length > 0) {
        renderErrors(errors);
        return;
    }

    const result = await window.pywebview.api.validate_score(nameEl.value, scoreEl.value);
    if (!result.ok) {
        renderErrors(result.errors);
        return;
    }

    resultEl.className = 'result ok';
    resultEl.textContent = `${result.student.name}: ${result.student.score}점 (${result.student.grade})`;
}

submitButton.addEventListener('click', validate);
