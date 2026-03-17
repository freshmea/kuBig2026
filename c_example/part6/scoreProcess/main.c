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

#include <stdio.h>
#include <stdlib.h>

typedef struct {
    char name[20];
    int kor;
    int eng;
    int mat;
    int sum;
    double average;
    int rank;
} Sdata;

void inputData(FILE *fp, Sdata *s, int n);
void calculateScore(Sdata *s, int n);
void calculateRank(Sdata *s, int n);
void sortPointers(Sdata *s, Sdata **table, int n);
void printResult(FILE *fp, Sdata **table, int n);

int main(void){
    FILE *fin = fopen("score.dat", "r");
    FILE *fout = fopen("score.out", "w");
    int n;
    printf("처리할 학생의 수를 입력하세요: ");
    if (scanf("%d", &n) != 1)
        return 1;

    if (fin == NULL || fout == NULL){
        fprintf(stderr, "파일을 열수 없습니다.\n");
        return 1;
    }

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

    free(table);
    free(students);

    fclose(fin);
    fclose(fout);
    return 0;
}

void inputData(FILE *fp, Sdata *s, int n)
{
    for (int i = 0; i < n;++i){
        fscanf(fp, "%s %d %d %d", s[i].name, &s[i].kor, &s[i].eng, &s[i].mat);
    }
}
void calculateScore(Sdata *s, int n)
{
    for (int i = 0; i < n;++i){
        s[i].sum = s[i].kor + s[i].eng + s[i].mat;
        s[i].average = (double)s[i].sum / 3.0;
        s[i].rank = 1;
    }
}
void calculateRank(Sdata *s, int n)
{
    for (int i = 0; i < n;++i){
        for (int j = 0; j < n;++j){
            if (s[i].sum <s[j].sum)
                s[i].rank++;
        }
    }
}
void sortPointers(Sdata *s, Sdata **table, int n)
{
    for (int i = 0; i < n;++i)
        table[i] = &s[i];
    for (int i = 0; i < n;++i){
        for (int j = 0; j < n;++j){
            if (table[i]->sum > table[j]->sum){
                Sdata *tmp = table[i];
                table[i] = table[j];
                table[j] = tmp;
            }
        }
    }

}
void printResult(FILE *fp, Sdata **table, int n)
{
    fprintf(fp, "-----------------------------------------------\n");
    fprintf(fp, "                  Test Result\n");
    fprintf(fp, "-----------------------------------------------\n");
    for (int i = 0; i < n;++i){
        fprintf(fp, "%-20s %3d %3d %3d %3d %6.2f %2d\n", table[i]->name, table[i]->kor, table[i]->eng, table[i]->mat, table[i]->sum, table[i]->average, table[i]->rank);
    }
    fprintf(fp, "-----------------------------------------------\n");
}