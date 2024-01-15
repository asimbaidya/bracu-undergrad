#include <stdio.h>
#include <string.h>

void palimdrom_checker(char str[]) {
    int i = 0;
    int j = strlen(str) - 1;

    while (i < j) {
        if (str[i] != str[j]) {
            printf("Not Palimdrom\n");
            return;
        }

        i++, j--;
    }
    printf("Palimdrom\n");
}

int main() {

    palimdrom_checker("AAABBAAA");
    palimdrom_checker("AABBABA");
    palimdrom_checker("aabcbaa");

    return 0;
}
