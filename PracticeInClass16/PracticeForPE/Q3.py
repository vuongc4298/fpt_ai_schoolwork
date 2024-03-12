import random

n = random.randint(1, 100)
while True:
    print("Guess the value of n")
    try:
        x = int(input(">>> "))
        if x < 1 or x > 100:
            print('The range of n is 1 to 100. Try again')
            continue
        if x == n:
            print("EXACTLY!")
            quit()
        elif n < x:
            print(f"n < {x}")
            continue
        elif n > x:
            print(f"n > {x}")
            continue
    except ValueError:
        print('n is an integer. Try again')
    