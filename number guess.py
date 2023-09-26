import random
choice =int(input("""
    1 for easy (1-10)
    2 for medium (1-100)
    3 for hard (1-1000)

>>> """))
if choice == 1:
    count = 7
    taken = 0
    while taken <= count:
        num = int(input("Enter Your Guess: "))
        taken += 1
        dig = random.randint(1, 10)
        if num == dig:
            print("Woila, You Got Right Number")
            break
        elif num < dig:
            print("TOO LOW!")
        else:
            print("TOO HIGH")
            while taken > count:
                dig = dig
                print(f"The Number was {dig}")
                break
elif choice == 2:
    count = 7
    taken = 0
    while taken <= count:
        num = int(input("Enter Your Guess: "))
        taken += 1
        dig = random.randint(11, 100)
        if num == dig:
            print("Woila, You Got Right Number")
            break
        elif num < dig:
            print("TOO LOW!")
        else:
            print("TOO HIGH")
            while taken > count:
                dig = dig
                print(f"The Number was {dig}")
                break
elif choice == 3:
    count = 7
    taken = 0
    while taken <= count:
        num = int(input("Enter Your Guess: "))
        taken += 1
        dig = random.randint(1, 1000)
        if num == dig:
            print("Woila, You Got Right Number")
            break
        elif num < dig:
            print("TOO LOW!")
        else:
            print("TOO HIGH")
            while taken > count:
                dig = dig
                print(f"The Number was {dig}")
                break
else:
    print("Invalid Choice, Re-run")