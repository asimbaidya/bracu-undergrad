#include <stdio.h>
#include <string.h>

void domain_checker(char str[]) {

    char *token = strtok(str, "@");
    token = strtok(NULL, "@");

    if (strcmp(token, "kaaj.com") == 0) {
        printf("%s@kaaj.com Email address is outdated\n", str);
    } else {
        printf("%s@sheba.xyz Email address is okay\n", str);
    }
}

int main() {

    char str1[] = "zaki@sheba.xyz";
    char str2[] = "fahimd@kaaj.com";

    domain_checker(str1);
    domain_checker(str2);
    return 0;
}
