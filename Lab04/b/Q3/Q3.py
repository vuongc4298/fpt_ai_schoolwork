path = "./Lab04/b/Q3/"

def count_upper():
    with open(f"{path}article.txt", "r") as file:
        count = sum(1 for c in file.read() if c.isupper())
    print(count)

def count_this_these():
    with open(f"{path}article.txt", "r") as file:
        content = file.read()
        count_this = content.count("this")
        count_This = content.count("This")
        count_these = content.count("these")
        count_These = content.count("These")
    print(count_this + count_these + count_This + count_These)

count_upper()
count_this_these()