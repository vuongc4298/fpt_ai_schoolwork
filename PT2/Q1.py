def getString(prompt):
    string = input(prompt)
    return string

def getChar1(prompt):
    char1 = input(prompt)
    return char1

def getChar2(prompt):
    char2 = input(prompt)
    return char2

def replaceChars(string, char1, char2):
    return string.replace(char1, char2)

string = getString("Enter string: ")
char1 = getChar1("Enter char: ")
char2 = getChar2("Enter replacement char: ")
print(replaceChars(string, char1, char2))