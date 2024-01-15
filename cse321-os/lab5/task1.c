#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define MAX 10
#define BUFLEN 6
#define NUMTHREAD 2

void *consumer(void *id);
void *producer(void *id);

char buffer[BUFLEN + 1];
char source[BUFLEN + 1];

int pCount = 0;
int cCount = 0;
int buflen;

pthread_mutex_t count_mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t empty = PTHREAD_COND_INITIALIZER;
pthread_cond_t full = PTHREAD_COND_INITIALIZER;

int thread_id[NUMTHREAD] = {0, 1};

int src_index = 0;  // for accessing values
int count = 0;      // for ..

int main() {
    pthread_t thread[NUMTHREAD];

    strcpy(source, "abcdef");
    buflen = strlen(source);

    for (int i = 0; i < NUMTHREAD; i++) {
        int *a = malloc(sizeof(int));
        *a = thread_id[i];
        if (i == 0) {
            pthread_create(&thread[i], NULL, &producer, a);
        } else {
            pthread_create(&thread[i], NULL, &consumer, a);
        }
    }

    for (int i = 0; i < NUMTHREAD; i++) {
        pthread_join(thread[i], NULL);
    }
}

// producer
void *producer(void *id) {
    for (int i = 0; i < MAX; i++) {
        pthread_mutex_lock(&count_mutex);

        while (count >= BUFLEN) {
            pthread_cond_wait(&full, &count_mutex);
        }

        char x = source[src_index % BUFLEN];
        buffer[count] = x;
        src_index++;
        count++;
        pCount++;

        printf("%d produced %c by Thread %d\n", i, x, *(int *)id);

        pthread_cond_signal(&empty);
        pthread_mutex_unlock(&count_mutex);
    }
    pthread_exit(0);
}
// consumer
void *consumer(void *id) {
    for (int i = 0; i < MAX; i++) {
        pthread_mutex_lock(&count_mutex);

        while (count <= 0) {
            pthread_cond_wait(&empty, &count_mutex);
        }
        char y = buffer[count - 1];
        count--;
        cCount++;

        printf("%d consumeed %c by Thread %d\n", i, y, *(int *)id);

        pthread_cond_signal(&full);
        pthread_mutex_unlock(&count_mutex);
    }
    pthread_exit(0);
}
