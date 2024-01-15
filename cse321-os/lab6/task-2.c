#include <stdbool.h>
#include <stdio.h>

void safe_seq(int N, int M, int allocated[N][M], int max[N][M], int avail[M]) {
    int remain = N;
    bool completed[N];
    for (int i = 0; i < N; i++) {
        completed[i] = false;
    }

    int save_sequence[N];
    int index = 0;
    bool flag = true;

    while (flag && remain > 0) {
        flag = false;
        for (int i = 0; i < N; i++) {
            if (completed[i] == true) {
                continue;
            }
            bool enough_res = true;
            for (int j = 0; j < M; j++) {
                int need = max[i][j] - allocated[i][j];
                if (need > avail[j]) {
                    enough_res = false;
                    break;
                }
            }

            if (enough_res) {
                flag = true;
                completed[i] = true;
                save_sequence[index] = i;
                index++;
                remain--;
                for (int j = 0; j < M; j++) {
                    avail[j] += allocated[i][j];
                }
            }
        }
    }
    if (remain == 0) {
        printf("Save Sequences: ");
        for (int i = 0; i < N; i++) {
            printf("Process%d", save_sequence[i]);
            if (i == N - 1) {
                printf(" | Done\n");
            } else {
                printf(" -> ");
            }
        }
    } else {
        printf("Eid Mubarak!!, btw, Deadlock got you!\n");
    }
}

int main(int argc, char *argv[]) {

    int n = 6; // Number of processes
    int m = 4; // Number of resources
    int alloc[6][4] = {
        {0, 1, 0, 3}, // P0
        {2, 0, 0, 3}, // P1
        {3, 0, 2, 0}, // P2
        {2, 1, 1, 5}, // P3
        {0, 0, 2, 2}, // P4
        {1, 2, 3, 1}, // P5
    };
    int max[6][4] = {
        {6, 4, 3, 4}, // P0
        {3, 2, 2, 4}, // P1
        {9, 1, 2, 6}, // P2
        {2, 2, 2, 8}, // P3
        {4, 3, 3, 7}, // P4
        {6, 2, 6, 5}, // P5
    };
    int avail[4] = {2, 2, 2, 1};
    safe_seq(n, m, alloc, max, avail);

    return 0;
}
