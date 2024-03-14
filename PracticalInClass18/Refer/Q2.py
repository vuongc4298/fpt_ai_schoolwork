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
        arr.append(x)

def solve():
    numList = []
    getList(numList)
    n = len(numList)
    if (n == 0 or n == 1): return False
    else:
        for i in range(n):
            if sum(numList[:i]) == sum(numList[i+1:]):
                return True
    return False
if (solve()): print("YES")
else: print("NO")