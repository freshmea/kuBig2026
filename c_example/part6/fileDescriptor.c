#include <fcntl.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

static int build_source_path(char *buffer, size_t buffer_size, const char *filename)
{
    const char *source_file = __FILE__;
    const char *last_slash = strrchr(source_file, '/');
    size_t dir_length;

    if (last_slash == NULL)
    {
        return snprintf(buffer, buffer_size, "%s", filename) >= (int)buffer_size ? -1 : 0;
    }

    dir_length = (size_t)(last_slash - source_file);
    if (dir_length + 1 + strlen(filename) + 1 > buffer_size)
    {
        return -1;
    }

    memcpy(buffer, source_file, dir_length);
    buffer[dir_length] = '/';
    strcpy(buffer + dir_length + 1, filename);
    return 0;
}

int main(void)
{
    int fd;
    char path[sizeof(__FILE__) + 32];

    if (build_source_path(path, sizeof(path), "test.dat") != 0)
    {
        printf("파일 경로를 만들 수 없습니다.\n");
        return -1;
    }

    fd = open(path, O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (fd == -1)
    {
        printf("파일을 열수 없다.\n");
        return -1;
    }
    write(fd, "이것은 파일로 저장되는 예시 데이터 입니다.!", 62);
    close(fd);
    return 0;
}
