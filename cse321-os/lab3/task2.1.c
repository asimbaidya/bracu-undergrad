#include <errno.h>
#include <fcntl.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Unexpected number of argument!\n");
        printf("please use..\n");
        printf("λ ./a.out [filename]\n");
        exit(-1);
    }

    printf("File name: %s\n", argv[1]);

    int fd = open(argv[1], O_RDWR | O_CREAT, 0664);

    // if (fd == -1) {
    //     printf("Something is up!\n");
    //     printf("Error NO: %d\n", errno);
    //     perror("Error: ");
    // }

    char buf[100];
    printf("enter something!\n");

    while (1) {
        scanf("%s", buf);
        if ((strcmp(buf, "-1") == 0)) {
            break;
        }
        write(fd, buf, strlen(strcat(buf, " ")));
        // write(fd, "\n", 1);
    }
    close(fd);

    return 0;
}
