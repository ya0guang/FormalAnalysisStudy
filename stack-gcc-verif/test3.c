#include <stdio.h>

#include "stack_verif.h"

int foo()
{
	void *init_ret_addr;
	void *fini_ret_addr;

	GET_RBP8(init_ret_addr);
	printf("init_ret addr: %p\n", init_ret_addr);

	int a1, a2, a3, a4, a5, a6, a7, a8, a9;
	a1 = a2 = a3 = a4 = a5 = a6 = a7 = a8 = a9 = 1;

	GET_RBP8(fini_ret_addr);
	printf("fini_ret addr: %p\n", fini_ret_addr);

	return 0;
}

int main()
{
	void *ptr;
	foo();
	printf("Foo finished\n");
	return 0;
}
