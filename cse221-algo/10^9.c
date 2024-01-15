#include <stdio.h>

int main() {
  for (int i = 0; i < 1e12; i++) {
    continue;
  }
  printf("END\n");
  return 0;
}
