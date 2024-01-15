#include <stdio.h>

void sort(int array[], int size) {
  // output before sort
  printf("Before sorted: \n");
  for (int i = 0; i < size; i++) {
    printf("%d ", array[i]);
  }
  printf("\n");

  // sorting array
  for (int i = 1; i < size; i++) {
    int item = array[i];
    int j = i - 1;
    while (j >= 0 && item < array[j]) {
      array[j + 1] = array[j];
      j--;
    }
    array[j + 1] = item;
  }

  // output after sort
  printf("After sorted: \n");
  for (int i = 0; i < size; i++) {
    printf("%d ", array[i]);
  }
  printf("\n");
}
