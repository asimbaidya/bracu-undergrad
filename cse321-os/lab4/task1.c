#include <stdio.h>
#include <stdlib.h>

typedef struct Ps {
    int id;
    int at;
    int bt;
    int ct;
    int tat;
    int wt;
} Ps;

void sjf(Ps ps[], int n) {

    int time_counter = 0;
    int completed = 0;

    for (; completed < n; time_counter++) {
        Ps boli;
        int boli_i = 0;
        boli.bt = 9999999;
        for (int i = 0; i < n; i++) {
            if (ps[i].at <= time_counter) {
                if (ps[i].bt > 0 && ps[i].bt < boli.bt) {
                    boli_i = i;
                    boli = ps[i];
                }
            }
        }
        ps[boli_i].bt--;
        if (ps[boli_i].bt == 0) {
            completed++;
            ps[boli_i].ct = time_counter + 1;
        }
    }

    for (int i = 0; i < n; i++) {
        ps[i].ct = ps[i].ct;
        ps[i].tat = ps[i].ct - ps[i].at;
        ps[i].wt = ps[i].tat - ps[i].bt;
        int ct = ps[i].ct;
        int tat = ps[i].tat;
        int wt = ps[i].wt;
        printf("PS%d: \t| CT: %d \t| TAT: %d \t| WT: %d\n", i + 1, ct, tat, wt);
    }
}

int main(int argc, char *argv[]) {

    int size = 5;
    Ps ps[5];

    int ats[] = {0, 2, 3, 4, 5};
    int bts[] = {5, 2, 7, 4, 5};

    for (int i = 0; i < size; i++) {
        ps[i].at = ats[i];
        ps[i].bt = bts[i];
    }

    sjf(ps, size);

    return 0;
}
