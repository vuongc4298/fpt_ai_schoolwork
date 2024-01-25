import random

def display_number(arr):
    for num in arr:
        if num > 500:
            break
        elif num > 150:
            continue
        elif num % 5 == 0:
            print(num)

def digits_count(n):
    count = 0
    for d in str(n):
        count += 1
    return count

def print_list_reverse(arr):
    for i in range(len(arr)-1, -1, -1):
        print(arr[i])

def main():
    try:
        input_func = raw_input
    except NameError:
        input_func = input
    
    lst = [13, 25, 50, 35, 195, 650, 99, 458, 5]
    print("Printing list")
    print(lst)
    print("Printing divisible by 5") #Q2_1
    display_number(lst)
    print("Printing list in reverse") #Q2_3
    print_list_reverse(lst)
    n = random.randint(0, 100000000000)
    print(f"Printing digits count for {n}: {digits_count(n)}") #Q2_2

if __name__=="__main__":
    main()