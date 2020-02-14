#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

def parse1file(filename):
	file = open(filename, "r")
	lines = file.readlines()
	newfile = filename.split('.')[0] + "-stack.c"
	writeFile = open(newfile,"a+")

	writeFile.write("#include \"stack-verif.h\"\n")

	for i in range(len(lines)):
		if "{" in lines[i] and len(lines[i].split('{')[0]) == 0 and lines[i-1].strip().endswith(')'):
			newlines = "\nvoid *init_ret_addr;\n" + "void *fini_ret_addr;\n" + "GET_RBP8(init_ret_addr);\n\n"
			writeFile.write(lines[i])
			writeFile.write(newlines)

		elif lines[i].strip().endswith(') {') and not lines[i].strip().startswith('for') and not lines[i].strip().startswith('if') and not lines[i].strip().startswith('while') and "else if" not in lines[i]:
			newlines = "\nvoid *init_ret_addr;\n" + "void *fini_ret_addr;\n" + "GET_RBP8(init_ret_addr);\n\n"
			writeFile.write(lines[i])
			writeFile.write(newlines)
		
		elif lines[i].strip().startswith("return ") or lines[i].strip().startswith("return;"):
			newlines = "\nGET_RBP8(fini_ret_addr);\n" + "assert(ret_assert(init_ret_addr, fini_ret_addr));\n"
			writeFile.write(newlines)
			writeFile.write(lines[i])
		elif "}" in lines[i] and len(lines[i].split('}')[0]) == 0:
			if ";" not in lines[i]:
				newlines = "\nGET_RBP8(fini_ret_addr);\n" + "assert(ret_assert(init_ret_addr, fini_ret_addr));\n"
				writeFile.write(newlines)
			writeFile.write(lines[i])
		else:
			writeFile.write(lines[i])

if __name__ == "__main__":
	if sys.argv[1] != None:
		parse1file(sys.argv[1])
