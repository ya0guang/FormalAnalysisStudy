#ifndef _RET_VERIF_H_
#define _RET_VERIF_H_

  #define GET_RBP8(init_ret_addr)		\
	    asm volatile (				\
			"movq 8(%%rbp), %%rax\n"	\
			"movq %%rax, %0;"			\
		    :"=r"(init_ret_addr)	\
			:						\
			)

  #define GET_RSP(fini_ret_addr)		\
	    asm volatile (				\
			"movq (%%rsp), %%rax\n"		\
			"movq %%rax, %0;"			\
			:"=r"(fini_ret_addr)	\
			:						\
	        )

  #define ret_assert(init_ret_addr, fini_ret_addr)	\
	((unsigned long long)init_ret_addr ==	\
	 (unsigned long long)fini_ret_addr) ?	\
	1 : 0

#endif
