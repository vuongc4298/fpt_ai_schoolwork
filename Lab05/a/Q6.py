def selection_sort_asc(iter):
    for i in range(1, len(iter)):
        print('i =', i)
        m = iter[i-1]
        print('m=', m)
        if m > min(iter[i:]):
            temp = m
            m = min(iter[i:])
            index = iter[i:].index(m) + i
            print('min =', m)
            iter[i-1] = m
            iter[index] = temp
            print(f'iteration {i}, swapped {temp} and {m}')
    return iter

def sequential_search(iter, key):
    count = 0
    for i in range(len(iter)):
        if iter[i] == key:
            print(f"Found {key} at position {i}")
            count += 1
        else:
            continue
    if not count:
        print(f"{key} not found!")
    return count

def binary_search_recursive(iter, key, low, high):
    mid = (low + high) // 2

    if high >= low:
        if iter[mid] == key:
            return mid
        
        elif iter[mid] > key:
            return binary_search_recursive(iter, key, low, mid - 1)

        elif iter[mid] < key:
            return binary_search_recursive(iter, key, mid + 1, high)
    else:
        return -1

def binary_search_iterative(iter, key):
    low = 0
    high = len(iter) - 1
    mid = 0

    while high >= low:
        mid = (high + low) // 2
        if iter[mid] > key:
            high = mid - 1
        elif iter[mid] < key:
            low = mid + 1
        else:
            return mid
    return -1

lst = [5, 3, 7, 9, 5, 12, 42, 1, 6, 8]
print(selection_sort_asc(lst))
sequential_search(lst, 5)
sequential_search(lst, 13)

print(lst[binary_search_iterative(lst, 8)])
print(lst[binary_search_recursive(lst, 8, 0, len(lst)-1)])
