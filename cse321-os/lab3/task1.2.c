#include <stdbool.h>
#include <stdio.h>

bool is_perfect(int n) {

    int div_sum = 0;
    for (int i = 1; i <= n / 2; i++) {
        if (n % i == 0) {
            div_sum += i;
        }
    }

    if (div_sum == n)
        return true;
    return false;
}

void solve() {
    int l, r;
    scanf("%d%d", &l, &r);

    for (int i = l; i <= r; i++) {
        if (is_perfect(i)) {
            printf("%d\n", i);
        }
    }
}

int main() {

    solve();
    return 0;
}
