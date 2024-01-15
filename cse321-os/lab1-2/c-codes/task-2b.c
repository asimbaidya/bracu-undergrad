#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// use a --- file
void trim(char str[], int size) {
    int i = 0;
    int j = 0;
    for (; i < size; i++) {
        if (i > 0 && str[i] == ' ' && str[i - 1] != ' ') {
            str[j] = str[i];
            j++;
        } else if (str[i] != ' ') {
            str[j] = str[i];
            j++;
        }
    }
}

int main() {

    FILE *fptr;

    fptr = fopen("2b-input.txt", "r");
    if (fptr == NULL) {
        printf("Could not read input file!!\n");
        exit(1);
    }

    char str[1000];
    fscanf(fptr, "%[^\n]s", str);

    printf("Raw input: %s\n", str);
    printf("size of input: %ld\n", strlen(str));
    trim(str, 1000); //
    printf("trimmed: %s\n", str);

    FILE *ofptr;
    ofptr = fopen("2b-output.txt", "w");
    fprintf(ofptr, "%s\n", str);
    return 0;
}
