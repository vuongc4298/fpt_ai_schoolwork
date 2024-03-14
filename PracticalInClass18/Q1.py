def is_prime(n):
    if n == 1:
        return True
    elif n < 2:
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
    return lst, flag
print("The prime numbers")
print("=================")
while True:
    try:
        s = input("The sequence of numbers: ")
        if not s.split():
            print("Please enter at least one integer")
            continue
        lst, flag = is_prime_list(s)
        prime_lst = sorted(lst)
        if flag < 0:
            print("Invalid input, please enter only positive integers")
            continue
        if not prime_lst:
            print("There are no prime numbers in the list")
        else:
            prime_str = " ".join(str(prime) for prime in prime_lst)
            print(f"The prime numbers: {prime_str}")
            print(f"The largest number: {max(prime_lst)}")
            print(f"You got the total of the prime number: {sum(prime_lst)}")
        break 

    except ValueError:
        print("Invalid input. Please enter positive integers")
    except Exception as e:
        print(f"Error: {e}")