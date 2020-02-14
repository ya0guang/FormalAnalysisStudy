#include <stdio.h>

int foo()
{
	void *ret_addr;
	asm volatile (
			"movq 8(%%rbp), %%rax\n"
			"movq %%rax, %0;"
			:"=r"(ret_addr)
			:
			);
	printf("ret addr: %p\n", ret_addr);
	return 0;
}

int main()
{
	void *ptr;
	ptr = &&tag;
	printf("tag addr: %p\n", ptr);
	foo();
tag:
	printf("after tag\n");
	return 0;
}
