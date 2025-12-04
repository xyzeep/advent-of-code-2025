#include <stdio.h>
#include <SDL3/SDL.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>

#define SCREEN_WIDTH 1200
#define SCREEN_HEIGHT 800


#define COLOR_BLACK 0x00000000
#define COLOR_GRID 0xff404040
#define CELL_COLOR 0xff7aadff

#define GRIDLINE_WIDTH 1

#define ROWS 139
#define COLS 139

#define CELL_H ((float)SCREEN_HEIGHT / ROWS)
#define CELL_W ((float)SCREEN_WIDTH / COLS)

#define MAX_LINES 150
#define MAX_LENGTH 150
#define MAX_REMOVE 10000



void drawGrid(SDL_Surface *surface)
{
    // rows
    for (int i = 0; i <= ROWS; i++)
    {
        SDL_Rect line = {0, CELL_H * i, SCREEN_WIDTH, GRIDLINE_WIDTH};
        SDL_FillSurfaceRect(surface, &line, COLOR_GRID);
    }
    // cols
    for (int i = 0; i <= COLS; i++)
    {
        SDL_Rect line = {CELL_W * i, 0, GRIDLINE_WIDTH, SCREEN_HEIGHT};
        SDL_FillSurfaceRect(surface, &line, COLOR_GRID);
    }
}

void drawCells(SDL_Surface *surface, char grid[][MAX_LENGTH]){
    for (int i = 0; i < ROWS; i ++) {
        for (int j = 0; j < COLS; j++) {
            if (grid[i][j] == '@') {

                SDL_Rect cell = {CELL_W * j, i * CELL_H, CELL_W + GRIDLINE_WIDTH, CELL_H + GRIDLINE_WIDTH};
                SDL_FillSurfaceRect(surface, &cell, CELL_COLOR);

            }
        }
    }
}

bool validRoll(int row, int col, char grid[][MAX_LENGTH]){
    int neighbor_count = 0;
    for (int i = row - 1; i < row + 2; i ++) {
        for (int j = col - 1; j < col + 2; j ++) {
            if (i == row && j == col){
                continue;
            }

            if (i < 0 || i > ROWS - 1 || j < 0 || j > COLS - 1){
                continue;
            }

            if (grid[i][j] == '@'){
                neighbor_count += 1;
            }
        }

    }

    return neighbor_count < 4;
}

void reviseGrid(char grid[][MAX_LENGTH], int to_remove[][2], int length){

    for (int i = 0; i < length; i ++) {
        int x = to_remove[i][0];
        int y = to_remove[i][1];

        grid[x][y] = '.';
    }

}

int solve(char grid[][MAX_LENGTH]){

    int rolls_count = 0;

        int to_remove[MAX_REMOVE][2];
        int remove_count = 0;

        for(int i = 0; i < ROWS; i++) {
            for (int j = 0; j < COLS; j++) {
                if (grid[i][j] == '@' && validRoll(i, j, grid)) {
                    rolls_count += 1;

                    if (remove_count < MAX_REMOVE) {
                        to_remove[remove_count][0] = i;
                        to_remove[remove_count][1] = j;
                        remove_count ++;
                    }
                    else {
                        printf("remove_count: %i\n", remove_count);
                        perror("Not enough memory for to_remove[][]. Increase MAX_REMOVE!\n");
                        return 1;
                    }
                }
            }

        reviseGrid(grid, to_remove, remove_count);
    }

    return rolls_count;
}

int main()
{
    // reading the input file
    FILE* file;

    file = fopen("input.txt", "r");
    if (file == NULL){
        printf("Couldn't find file\n");
        return 1;
    }

    char grid[MAX_LINES][MAX_LENGTH];

    int count = 0;
    while (fgets(grid[count], MAX_LENGTH, file)) {

        grid[count][strcspn(grid[count], "\n")] = '\0';
        count ++;
    }

    fclose(file);


    // ----------------------------------------------------


    // SDL initialization part
    SDL_Init(SDL_INIT_VIDEO);

    SDL_Window *window = SDL_CreateWindow("Paper Rolls", SCREEN_WIDTH, SCREEN_HEIGHT, 0);
    SDL_Surface *surface = SDL_GetWindowSurface(window);

    SDL_Rect black_screen = {0, 0, SCREEN_WIDTH, SCREEN_HEIGHT}; // to reset screen on every iteration

    int running = 1; // 1 for true and 0 for false


    SDL_Event event;

    while (running)
    {

        while (SDL_PollEvent(&event))
        {
            if (event.type == SDL_EVENT_QUIT)
            {
                running = 0;
            }
        }

        SDL_FillSurfaceRect(surface, &black_screen, COLOR_BLACK);

        // draw grids
        drawGrid(surface);

        drawCells(surface, grid);

        SDL_UpdateWindowSurface(window);

        solve(grid);

        SDL_Delay(200);
    }

    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}
