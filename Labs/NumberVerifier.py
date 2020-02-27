def is_floating_pt(value):
    decimal = 0
    
    for x in range(len(value)):
        if value[x] >= '0' and value[x] <='9':
            continue
        elif value[x] == '-' and x == 0:
            continue
        elif value[x] == '.' and decimal == 0:
            decimal = 1
        else:
            return False   
            
    if decimal == 1:
        return True
    else:
        return False

def is_integer(value):
    count = 0
    
    for x in value:
        if x >= '0' and x <='9':
            continue
        elif x == '-' and count == 0:
            continue
        else:
            return False   
        
        count += 1
    
    return True

choice = int(input("Enter 1 to enter a signed integer or enter 2 to enter a floating-point number: "))

if choice == 1:
    value = input("Enter an integer: ")
    print(is_integer(value))
elif choice == 2:
    value = input("Enter a float: ")
    print(is_floating_pt(value))