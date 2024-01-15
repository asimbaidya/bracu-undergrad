#include <stdbool.h>
#include <stdio.h>

void deadlock_check(int N, int M, int allocated[N][M], int max[N][M],
                    int avail[M]) {
  bool flag = true;
  int remain = N;
  bool completed[N];
  for (int i = 0; i < N; i++) {
    completed[i] = false;
  }
  while (flag && remain > 0) {
    flag = false;
    for (int i = 0; i < N; i++) {
      if (completed[i] == true) {
        continue;
      }

      bool enough_res = true;
      for (int j = 0; j < M; j++) {
        int need = max[i][j] - allocated[i][j];
        if (need > allocated[i][j]) {
          enough_res = false;
          break;
        }
      }
      if (enough_res) {
        remain--;
        flag = false;
        for (int j = 0; j < M; j++) {
          avail[j] += allocated[i][j];
        }
      }
    }
  }
  if (remain == 0) {
    printf("Save hare\n");
  } else {
    printf("DeadLock Ahead :)\n");
  }
}

int main(int argc, char *argv[]) {

  // given inputs
  int n = 5;
  int m = 4;
  int alloc[5][4] = {
      {0, 1, 0, 3}, {2, 0, 0, 0}, {3, 0, 2, 0}, {2, 1, 1, 5}, {0, 0, 2, 2},
  };
  int max[5][4] = {
      {6, 4, 3, 4}, {3, 2, 2, 1}, {9, 1, 2, 6}, {2, 2, 2, 8}, {4, 3, 3, 7},
  };
  int avail[4] = {3, 3, 2, 1};
  // function call
  deadlock_check(n, m, alloc, max, avail);
  return 0;
}
