// 구조체를 다뤄서 파일포인터로 저장, 읽어오기, 처리 를 하는 프로그램.
// Test result 출력 예시.
// -----------------------------------------------
//                  Test Result
// -----------------------------------------------
// ParkJungSeok         100 100 100 300 100.00  1
// LeeYoungHo            99  85  91 275  91.67  2
// LimYoHan              85  91  95 271  90.33  3
// KimTaekYong           95  83  91 269  89.67  4
// LeeYunYeol            80  90  85 255  85.00  5
// LeeJaeDong            95  85  51 231  77.00  6
// SongByungKoo          70  75  69 214  71.33  7
// MaJaeYoon             50  60  55 165  55.00  8
// ShinJiSoo             55  45  33 133  44.33  9
// HongJinHo             45  32  55 132  44.00 10
// -----------------------------------------------
// **table 포인터를 쓰지 않으려면 쓰지 않고 결과만 만들어도 됨
#include "scoreProcess.h"
#include <string.h>

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

int main(void){
    char finPath[sizeof(__FILE__) + 32];
    char foutPath[sizeof(__FILE__) + 32];

    if (build_source_path(finPath, sizeof(finPath), "score.dat") != 0 ||
        build_source_path(foutPath, sizeof(foutPath), "score.out") != 0){
        fprintf(stderr, "파일 경로를 만들 수 없습니다.\n");
        return 1;
    }

    FILE *fin = fopen(finPath, "r");
    FILE *fout = fopen(foutPath, "w");

    if (fin == NULL || fout == NULL){
        fprintf(stderr, "입력 또는 출력 파일을 열 수 없습니다. 예제 폴더의 데이터 파일을 확인하세요.\n");
        return 1;
    }

    int n = count_students(fin);

    Sdata *students = (Sdata *)malloc(sizeof(Sdata) * n);
    Sdata **table = (Sdata **)malloc(sizeof(Sdata) * n);

    if (students == NULL || table == NULL){
        fprintf(stderr, "메모리 할당 실패\n");
        return 1;
    }

    inputData(fin, students, n);
    calculateScore(students, n);
    calculateRank(students, n);
    sortPointers(students, table, n);
    printResult(fout, table, n);
    printf("성적 처리 결과 생성 완료: %s\n", foutPath);

    free(table);
    free(students);

    fclose(fin);
    fclose(fout);
    return 0;
}
