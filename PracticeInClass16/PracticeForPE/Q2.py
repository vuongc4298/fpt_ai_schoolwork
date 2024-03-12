def equalSum(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            print("YES")
            return 1
    print("NO")
    return 0

lst = [2, 1, 4, 3, 5, 4, 3, 2, 1]
equalSum(lst)