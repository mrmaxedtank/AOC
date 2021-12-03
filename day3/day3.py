#!/usr/bin/python

def challenge1():
	with open('input.txt') as file:
		positions = ["0"] * 12
		power_consumption = 0
		gamma_list = ["0"] * 12
		epsilon_list = ["0"] * 12
		gamma = ""
		epsilon = ""

		values = file.readlines()

		for num in range(0,12):
			zero_count = 0
			one_count = 0
			for value in values:
				if value[num] == "0":
					zero_count += 1
				if value[num] == "1":
					one_count += 1

			#Debug
			#print("Zero_count: " + str(zero_count))
			#print("One_count: " + str(one_count))

			if zero_count > one_count:
				#print("Position " + str(num) + " = 0")
				positions[num] = "0"
			else:
				#print("Position " + str(num) + " = 1")
				positions[num] = "1"

		for i in range(0,12):
			gamma_list[i] = positions[i]
			epsilon_list[i] = flip(positions[i])

		gamma = ''.join(gamma_list)
		epsilon = ''.join(epsilon_list)

	#Convert binary string to decimal
	power_consumption = int(gamma,2) * int(epsilon,2)

	print(power_consumption)

def challenge2():
	print("Not ready yet")

def flip(val):
	if val == "0":
		res = "1"
	if val == "1":
		res = "0"

	return res


challenge1()
#challenge2()
