#!/usr/bin/python

def challenge1():
	with open('input.txt') as file:
		board_num = 0
		lines = file.readlines()
		line_num = 0
		boards = {}
		winning_board = 0
		last_value = 0

		for line in lines:
			if line_num == 0:
				numbers = line.strip().split(',')
				line_num += 1
			elif line == "\n":
				board_num += 1
				line_num += 1
				board_list = []
			else:
				board_list.append(format_line(line))
				line_num += 1
				boards[board_num] = board_list

		check = []
		found = False
		for x in range(0,len(numbers)):
			check.append(numbers[x])
			for n in range(1,board_num+1):
				res_l = check_lines(boards,n,check)
				if res_l == True:
					found = True
					winning_board = n
					last_value = check[-1]
					break
				res_c = check_columns(boards,n,check)
				if res_c == True:
					found = True
					winning_board = n
					last_value = check[-1]
					break
			if found == True:
				break

		value_left = calculate_result(boards,winning_board,check)
		print("Value left: " + str(value_left))
		print("Last value: " + str(last_value))

		res = int(value_left) * int(last_value)

		print(res)

def challenge2():
	with open('input.txt') as file:
		board_num = 0
		lines = file.readlines()
		line_num = 0
		boards = {}
		losing_board = 0
		last_value = 0
		board_index = []

		for line in lines:
			if line_num == 0:
				numbers = line.strip().split(',')
				line_num += 1
			elif line == "\n":
				board_num += 1
				board_index.append(board_num)
				#print(board_index)
				line_num += 1
				board_list = []
			else:
				board_list.append(format_line(line))
				line_num += 1
				boards[board_num] = board_list

		check = []
		found = False
		for x in range(0,len(numbers)):
			check.append(numbers[x])
			for n in range(1,board_num+1):
				#print(board_index)
				if n in board_index:
					res_l = check_lines(boards,n,check)
					if res_l == True:
						board_index.remove(n)
						#print("Row: Value: " + str(check[-1]))
						#print("Row: Removed: " + str(n))
						if len(board_index) == 1:
							found = True
							losing_board = board_index[0]
							try:
								last_value = numbers[x+1]
							except IndexError:
								last_value = numbers[x]
							break
						break
					res_c = check_columns(boards,n,check)
					if res_c == True and len(board_index) > 1:
						board_index.remove(n)
						#print("Column: Value: " + str(check[-1]))
						#print("Column: Removed:  " + str(n))
						if len(board_index) == 1:
							found = True
							losing_board = board_index[0]
							try:
								last_value = numbers[x+1]
							except IndexError:
								last_value = numbers[x]
							break

			if found == True:
				break

		print("Losing board: " + str(losing_board))

		value_left = calculate_result(boards,losing_board,check) - int(last_value)

		print("Value left: " + str(value_left))
		print("Last value: " + str(last_value))

		res = int(value_left) * int(last_value)

		print(res)



def format_line(x):
	res = []
	n = 3
	for i in range(0,len(x),n):
		res.append(x[i:i+n].strip())
	return res

def check_lines(boards,board_number,check_values):
	res = False
	for x in range(0,5):
		res = set(boards[board_number][x]).issubset(check_values)
		if res == True:
			#print("LINES: BREAK op board: " + str(board_number) + " regel " + str(x))
			return res

def check_columns(boards,board_number,check_values):
	res = False
	for x in range(0,5):
		column = set()
		for y in range(0,5):
			column.add(boards[board_number][y][x])
		res = set(column).issubset(check_values)
		if res == True:
			return res

def calculate_result(boards,board_number,check_values):
	res = 0
	for x in check_values:
		for y in range(0,5):
			if x in boards[board_number][y]:
				boards[board_number][y].remove(x)

	for i in range(0,5):
		ints = [int(item) for item in boards[board_number][i]]
		res += sum(ints)


	return res

#challenge1()
challenge2()
