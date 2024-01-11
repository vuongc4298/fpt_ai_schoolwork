def func1(*args):
    print("Printing values")
    for arg in args:
        print(arg)

def calculation(a, b):
    return a+b, a-b

func1(20, 40, 60)
func1(80, 100)

res = calculation(40, 10)
print(res)