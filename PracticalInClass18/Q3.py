class Menu:
    def mainMenu(self):
        while True:
            print("1-Processing data data")
            print("2-Character data")
            print("3-Quit")

            choice = input("Choose an operation: ")
            if choice == '1':
                self.processingDateData()

            elif choice == '2':
                self.characterData()

            elif choice == '3':
                print("Exiting...")
                break

            else:
                print("Invalid input. Please try again")
                continue


    def processingDateData(self):
        day = int(input("Enter the date: "))
        month = int(input("Enter the month: "))
        year = int(input("Enter the year: "))
        
        flag = 1
        if month < 1 or month > 12:
            flag = 0
        elif day < 1:
            flag = 0
        elif month in [1, 3, 5, 7, 8, 10, 12] and day > 31:
            flag = 0
        elif month in [4, 6, 9, 11] and day > 30:
            flag = 0
        elif month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                if day > 29:
                    flag = 0
            elif day > 28:
                flag = 0
                
        if flag:
            print("This date is valid")
        else:
            print("This date is not valid")

    def ascii_descending(self, start, end):
        st_code = ord(start)
        e_code = ord(end)
        if st_code > e_code:
            st_code, e_code = e_code, st_code
        for c in range(e_code, st_code-1, -1):
            print(f"{chr(c)}: {c}, {str(hex(c))[2:]}h")

    def characterData(self):
        c_list = input("Input: ")
        self.ascii_descending(c_list[0], c_list[1])

menu = Menu()
menu.mainMenu()