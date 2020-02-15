#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

def parse1file(filename):
	file = open(filename, "r")
	lines = file.readlines()
	newfile = filename.split('.')[0] + "-br-tb.txt"
	writeFile = open(newfile,"w")

	funcAddr = {}

	funcName = ""
	startAddr = ""
	endAddr = ""
	insList = ["call", "callq", "jmp", "jmpl", "jmpq", "jo", "jno", "js", "jns", "je", "jz", "jne", "jnz", "jb", "jnae", "jc", "jnb", "jae", "jnc", "jbe", "jna", "ja", "jnbe", "jl", "jnge", "jge", "jnl", "jle", "jng", "jg", "jnle", "jp", "jpe", "jnp", "jpo", "jcxz", "jecxz"]
	jmps = []
	for i in range(len(lines)):
	#for line in lines:
		inFlag = True
		
#if not inFlag:
#			print(start)
		
		if " <" in lines[i] and ">:" in lines[i]:
			startAddr = lines[i].split()[0]
			funcName = lines[i].split()[1]
			#print (funcName, startAddr, end="----")
			#inFlag = True

		if lines[i].startswith('\n'):
			endAddr = lines[i-1].split(':')[0]
#inFlang = False
			addr =  startAddr + "->" + endAddr.strip()
			print ("\t" + funcName + "\t", "\t", addr)
			for jmp in jmps:
				print("\t\t", jmp, "\t")
			jmps = []
		
		for ins in insList:
			if ("\t" + ins) in lines[i]:
				jmps.append(lines[i])
			
	
if __name__ == "__main__":
	if sys.argv[1] != None:
		parse1file(sys.argv[1])
