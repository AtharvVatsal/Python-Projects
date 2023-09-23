import math         #imported math module for use in complex calculations

def add(a, b):      #defined function fo addition
    return a + b    
def sub(a, b):      #defined function for substraction
    return a - b
def mul(a, b):      #defined function for multiplication
    return a*b
def div(a, b):      #defined function for division
    return a/b
def exp(a, b):      #defined function for exponent of 2 number
    return a**b
def remain(a, b):   #defined function for finding remainder
    return a%b

user = int(input("""
Enter 1 for addition            |
Enter 2 for substraction        |
Enter 3 for multiplication      |
Enter 4 for Division            |
Enter 5 for Exponents           |
Enter 6 for finding remainder   |
Enter 7 for More options.       | 
                                """))

while user == 1:
    num1 = float(input("Enter First Number "))
    num2 = float(input("Enter Second Number "))
    print(f"Addition ({num1} + {num2})-> {add(num1, num2)}")
    break

while user == 2:
    num1 = float(input("Enter First Number "))
    num2 = float(input("Enter Second Number "))
    print(f"Substraction ({num1} - {num2})-> {sub(num1, num2)}")
    break

while user == 3:
    num1 = float(input("Enter First Number "))
    num2 = float(input("Enter Second Number "))
    print(f'Multiplied ({num1} x {num2}) -> {mul(num1, num2)}')
    break

while user == 4:
    num1 = float(input("Enter First Number "))
    num2 = float(input("Enter Second Number "))
    print(f"Division ({num1} / {num2})-> {div(num1, num2)}")
    break

while user == 5:
    num1 = float(input("Enter First Number "))
    num2 = float(input("Enter Second Number "))
    print(f"Powered ({num1}^{num2})-> {exp(num1, num2)}")
    break

while user == 7:
    choice = int(input("""
1 for square root           |
2 for Trignometric Functions|
3 for Exponential Functions |
4 for Logarithmic Functions |
5 for Absolute Value        |
                            """))
    
    if choice == 1:
        num = float(input("Enter The Number: "))
        print(f"Square Root of {num} = {math.sqrt(num)}")
        break
    elif choice == 2:
        tf = int(input("""
1 for Sin
2 for Cos
3 for Tan
4 for Cosec
5 for Sec
6 for Cot"""))
        units = str(input("Enter 'd' for Degree use and 'r' for radian use: ")).lower()
        angle = float(input("Enter Angle: "))
        if tf == 1:
            if units == "d":
                angle = math.radians(units)
                sin = math.sin(angle)
                print(f"Sin = {sin}")
                break
            elif units == 'r':
                sin = math.sin(angle)
                print(f"Sin = {sin}")
                break
        elif tf == 2:
            if units == 'd':
                angle = math.radians(angle)
                cos = math.cos(angle)
                print(f"Cos = {cos}")
                break
            else:
                cos = math.cos(angle)
                print(f"Cos = {cos}")
                break
        elif tf == 3:
            if units == 'd':
                angle = math.radians(angle)
                tan = math.tan(angle)
                print(f"Tan = {tan}")
                break
            else:
                tan = math.tan(angle)
                print(f"Tan = {tan}")
                break
        elif tf == 4:
            if units == 'd':
                angle = math.radians(angle)
                cosec = (1/math.sin(angle))     #cosec = 1/sin
                print(f"Cosec = {cosec}")
                break
            else:
                cosec = (1/math.sin(angle))
                print(f"Cosec = {cosec}")
                break
        elif tf == 5:
            if units == 'd':
                angle = math.radian(angle)
                sec = (1/math.cos(angle))       #sec = 1/cos
                print(f"Secant = {sec}")
                break
            else:
                sec = (1/math.cos(angle))
                print(f"Secant = {sec}")
                break
        elif tf == 6:
            if units == 'd':
                angle = math.radians(angle)
                cot =(1/math.tan(angle))        #cot = 1/tan
                print(f"COt = {cot}") 
                break     
    elif choice == 3:
        num = float(input("Enter Your Number "))
        expo = math.exp(num)                                    #e^(number)
        print(f"e raised to given number = {expo}")
        break
    elif choice == 4:
        num = float(input("Enter Number of Your Choice "))
        loga = math.log(x)                                     #log(x)
        print(f"Log of given number to base e = {loga}")        #  e
        break
    elif choice == 5:
        num = float(input("Enter Number of Your Choice "))
        abso = round(num)
        print(f"Rouned Value = {abso}")
        break
    else:
        print("Invalid Input ,Re-run Program")
        break
else:
     print("Invalid Input, Re-Run Program")