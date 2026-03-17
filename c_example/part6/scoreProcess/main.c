// 구조체를 다뤄서 파일포인터로 저장, 읽어오기, 처리 를 하는 프로그램.

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
