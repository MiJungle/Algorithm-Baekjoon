#define LOADER_SIG (LOADER_END - LOADER_SIG_LEN)  
#define LOADER_SIG_LEN 2
#define LOADER_END  0x7e00  
#define LOADER_ARGS (LOADER_SIG - LOADER_ARGS_LEN)     /* Command-line args. */
#define LOADER_ARG_CNT (LOADER_ARGS - LOADER_ARG_CNT_LEN) /* Number of args. */
#include <stdio.h>

int main(){

    // printf("%d\n", LOADER_SIG);
    // printf("%d\n", LOADER_ARG_CNT);
    printf("%d\n", LOADER_END);

}


//loader_sig: 32254 - loader_args_len(128)
// loader_arg_cnt =  32254-128-4 = 32122

// 0x8004007D7A
// 549822954874