# -*- coding: utf-8 -*-

f1 = open('input2.txt', 'r')
lines = f1.readlines()
f1.close()

num_lines = sum(1 for line in open('input.txt'))

#print lines

for i in range(1,num_lines):
	if i % 2 == 1:
		print lines[i];

