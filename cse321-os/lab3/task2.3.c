#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main(void) {

    int fd[2];
    if (pipe(fd) == -1) {
        printf("Could not create a pipe:\n");
    }
    int count = 1;
    write(fd[1], &count, sizeof(int));

    pid_t a, b, c;
    pid_t main_pid = getpid();

    a = fork();
    b = fork();
    c = fork();

    if (a == 0) {

        wait(NULL);

        pid_t cur_pid = getpid();
        if (cur_pid % 2 != 0) {
            fork();
            printf("ODD, a: %d\n", cur_pid);
        }
    }
    if (b == 0) {
        wait(NULL);

        pid_t cur_pid = getpid();
        if (cur_pid % 2 != 0) {
            fork();
            printf("ODD, b: %d\n", cur_pid);
        }
    }
    if (c == 0) {
        wait(NULL);

        pid_t cur_pid = getpid();
        if (cur_pid % 2 != 0) {
            fork();
            printf("ODD, c: %d\n", cur_pid);
        }
    }

    if (getpid() != main_pid) {
        read(fd[0], &count, sizeof(int));
        count += 1;
        write(fd[1], &count, sizeof(int));
    }

    waitpid(a, NULL, 0);
    waitpid(b, NULL, 0);
    waitpid(c, NULL, 0);

    if (getpid() == main_pid) {
        printf("parent!\n");

        read(fd[0], &count, sizeof(int));
        close(fd[1]);
        close(fd[0]);
        printf("total process: %d\n", count);
    }

    return 0;
}
