#include <stdio.h>


void lets_see_what_i_got(int *first_index){
	for(int i=0; i<5; i++){
		printf("value: %d\n",first_index[i]);
	}
}


int main(){
    int array[] = {1,2,3,4,5};
	lets_see_what_i_got(&array[2]);
    return 0;
}
