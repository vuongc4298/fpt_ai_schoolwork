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

def getList(arr):
    n = getInput("Number of elements in the list: ")
    for i in range(n):
        x = getInput("Enter element: ")
        while (x < 0):
            print("Please enter positive integer!") 
            x = getInput("Enter element: ")
        arr.append(x)

def checkPrime(x):
    if (x < 2): return False
    for i in range(2, x):
        if (i * i > x): break
        if (x % i == 0): return False
    return True

numList = []
getList(numList)

primeList = []
for num in numList:
    if (checkPrime(num)): primeList.append(num)

print("Prime numbers: ", primeList)
print("Largest prime number: ", max(primeList))
