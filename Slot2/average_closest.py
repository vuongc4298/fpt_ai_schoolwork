def array_average_closest(arr):
    ave = sum(arr)/len(arr)
    closest = min(arr, key = lambda x: abs(x - ave))
    pos = arr.index(closest)
    return pos

def main():
    try:
        input_func = raw_input #python2
    except NameError:
        input_func = input #python3
        
    print("Start")
    flag = 0
    while flag == 0:
        try:
            size = int(input_func("Enter the length of the array: "))
            arr = [0] * size

            for i in range(size):
                arr[i] = float(input_func(f"Input the element {i + 1}: "))
            result = array_average_closest(arr)

            print(f"The position of the element that has the value nearest to the average of the array is: {result}")
            flag = 1
            print("Finish")

        except ValueError:
            print("Please enter a number")
        except ZeroDivisionError:
            print("The size of the array must be large than 0")
        except Exception as e:
            print("An error has occurred: ", e)

if __name__ == "__main__":
    main()
