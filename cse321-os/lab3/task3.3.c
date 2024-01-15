#include <fcntl.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

void *ascii_counter(void *arg) {
    char *s = (char *)arg;
    int *result = malloc(sizeof(int));
    *result = 0;

    for (int i = 0; i < strlen(s); i++) {
        *result += s[i];
    }

    free(arg);
    pthread_exit((void *)result);
}

int main() {
    int rs[1000];
    pthread_t th[1000];
    pthread_t one, two, three;

    for (int iter = 0; iter < 3; iter++) {
        char *name = malloc(sizeof(char) * 100);
        scanf("%s", name);
        pthread_create(&th[iter], NULL, ascii_counter, name);
    }

    for (int i = 0; i < 3; i++) {
        int *res;
        pthread_join(th[i], (void *)&res);
        rs[i] = *res;
        free(res);
    }

    if (rs[0] == rs[1] && rs[0] == rs[2]) {
        printf("Youreka\n");
    } else if (rs[0] == rs[1] || rs[0] == rs[2] || rs[1] == rs[2]) {
        printf("Miracle\n");
    } else {
        printf("Hasta la vista\n");
    }

    return 0;
}
