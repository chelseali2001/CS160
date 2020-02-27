def convert(num, n, val):
	if (n == -1):
		return val
	elif (2**n <= num):
		val += "1"
		return convert(num - 2**n, n - 1, val)
	else:
		val += "0"
		return convert(num, n - 1, val)

right = False

while (right == False):
	num = int(input("Enter a decimal number less than or equal to 256: "))

	if (num <= 256 && num > 0):
		right = True
	else:
		print("Error: Input needs to be between 0 and 256");

print(convert(num, 8, ""));
