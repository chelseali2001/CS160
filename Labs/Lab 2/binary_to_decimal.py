print("Enter a binary number to convert to decimal.")

bitNum = []

for x in range(8):
    val = input("Digit " + str(x + 1) + ": ")
    bitNum += str(val)

count = 0
decNum = 0

for x in bitNum:
    decNum += int(x) * 2**count
    count += 1

theInput = ""
bitNum.reverse()

for x in bitNum:
    theInput += x

print(str(theInput) + " to decimal is: " + str(decNum))
