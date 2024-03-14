import random

flag = 0
i = 1

print("Ball lottery")
print("===============")
inp = int(input("Total sought: "))
while flag == 0:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    print(f"Result of picks {i} and {i+1}: {a} + {b}")
    if a + b == inp:
        print(f"You got your total in {i+1} picks!")
        break
    i+=2
    


