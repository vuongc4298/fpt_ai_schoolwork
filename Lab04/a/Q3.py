import os

path = "./Lab04/a/"
filename = f"{path}test.txt"

def seek_beginning(fname):
    with open(fname, 'r') as file:
        file.seek(0, os.SEEK_SET)
        print(file.read())

def seek_end(fname):
    with open(fname, 'r+') as file:
        file.seek(0, os.SEEK_END)
        file.write("\nThis content is added to the end of the file")
        file.seek(0, os.SEEK_SET)
        for line in file.readlines():
            print(line.strip())
    
def seek_current(fname, offset):
    with open(fname, 'rb') as file:
        while True:
            file.seek(offset, os.SEEK_CUR)
            line = file.readline().decode('utf-8')
            if line:
                print(line.strip().split(" ")[0])
                continue
            break

def seek_end_negative(fname, offset):   
    with open(fname, 'rb') as file:
        file.seek(offset, os.SEEK_END)
        lst = file.readline().decode('utf-8').split(" ")
        print(lst[0] + " " + lst[1])
        file.seek(-12, os.SEEK_CUR)
        print(file.readline().decode('utf-8').strip())

def demonstate_tell(fname):
    with open(fname, 'rb') as file:
        file.seek(75, os.SEEK_SET)
        print(file.tell())
        file.seek(20, os.SEEK_CUR)
        print(file.tell())
        file.seek(0, os.SEEK_SET)
        print(file.tell())
        print("***Printing file content***")
        print(file.read().decode('utf-8').strip())
        print("Demonstrating tell")
        print("***Done***")
        print(file.tell())

seek_beginning(filename)
print("*************")
seek_end(filename)
print("*************")
seek_current(filename, 3)
print("*************")
seek_end_negative(filename, -29)
print("*************")
demonstate_tell(filename)


