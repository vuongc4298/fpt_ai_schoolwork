def isPalindrome(s):
    for i in range(0, int(len(s)/2)):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

def maxima(lst):
    m = 0
    for i in lst:
        if i > m:
            m = i
    return m

a = input("Original number: ")
if isPalindrome(a):
    print("The given number is palindrome")
else:
    print("The given number is not palindrome")

x = [4, 6, 8, 24, 12, 2]
print(maxima(x))
print(max(x))