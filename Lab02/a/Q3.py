def addition_recursive(n):
    if n == 0:
        return 0
    return n + addition_recursive(n-1)

def addition_formula(n):
    return n*(n+1)/2

def addition_loop(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result

def display_student(name, age):
    print(name, age)

show_student = display_student

print(addition_formula(10))
print(addition_loop(10))
print(addition_recursive(10))

display_student("Emma", 26)
show_student("Emma", 26)