def trapezoid(func, lower, upper, traps):
    integral = 0
    deltaX = (upper - lower) / traps
    k = 1
    
    while k <= traps:
        if func == 1:
            integral += (10 * (((lower + (deltaX * k)) + (lower + (deltaX * (k + 1)))) / 2)**2) * deltaX
        elif func == 2:
            integral += (2 * (((lower + (deltaX * k)) + (lower + (deltaX * (k + 1)))) / 2)**2 - 5) * deltaX
        elif func == 3:
            integral += ((((lower + (deltaX * k)) + (lower + (deltaX * (k + 1)))) / 2) + 20) * deltaX
        
        k += 1
    
    return integral

def rectangle(func, lower, upper, recs):
    integral = 0
    deltaX = (upper - lower) / recs
    k = 1
    
    while k <= recs:
        if func == 1:
            integral += (10 * (lower + (deltaX * k))**2) * deltaX
        elif func == 2:
            integral += (2 * (lower + (deltaX * k))**2 - 5) * deltaX
        elif func == 3:
            integral += ((lower + (deltaX * k)) + 20) * deltaX
        
        k += 1
        
    return integral

def summation(func, lower, upper):
    sum = 0
    x = lower
    
    while x <= upper:
        if func == 1:
            sum += 10 * x**2
        elif func == 2:
            sum += 2 * x**2 - 5
        elif func == 3:
            sum += x + 20
        
        x += 1
    
    return sum

done = False

while done == False:
    right = False
    
    while right == False:
        choose = int(input("Enter 1 to find the summation or enter 2 to find the integration: "))
        
        if choose == 1 or choose == 2:
            print()
            right = True
        else:
            print("Error: invalid input")

    print("f1(x) = 10x^2")
    print("f2(x) = 2x^2 - 5")
    print("f3(x) = x + 20")
    
    while right:
        function = int(input("Enter 1 for f1, enter 2 for f2, or enter 3 for f3: "))
        
        if function == 1 or function == 2 or function == 3:
            print()
            right = False
        else:
            print("Error: invalid input")
    
    lowerBound = int(input("What is the lower bound: "))
    upperBound = int(input("What is the upper bound: "))
    print()
    
    if choose == 1:
        print("The answer is " + str(summation(function, lowerBound, upperBound)) + "\n")
    if choose == 2:
        while right == False:
            areaMethod = int(input("Enter 1 for the rectangle method or enter 2 for the trapezoid method: "))
            
            if areaMethod == 1 or areaMethod == 2:
                print()
                right = True
            else:
                print("Error: invalid input")
        
        works = False
        
        if areaMethod == 1:
            while works == False:
                rectangles = int(input("Enter the number of rectangles you want to use: "))
                
                if rectangles > 0:
                    works = True
                else:
                    print("Error: invalid input")
                    
            print("\nThe answer is " + str(rectangle(function, lowerBound, upperBound, rectangles)) + "\n")
        elif areaMethod == 2:
            while works == False:
                trapezoids = int(input("Enter the number trapezoids you want to use: "))
                
                if trapezoids > 0:
                    works = True
                else:
                    print("Error: invalid input")
            
            print("\nThe answer is " + str(trapezoid(function, lowerBound, upperBound, trapezoids)) + "\n")
    
    retry = False
    
    while retry == False:
        end = int(input("Enter 1 to do another calculation or enter 2 to exit: "))
        
        if end == 1:
            print()
            retry = True
        elif end == 2:
            retry = True
            done = True
        else:
            print("Error: invalid input")