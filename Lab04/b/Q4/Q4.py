path = "./Lab04/b/Q4/"

def hash_display():
    with open(f"{path}matter.txt", 'r') as file:
        content = file.read()
        modded_content = "#".join(content)
    print(modded_content)

def JTOI():
    with open(f"{path}WORDS.TXT", 'r') as file:
        content = file.read()
        modded_content = content.replace("J", "I")
    print(modded_content)

hash_display()
JTOI()