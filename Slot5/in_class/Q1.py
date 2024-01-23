def print_pyramid(n):
    for i in range(1, n+1):
        s = ''
        for j in range(1, i+1):
            s += str(j) + ' '
        print(s)

def addition_loop(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result
    
def main():
    try:
        input_func = raw_input #python2
    except NameError:
        input_func = input #python3
    
    while True:
        try:
            n = int(input_func("Enter integer n larger than 0: "))
            if n < 1:
                print("Invalid value. Please re-enter")
                continue
            break
        except ValueError:
            print("Please enter a valid integer number")
        except Exception as e:
            print(f"Error: {e}")
    print("Printing pyramid")
    print_pyramid(n) #Q1_1

    while True:
        try:
            n = int(input_func("Re-enter integer n larger than 0: "))
            if n < 1:
                print("Invalid value. Please re-enter")
                continue
            break
        except ValueError:
            print("Please enter a valid integer number")
        except Exception as e:
            print(f"Error: {e}")

    print(f"Sum is: {addition_loop(n)}") #Q1_2

if __name__ == "__main__":
    main()