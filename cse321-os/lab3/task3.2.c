#include <fcntl.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int count = 1;

void runner(void *arg) {
    int thno = *(int *)arg;

    for (int i = 0; i < 5; i++, count++) {
        printf("Thread %d prints %i\n", thno, count);
    }
    pthread_exit(0);
}

int main() {
    for (int i = 1; i <= 5; i++) {
        pthread_t t;
        pthread_create(&t, NULL, (void *)&runner, &i);
        pthread_join(t, NULL);
    }

    return 0;
}
