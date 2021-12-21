#!/usr/bin/python

def challenge1():
	with open('test_input.txt') as file:
		board_num = 0
		board_id = "board" + str(board_num)
		lines = file.readlines()
		line_num = 0
		boards = {}

		print(lines)

		for line in lines:
			if line_num == 0:
				numbers = line.strip().split(',')
				line_num += 1
			elif line == "\n":
				board_num += 1
				board_id = "board" + str(board_num)
				line_num += 1
				board_list = []
			else:
				board_list.append(format_line(line))
				line_num += 1
				boards[board_id] = board_list

		#print(numbers)

		check = []
		for x in range(0,len(numbers)):
			check.append(numbers[x])
			for n in range(1,board_num+1):
				res = check_lines(boards,n,check)
				if res == True:
					break
				res = check_columns(boards,n,check)
				if res == True:
					break
			if res == True:
				break

def format_line(x):
	res = []
	n = 3
	for i in range(0,len(x),n):
		res.append(x[i:i+n].strip())
	return res

def check_lines(b,n,c):
	res = False
	for x in range(0,5):
		print("check_lines")
		print(n)
		res = set(b["board"+str(n)][x]).issubset(c)
		print(c)
		if res == True:
			print("BREAK op board: " + str(n) + " regel " + str(x))
			return res

def check_columns(b,n,c):
	res = False
	for x in range(0,5):
		for y in range(0,5):
			print("check_columns")
			print("x: " + str(x))
			print("y: " + str(y))
			res = set(b["board"+str(n)][x][y]).issubset(c)
			print(c)
			if res == True:
				print("BREAK op board: " + str(n) + " column " + str(y))
				return res

challenge1()
#challenge2()
