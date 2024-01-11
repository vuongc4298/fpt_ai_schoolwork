def showEmployee(name, salary=9000):
    print(f"Name: {name} salary: {salary}")

def inner_fun(a, b):
    return a + b

def outer_fun(a, b):
    return inner_fun(a, b) + 5


showEmployee("Ben", 12000)
showEmployee("Jessa")

result = outer_fun(5, 10)
print(result)