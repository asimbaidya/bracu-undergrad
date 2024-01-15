#include <fcntl.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

void function_runner_for_Faisal(void *first_argument) {
    int i = *(int *)first_argument;
    printf("thread-%d running\n", i);
    free(first_argument);
    pthread_exit(0);
}

int main() {
    int i = 1;
    while (i <= 5) {
        pthread_t t;
        int *tn = malloc(sizeof(int));
        *tn = i;
        pthread_create(&t, NULL, (void *)&function_runner_for_Faisal, tn);
        pthread_join(t, NULL);
        printf("thread-%d closed\n", i);
        i++;
    }

    return 0;
}
