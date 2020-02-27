import random

numbers = []
right = False

while len(numbers) < 5:
    num = random.randint(1, 100)
    
    if num not in numbers:
        numbers.append(num)

guesses = int(input("How many guesses do you think you'll need: "))

print()

while guesses > 0 and right == False:
    guess = int(input("What is your guess: "))
    
    if guess in numbers:
        print("\nYay you got a number.")
        right = True
    else:
        guesses -= 1
        
        if guesses > 0:
            print("Wrong, try again\n")

print("\nThe answers were: " + str(numbers))