#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void checker(char pass[]) {
    bool lo_ch = 0, up_ch = 0, d_ch = 0, sym_ch = 0;
    int size = strlen(pass);

    for (int i = 0; i < size; i++) {
        if (pass[i] >= 65 && pass[i] <= 90)
            up_ch = true;
        if (pass[i] >= 97 && pass[i] <= 122)
            lo_ch = true;
        if (pass[i] >= 48 && pass[i] <= 57)
            d_ch = true;
        if (pass[i] == '_' || pass[i] == '$' || pass[i] == '#' ||
            pass[i] == '@')
            sym_ch = true;
    }

    if (lo_ch && up_ch && d_ch && sym_ch) {
        printf("OK\n");
    } else {
        char *str = malloc(1024 * sizeof(char));
        memset(str, 0, strlen(str));

        if (!up_ch) {
            strcat(str, "Uppercase character  missing, ");
        }
        if (!lo_ch) {
            strcat(str, "Lowercase character  missing, ");
        }
        if (!d_ch) {
            strcat(str, "Digit missing, ");
        }
        if (!sym_ch) {
            strcat(str, "Special Char missing, ");
        }

        str[strlen(str) - 2] = '\0'; // deleting tailing ,

        printf("%s\n", str);

        free(str);
    }
}

int main() {

    char p1[] = "hi Mom";
    char p2[] = "hi mom";
    char p3[] = "BR@CUspring";
    char p4[] = "bracuspring";
    char p5[] = "BR@CU20spring22";

    checker(p1);
    checker(p2);
    checker(p3);
    checker(p4);
    checker(p5);
    return 0;
}
