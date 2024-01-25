def middle_four(s, key = 0):
    middle_index = len(s) // 2                              #Combination of 2 functions below
    if key == 1:                                            #Taking key value of 0 for 
        return s[middle_index - 1: middle_index + 3]        #default or left shifted middle index
    return s[middle_index - 2: middle_index + 2]            #index, 1 for right shifted

# def middle_four_default_left_shift(s):                    Initial ideas
#     middle_index = len(s) // 2                            2 functions to deal with left
#     return s[middle_index - 2: middle_index + 2]          shifted and right shifted index
# def middle_four_right_shift(s):                           when dealing with string that has
#     middle_index = len(s) // 2                            odd number of characters
#     if len(s) % 2 == 0:
#         return s[middle_index - 2: middle_index + 2]
#     return s[middle_index - 1: middle_index + 3]
    
def insert_middle_right_shift(s1, s2):
    s1_middle_index = len(s1) // 2
    if len(s1) % 2 == 0:
        s1_first = s1[0:s1_middle_index]
        s1_second = s1[s1_middle_index:len(s1)]
        return s1_first + s2 + s1_second
    s1_first = s1[0:s1_middle_index+1]
    s1_second = s1[s1_middle_index+1:len(s1)]
    return s1_first + s2 + s1_second

def insert_middle_left_shift(s1, s2):
    s1_middle_index = len(s1) // 2
    s1_first = s1[0:s1_middle_index]
    s1_second = s1[s1_middle_index:len(s1)]
    return s1_first + s2 + s1_second

def first_middle_last_left_shift(s1, s2):
    s1_middle_index = len(s1) // 2 - 1 if len(s1) % 2 == 0 else len(s1) // 2
    s2_middle_index = len(s2) // 2 - 1 if len(s2) % 2 == 0 else len(s2) // 2
    s = s1[0] + s2[0] + s1[s1_middle_index] + s2[s2_middle_index] + s1[len(s1)-1] + s2[len(s2)-1]
    return s

def first_middle_last_right_shift(s1, s2):
    s1_middle_index = len(s1) // 2
    s2_middle_index = len(s2) // 2
    
    s = s1[0] + s2[0] + s1[s1_middle_index] + s2[s2_middle_index] + s1[len(s1)-1] + s2[len(s2)-1]
    return s

def lower_case_first(s):
    lower = ''
    other = ''
    for c in s:
        if c.islower():
            lower += c
        else:
            other += c
    return lower + other

def main():
    try:
        input_func = raw_input
    except NameError:
        input_func = input
    while True:
        s = input_func("Enter a string: ")
        if len(s) < 4:
            print("Insufficient length of string")
            continue
        # s = "BillDesctra"
        print(f"Original string: {s}")
        if len(s) % 2 == 0:
            print(f"Middle four characters are: {middle_four(s)}")
        else:
            print(f"Middle four characters, left shifted, are: {middle_four(s)}")
            print(f"Middle four characters, right shifted, are: {middle_four(s, 1)}")
        break

    s1 = "Aunt"
    s2 = "Kelly"
    print(insert_middle_left_shift(s1, s2))
    print(insert_middle_right_shift(s1, s2))
    

if __name__=="__main__":
    main()