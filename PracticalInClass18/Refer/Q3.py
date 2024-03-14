import random

n = random.randint(1, 100)

def getInput(prompt):
    x = input(prompt)
    while True:
        try:
            x = int(x)
        except:
            print("Error, please enter numeric input")
            x = input(prompt)
        else:
            break
    return int(x)

userNum = 0
while(userNum != n):
    userNum = getInput("Guess the value of x: ")
    if (userNum == n):
        print("EXACTLY!")
        break
    if (userNum > n): print("n < x")
    if (userNum < n): print("n > x")