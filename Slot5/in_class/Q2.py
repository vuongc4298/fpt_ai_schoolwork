def display_number(arr):
    for num in arr:
        if num > 500:
            break
        elif num > 150:
            continue
        elif num % 5 == 0:
            print(num)
    
def digits_sum(n):
    result = 0
    for d in str(n):
        result += int(d)
    return result

def main():
    try:
        input_func = raw_input
    except NameError:
        input_func = input
    
    lst = [13, 25, 50, 35, 195, 650, 99, 458, 5]
    print("Printing divisible by 5")
    display_number(lst)

    while True:
        try:
            n = float(input_func("Enter number n:"))
        