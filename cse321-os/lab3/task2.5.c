#include <fcntl.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main() {
    pid_t child = fork();

    if (child == 0) {
        printf("2.Child process: %d\n", getpid());

        pid_t gc1, gc2, gc3;
        gc1 = fork();

        if (gc1 != 0) {
            // still inside child
            printf("3.Grand child process ID: %d\n", gc1);
            gc2 = fork();

            if (gc2 != 0) {
                // inside chid1, so new child will be grand child
                printf("4.Grand child process ID: %d\n", gc2);
                gc3 = fork();
                if (gc3 != 0) {
                    // inside chid1, so new child will be grand child
                    printf("5.Grand child process ID: %d\n", gc3);
                }
            }
        }
    } else {
        printf("1.Parent Process: %d\n", getpid());
    }

    wait(NULL);
    return 0;
}
