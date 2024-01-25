def print_triangle(n):
    for i in range(1, n + 1):
        s = ""
        for j in range(1, i + 1):
            s += f"{j} "
        print(s)

def sum(n):
    s = 0
    for i in range(1, n+1):
        s += i
    return s

def main():
    try:
        input_func = raw_input
    except NameError:
        input_func = input

    while True:
        try:
            n = int(input_func("Enter a natural number: "))
        except ValueError:
            print("Invalid input. Please enter a natural number")
            continue
        except Exception as e:
            print(f"Error: {e}")
        
        if n < 0:
            print("Invalid input. Please enter a natural number")
            continue
        break
    print_triangle(n) #Q1_1
    print(f"Sum is: {sum(n)}") #Q1_2
    
if __name__=="__main__":
    main()