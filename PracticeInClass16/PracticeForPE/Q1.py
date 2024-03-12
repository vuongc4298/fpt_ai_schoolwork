def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
    return True

def is_prime_list(s):
    flag = 1
    arr = list(map(int, s.split()))
    lst = []
    for i in arr:
        if i < 1:
            flag = -1
        if is_prime(i):
            lst.append(i)
    lst = list(map(str, lst))
    return lst, flag

while True:
    try:
        s = input("Enter a sequence of positive integers: ")
        if not s.split():
            print("Please enter at least one integer")
            continue
        prime_lst, flag = is_prime_list(s)
        if flag < 0:
            print("Invalid input, please enter only positive integers")
            continue
        if not prime_lst:
            print("There are no prime numbers in the list")
        else:
            prime_str = " ".join(list(map(str, prime_lst)))
            print("Prime numbers:")
            print(f"{prime_str}")
            print("Maximum prime number in the sequence:")
            print(f"{max(prime_lst)}")
        break 

    except ValueError:
        print("Invalid input. Please enter positive integers")
    except Exception as e:
        print(f"Error: {e}")