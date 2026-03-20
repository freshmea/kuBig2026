#include "board.h"

static char board[7][50] = {
    "-------------------------------------------",
    "| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10  |",
    "-------------------------------------------",
    "| | | | | | | | | | | | | | | | | | | | | |",
    "-------------------------------------------",
    "|   |   |   |   |   |   |   |   |   |     |",
    "-------------------------------------------",
};

void initScore(Score * player, const char name[])
{
    strcpy(player->name, name);
    for (int i = 0; i < 12;++i){
        for (int j = 0; j < 3;j++){
            player->score[i][j] = 0;
        }
    }
}
void playGame(Score *player, int i);
void playGame10Frame(Score *player);
void printBoard(Score *player)
{
    system("clear");
    printf("\nPlayer name: %s\n", player->name);
    for (int i = 0; i < 7;++i){
        printf("%s\n", board[i]);
    }
}
void setScore(int frame, int bow, Score *player);
void setFrameScore(int frame, Score *player);
void calScore(int *frameScore, const int (*score)[3]);