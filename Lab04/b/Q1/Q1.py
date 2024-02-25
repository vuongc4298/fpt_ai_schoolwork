path = "./Lab04/b/Q1/"


with open(f"{path}poem.txt", "r") as file: #1.1
    for line in file:
        print(line.strip())

with open(f"{path}story.txt", "r") as file: #1.2
    count = sum(1 for line in file.readlines() if not line.startswith("T"))
    print(f"Number of lines not starting with T: {count}")


