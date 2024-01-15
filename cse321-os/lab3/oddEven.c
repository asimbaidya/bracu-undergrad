#include <stdio.h>

void oddEven(int array[], int size) {
    for (int i = 0; i < size; i++) {
        if (array[i] % 2 == 0) {
            printf("%d is Even\n", array[i]);
        } else {
            printf("%d is Odd\n", array[i]);
        }
    }
}
