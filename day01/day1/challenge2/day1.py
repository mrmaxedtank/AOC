#!/usr/bin/python

import os, sys

def count():
	with open('input.txt') as file:
		res = 0
		data = file.readlines()
		data = [int(line.rstrip()) for line in data]

		for x in range(1,len(data)-2):
			if data[x]+data[x+1]+data[x+2] > data[x-1]+data[x]+data[x+1]:
				res += 1
	print(res)

count()
