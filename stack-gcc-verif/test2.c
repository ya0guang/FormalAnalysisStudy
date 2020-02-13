#include <stdio.h>

int foo()
{
	void *init_ret_addr;
	void *fini_ret_addr;
	asm volatile (
			"movq 8(%%rbp), %%rax\n"
			"movq %%rax, %0;"
			:"=r"(init_ret_addr)
			:
			);

	int a1, a2, a3, a4, a5, a6, a7, a8, a9;
	a1 = a2 = a3 = a4 = a5 = a6 = a7 = a8 = a9 = 1;

	printf("init_ret addr: %p\n", init_ret_addr);
	asm volatile (
			"movq (%%rsp), %%rax\n"
			"movq %%rax, %0;"
			:"=r"(fini_ret_addr)
			:
			);
	printf("fini_ret addr: %p\n", fini_ret_addr);

	return 0;
}

int main()
{
	void *ptr;
	foo();
	printf("fini\n");
	return 0;
}
