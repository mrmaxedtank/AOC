#!/usr/bin/python

def position():
	with open('input.txt') as file:
		horpos = 0
		depth = 0
		aim = 0
		res = 0

		moves = file.readlines()

		for x in moves:
			move = x.split(' ')
			if move[0] == "forward":
				horpos += int(move[1])
				depth = depth + (aim * int(move[1]))
			if move[0] == "up":
				aim -= int(move[1])
			if move[0] == "down":
				aim += int(move[1])

	res = horpos * depth
	print(res)

position()
