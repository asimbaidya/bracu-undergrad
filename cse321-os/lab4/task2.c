#include <stdio.h>
#include <stdlib.h>
#define shows(x) printf("%s\n", x);
#define showi(x) printf("%d\n", x);

typedef struct Ps {
    int id;
    int at;
    int bt;
    int ct;
} Ps;

void rr(Ps ps[], int size, int time_qt) {

    int tmp_bt[size];
    for (int i = 0; i < size; i++) {
        tmp_bt[i] = ps[i].bt;
    }

    int time_count = 0;
    int completed = 0;
    int i = 0;

    while (completed < size) {
        i = i % size;
        if (tmp_bt[i] == 0) {
            i++;
            continue;
        } else if (tmp_bt[i] - time_qt > 0) {
            tmp_bt[i] = tmp_bt[i] - time_qt;
            time_count += time_qt;
        } else {
            time_count += tmp_bt[i];
            ps[i].ct = time_count;
            tmp_bt[i] = 0;
            completed++;
        }
        i++;
    }

    for (int i = 0; i < size; i++) {
        int ct = ps[i].ct;
        int tat = ct - ps[i].at;
        int wt = tat - ps[i].bt;
        printf("PS%d: \t| CT: %d \t| TAT: %d \t| WT: %d\n", i + 1, ct, tat, wt);
    }
}

int main(int argc, char *argv[]) {

    int time_qt = 20;
    int size = 4;
    int bts[] = {53, 17, 68, 24};

    Ps ps[size];

    // assigning given value to each process
    for (int i = 0; i < size; i++) {
        ps[i].id = i + 1;
        ps[i].at = 0;
        ps[i].bt = bts[i];
    }

    // calling function
    rr(ps, size, time_qt);

    return 0;
}
