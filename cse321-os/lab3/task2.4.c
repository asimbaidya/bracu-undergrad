#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

void oddEven(int array[], int size) {
    for (int i = 0; i < size; i++) {
        if (array[i] % 2 == 0) {
            printf("%d is Even\n", array[i]);
        } else {
            printf("%d is Odd\n", array[i]);
        }
    }
}

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

int main(int argc, char *argv[]) {

    int size = argc - 1;
    int array[argc];

    if (size == 0) {
        printf("Please pass  cmd args like $ a.out 1 2 3\n");
        return -1;
    }

    for (int i = 1; i < argc; i++) {
        array[i - 1] = atoi(argv[i]);
    }

    pid_t pid = fork();

    if (pid == 0) {
        sort(array, size);
    } else {
        wait(NULL);
        oddEven(array, size);
    }

    return 0;
}
