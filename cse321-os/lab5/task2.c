#include <pthread.h>
#include <semaphore.h>
#include <stdio.h>
#include <stdlib.h>

#define MaxCrops 5
#define warehouseSize 5

sem_t empty;
sem_t full;

// int in = 0;
// int out = 0;

int c_index = 0;
int w_index = 0;

// indicatig room for different crops
char crops[warehouseSize] = {
    'R', 'W', 'P', 'S', 'M',
};

// initially all the room is empty, N = empty
char warehouse[warehouseSize] = {
    'N', 'N', 'N', 'N', 'N',
};

pthread_mutex_t mutex;

void *Farmer(void *far) {

    /*
    1.Farmer harvest crops and put them in perticular room. For example, room 0
    for Rice(R). 2.use mutex and semaphore for critical section. 3.print which
    farmer is keeping which crops in which room inside the critical section.
    4.print the whole warehouse buffer outside of the critical section
    */
    for (int i = 0; i < MaxCrops; i++) {

        sem_wait(&empty);
        pthread_mutex_lock(&mutex);
        // CT
        char x = crops[c_index % 5];
        warehouse[w_index] = x;

        printf("Farmer %d: Insert crops %c at %d\n", *(int *)far, x, c_index);

        c_index++;
        w_index++;

        pthread_mutex_unlock(&mutex);
        sem_post(&full);
    }
    free(far);
    pthread_exit(0);
}
void *ShopOwner(void *sho) {

    /*
       1.Shop owner take crops and make that perticular room empty.
       2.use mutex and semaphore for critical section.
       3.print which shop owner is taking which crops from which room inside the
       critical section. 4.print the whole warehouse buffer outside of the
       critical section
       */

    for (int i = 0; i < MaxCrops; i++) {
        sem_wait(&full);
        pthread_mutex_lock(&mutex);

        char y = warehouse[w_index - 1];
        warehouse[w_index - 1] = 'N';
        int w = w_index - 1;
        printf("Shop owner %d: Remove crops %c from %d\n", *(int *)sho, y, w);
        w_index--;

        pthread_mutex_unlock(&mutex);
        sem_post(&empty);
    }
    printf("ShopOwner%d: ", *(int *)sho);
    for (int i = 0; i < warehouseSize; i++) {
        printf("%c", warehouse[i]);
    }
    printf("\n");

    free(sho);
    pthread_exit(0);
}
int main() {
    // intializing thread,mutex,semaphore
    pthread_t Far[5], Sho[5];
    pthread_mutex_init(&mutex, NULL);

    sem_init(&empty, 0, warehouseSize);
    sem_init(&full, 0, 0);

    // Just used for numbering the Farmer and ShopOwner
    int a[5] = {
        1, 2, 3, 4, 5,
    };

    /*creat 5 thread for Farmer 5 thread for ShopOwner
     * My code
     */
    for (int i = 0; i < 5; i++) {

        int *p = malloc(sizeof(int));
        int *q = malloc(sizeof(int));
        *p = a[i];
        *q = a[i];
        // creating 5+5, thread
        pthread_create(&Far[i], NULL, &Farmer, p);
        pthread_create(&Sho[i], NULL, &ShopOwner, q);
    }

    for (int i = 0; i < 5; i++) {
        pthread_join(Far[i], NULL);
        pthread_join(Sho[i], NULL);
    }

    pthread_mutex_destroy(&mutex);
    sem_destroy(&empty);
    sem_destroy(&full);

    return 0;
}
