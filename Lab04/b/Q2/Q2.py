path = "./Lab04/b/Q2/"

def display_words():
    s = ""
    with open(f"{path}story.txt", "r") as file:
        for word in file.read().split():
            if len(word) < 4:
                s += word + ' '
    print(s)
with open(f"{path}story.txt", "r") as file: #2.1
    count = sum(1 for word in file.read().split())
    print(f"Total words are: {count}")


display_words() #2.2