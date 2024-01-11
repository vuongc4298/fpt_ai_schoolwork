def unique_elements_out(arr):
    seen = set()
    s =""
    for element in arr:
        if element not in seen:
            seen.add(element)
            s += str(element) +" "
    return s
    

def main():
    try:
        input_func = raw_input #python2
    except NameError:
        input_func = input #python3

    input_values = input_func()
    try:
        lst_str = input_values.split()
        # print(lst_str)
        lst_int = list(map(int, lst_str))
        # print(lst_int)
        print(unique_elements_out(lst_int))
    except ValueError:
        print("Invalid input. Enter valid integers separated by space.")

if __name__ == "__main__":
    main()

