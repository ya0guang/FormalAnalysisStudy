#include "smack.h"
#include <stdlib.h>
#include <stdbool.h>

bool foo_executed = 0;

void foo() {
    //do_something();
    foo_executed = 1;
}

int main(){
    //comment foo to get an error from smack
    foo();
    assert(foo_executed == 1);

    //if you want to reset the "executed" status for later use, please:
    foo_executed = 0;
    return 0;
}

