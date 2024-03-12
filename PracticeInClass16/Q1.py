class Main:
    
    #====================f1====================
    def f1(self, inputString):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        lst = inputString.split(",")
        for element in lst:
            print(element.strip())
        pass
        # end def


    #====================f2====================
    def f2(self, inputString):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        lst = inputString.split(",")    
        for i in range(len(lst)):
            lst[i] = lst[i].strip().split(" ")
        dic = dict()
        for key, value in lst:
            if key not in dic:
                dic[key] = int(value)
            else:
                dic[key] += int(value)
        vertical = 0
        horizontal = 0
        for key in dic.keys():
            if key == "UP":
                vertical += int(dic[key])
            elif key == "DOWN":
                vertical -= int(dic[key])
            elif key == "LEFT":
                horizontal -= int(dic[key])
            elif key == "RIGHT":
                horizontal += int(dic[key])
            else:
                print("Invalid input")
        distance = int((vertical ** 2 + horizontal ** 2) ** 0.5)
        print(distance)
        pass
        # end def

#================DO NOT CHANGE THE CODE BELOW===============================
    def main(self):
        print(" 1. Test f1 (2 mark)")
        print(" 2. Test f2 (1 mark)")
        print(" Your selection (1 -> 2): ")
        choice = int(input())
        inputString = input()
        print("OUTPUT")
        if choice == 1:
            self.f1(inputString)
        elif choice == 2:
            self.f2(inputString)
        else:
            print("Wrong select")
        print("FINISH")
main = Main()
main.main()

