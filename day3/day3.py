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

			if zero_count > one_count:
				positions[num] = "0"
			else:
				positions[num] = "1"

		for i in range(0,12):
			gamma_list[i] = positions[i]
			epsilon_list[i] = flip(positions[i])

		gamma = ''.join(gamma_list)
		epsilon = ''.join(epsilon_list)

	power_consumption = int(gamma,2) * int(epsilon,2)

	print("Challenge 1: " + str(power_consumption))

def challenge2():
	res_oxy = oxygen()
	res_co2 = co2()
	print("Challenge 2: " + str(res_co2 * res_oxy))

def oxygen():
	with open('input.txt') as file:
		oxygen = ""

		values_oxy = file.read().splitlines()
		if len(values_oxy) > 1:
			for i in range(0,12):
				zero_count = 0
				one_count = 0
				for value in values_oxy:
					if value[i] == "0":
						zero_count += 1
					if value[i] == "1":
						one_count += 1

					if zero_count == one_count:
						maj = 1
					if one_count > zero_count:
						maj = 1
					if zero_count > one_count:
						maj = 0

				values_oxy = list(filter(lambda x: x[i] == str(maj), values_oxy))

				if len(values_oxy) == 1:
					break

		if len(values_oxy) == 1:
			oxygen = int(values_oxy[0],2)
			print("Result oxygen: " + str(oxygen))
			return oxygen

def co2():
	with open('input.txt') as file:
		co2 = ""

		values_co2 = file.read().splitlines() 
		if len(values_co2) > 1:
			for i in range(0,12):
				zero_count = 0
				one_count = 0
				for value in values_co2:
					if value[i] == "0":
						zero_count += 1
					if value[i] == "1":
						one_count += 1

					if zero_count == one_count:
						min = 0
					if one_count > zero_count:
						min = 0
					if zero_count > one_count:
						min = 1

				values_co2 = list(filter(lambda x: x[i] == str(min), values_co2))

				if len(values_co2) < 2:
					break

		if len(values_co2) == 1:
			co2 = int(values_co2[0],2)
			print("Result co2: " + str(co2))
			return co2
def flip(val):
	if val == "0":
		res = "1"
	if val == "1":
		res = "0"

	return res

challenge1()
challenge2()
