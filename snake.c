#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <windows.h>
#include <time.h>

#define width 20
#define height 19
char map[width][height];
int sx = width/2, sy = height/2; //snake pos
int fx, fy; //fruit pos
int score = 0;
int running = 1;

void set_fruit(){
    do{
        fx = rand() % width, fy = rand() % height;
    } while ((fx == sx && fy == sy) || (fx == 0 || fx == width - 1 || fy == 0 || fy == height - 1));
}

void init_map(){
    for (int j = 0; j < height; j++){
        for (int i = 0; i < width; i++){
            if (i == 0 || i == width - 1 || j == 0 || j == height - 1){
                map[i][j] = '#';
            }
            else{
                map[i][j] = ' ';
            }
        }
    }
    set_fruit();
    map[sx][sy] = '0';
    map[fx][fy] = '*';
}

void print_scr(){
    system("cls");
    for (int j = 0; j < height; j++){
        for (int i = 0; i < width; i++){
            printf("%c", map[i][j]);
        }
        printf("\n");
    }
    printf("\nScore: %i\n", score);
}

void update(char key){
    /**
     * Handles game logic
     */
    map[sx][sy] = ' ';
    switch(key){
        case 'w':
            sy += -1;
            break;
        case 'a':
            sx += -1;
            break;
        case 's':
            sy += 1;
            break;
        case 'd':
            sx += 1;
            break;
    }
    if (map[sx][sy] == '#') running = 0;
    if (map[sx][sy] == '*'){
        score += 1;
        set_fruit();
    }
    map[sx][sy] = '0';
    map[fx][fy] = '*';
}

int main(){
    srand(time(NULL));

    init_map();

    char key;

    while (running){
        if (kbhit()){
            key = getch();
        }
        else{
            update(key);
            print_scr();
            Sleep(100);
        }
    }

    printf("\nGame Over!\n");
    return 0;
}