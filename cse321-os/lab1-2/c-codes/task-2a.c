#include <stdio.h>

void add(int a, int b) {
    int result = a + b;
    printf("Addition result: %d\n", result);
}
void sub(int a, int b) {
    int result = a - b;
    printf("Subtractio result: %d\n", result);
}

void mul(int a, int b) {
    int result = a * b;
    printf("Multiplication result: %d\n", result);
}

int main() {
    int a, b, c;
    char op;

    printf("Enter 2 num & a char:\n");
    scanf("%d%d%c", &a, &b, &op);

    if (a > b) {
        sub(a, b);
    } else if (a < b) {
        add(a, b);
    } else {
        mul(a, b);
    }

    return 0;
}
