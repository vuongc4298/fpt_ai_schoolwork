def unique_character_frequency(s):
    char_count = dict()
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    print("Printing unique characters and their frequencies")
    print("\n")
    for char, count in char_count.items():
        print(f"{char}\t{count}")

def print_triangle(n):
    for i in range(1, n + 1):
        s = ""
        for j in range(1, i + 1):
            s += "* "
        print(s)

def print_isocesles_tri(n):
    for i in range(1, 2 * n + 1, 2):
        spaces = (2 * n - 1 - i) // 2
        print(' ' * spaces + '*' * i)

def char_type_count(s):
    letter_count = 0
    digit_count = 0
    other_count = 0
    for char in s:
        if char.isalpha():
            letter_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            other_count += 1
    print(f"numberOfLetters: {letter_count}")
    print(f"numberOfDigits: {digit_count}")
    print(f"numberOfOther: {other_count}")

char_type_count("Hom nay Hanoi troi rat lanh.")   
unique_character_frequency("Hom nay Hanoi troi rat lanh.")
print_triangle(10)
print_isocesles_tri(6)
print_isocesles_tri(7)