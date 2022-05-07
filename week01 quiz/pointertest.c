#include <stdio.h>

// int main(){
//     int*ptr;
//     printf("%p입니다\n",ptr);
// }

int main(void) {

double num = 5;

double * p = &num; // &num: num의 주소값을 의미

printf("%d", *p);

}