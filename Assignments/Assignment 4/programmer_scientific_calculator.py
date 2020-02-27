def binConvert(num, val):
	while num != 0:
		remainder = num % 2
		num = num // 2
		val += str(remainder)

	return val[::-1]

def decConvert(num, val):
	num = num[::-1]

	count = 0
	total = 0

	for x in num:
		total += int(x) * 2**count
		count += 1

	return total

def calculate(operation):
	num1 = int(input("Enter the first integer: "))
	num2 = int(input("Enter the second integer: "))
	print()

	answer = 0

	if operation == "+":
		answer = num1 + num2
	elif operation == "-":
		answer = num1 - num2
	elif operation == "*":
		answer = num1 * num2
	elif operation == "**":
		answer = num1**num2
	elif operation == "/":
		answer = num1 / num2

	if operation == "**":
		print(str(num1) + "^" + str(num2) + " = " + str(answer) + "\n")
	else:
		print(str(num1) + " " + operation + " " + str(num2) + " = " + str(answer) + "\n")

def programmer():
	done0 = False

	while done0 == False:
		right = False

		while right == False:
			bindecChoice = int(input("Enter 1 to convert from decimal to binary or enter 2 to convert from binary to decimal: "))
			print()

			if bindecChoice == 1:
				pos = False

				while pos == False:
					val = int(input("Enter the positive decimal number: "))
					print()

					if val >= 0:
						pos = True
					else:
						print("Error: Invalid input")

				print("The decimal number, " + str(val) + ", in binary is: " + str(binConvert(val, "")) + "\n")
				right = True
			elif bindecChoice == 2:
				val = int(input("Enter the binary number: "))
				print()

				print("The binary number, " + str(val) + ", in decimal is: " + str(decConvert(str(val), "")) + "\n")
				right = True	
			else:
				print("Error: Invalid input")

		while right:
			choose = int(input("Enter 1 to do another calculation, enter 2 to go to a different mode, or enter 3 to exit: "))
			print()

			if choose == 1:
				right = False
			elif choose == 2:
				return False
			elif choose == 3:
				return True
			else:
				print("Error: Invalid input")

def scientific():
	done0 = False

	while done0 == False:
		right = False

		while right == False:
			operationsChoice = int(input("Enter 1 for '+', enter 2 for '-', enter 3 for '*', enter 4 for '**', enter 5 for '/': "))
			print()

			if operationsChoice == 1:
				calculate("+")
				right = True
			elif operationsChoice == 2:
				calculate("-")
				right = True	
			elif operationsChoice == 3:
				calculate("*")
				right = True
			elif operationsChoice == 4:
				calculate("**")
				right = True
			elif operationsChoice == 5:
				calculate("/")
				right = True
			else:
				print("Error: Invalid input")

		while right:
			choose = int(input("Enter 1 to do another calculation, enter 2 to go to a different mode, or enter 3 to exit: "))
			print()

			if choose == 1:
				right = False
			elif choose == 2:
				return False
			elif choose == 3:
				return True
			else:
				print("Error: Invalid input")

done = False

while done == False:
	calcChoice = int(input("Enter 1 for programmer mode or enter 2 for scientific mode: "))
	print()

	if calcChoice == 1:
		done = programmer()
	elif calcChoice == 2:
		done = scientific()
	else:
		print("Error: Invalid input")
