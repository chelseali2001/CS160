def Occurance(a):
    letters = []
    numbers = []
    
    for x in a:
        for i in x:
            if i not in letters:
                letters.append(i)
                numbers.append(1)
            else:
                index = letters.index(i)
                numbers[index] += 1
                
    print("There are", end =" ")
        
    if len(a) == 0:
        print(" no letters")
    else:
        for x in range(len(letters)):
            if x == len(letters) - 1:
                print(" " + str(numbers[x]) + " " + letters[x] + "'s", end =" ")
            else:
                print(" " + str(numbers[x]) + " " + letters[x] + "'s,", end =" ")
        
        print()
    
def Length(a, b):
    return len(a) == len(b)

def Sum(a):
    sum = 0
    
    for x in a:
        sum += x
    
    return sum
    
def Average(a):
    average = 0
    
    for x in a:
        average += x
    
    if len(a) == 0:
        return 0
    else:
        return average / len(a)
    
def Diff(a, b):
    sum1 = Sum(a)
    sum2 = Sum(b)
    
    return sum1 != sum2

def Common(a, b):
    c = []
    
    for x in a:
        if x in b and x not in c:
            c.append(x)
    
    return c

picked = False

while picked == False:
    choice = input("Enter 1 to enter names or enter 2 to enter numbers: ")

    if choice.isdigit():
        if choice == "1" or choice == "2":
            picked = True
            print()
        else:
            print("Error: invalid input")
    else:
        print("Error: invalid input")
        
list1 = []
list2 = []

fin = False

if choice == "1":
    while fin == False:
        name = input("Enter a name or enter 'stop' to stop: ")
        
        if name == "stop":
            fin = True
            print()
        else:
            word = True
            
            for x in name:
                if x.isdigit():
                    word = False
            
            if word:
                list1.append(name)
       
            print()
            
    Occurance(list1)
elif choice == "2":  
    while fin == False:
        num = input("Enter a number or enter 'stop' to stop: ")
        
        if num == "stop":
            fin = True
            print()
        elif num.isdigit():
            picked = False
            
            while picked == False:
                whichList = input("Enter 1 to put this value in list 1 or enter 2 to put this value in list 2: ")
                
                if whichList.isdigit():
                    if whichList == "1":
                        list1.append(int(num))
                        picked = True
                    elif whichList == "2":
                        list2.append(int(num))
                        picked = True
                    else:
                        print("Error: invalid input")
                else:
                    print("Error: invalid input")
            
            print()
        else:
            print("Error: invalid input")

    print("The two lists are the same length: " + str(Length(list1, list2)))
    print("The sum of the numbers in list 1 is: " + str(Sum(list1)) + " and the sum of the numbers in list 2 is: " + str(Sum(list2)))
    print("The average of the first list is: " + str(Average(list1)) + ", the average of the second list is: " + str(Average(list2)))
    print("The sum of the two lists are different: " + str(Diff(list1, list2)))
    print("The common numbers between the two lists are: " + str(Common(list1, list2)))
