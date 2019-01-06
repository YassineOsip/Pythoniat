#!/usr/bin/python
import sys
file=open(sys.argv[1],"r+")
wordcount={}
for word in file.read().split():
	if word not in wordcount:
		wordcount[word] = 1
	else: 
		wordcount[word] += 1
for key,v in wordcount.items():
	print key,v
file.close();
