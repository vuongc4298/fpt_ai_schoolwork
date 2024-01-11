def addition(n):
    if n == 0:
        return 0
    return n + addition(n-1)

def display_student(name, age):
    print(name, age)

show_student = display_student

res = addition(10)
print(res)

display_student("Emma", 26)
show_student("Emma", 26)