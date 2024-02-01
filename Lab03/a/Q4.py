def string_removal(s):
    res = ''
    for i in s:
        if i.isdigit():
            res += i
    return res

def remove_special(s):
    res = ''
    for i in s:
        if i.isalnum() or i == ' ':
            res += i
    return res

def remove_empty_string(lst):
    return [i for i in lst if i]

str1 = 'I am 25 years and 10 months old'
str2 = '/+Jon is @developer & musician'
str_lst = ['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']
str3 = 'Emma-is-a-data-scientist'

print(string_removal(str1))
print(remove_special(str2))
print(remove_empty_string(str_lst))
print(str3.split('-'))