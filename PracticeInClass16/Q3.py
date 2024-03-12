# ===YOU CAN ADD NEW CLASSES IN THE FOLLOWING PART========4
class Employee:
    
    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age
    def getName(self):
        return self.__name
    def getSalary(self):
        return self.__salary
    def getAge(self):
        return self.__age
    def printEmployee(self):
        print(self.getName())
        print(self.getSalary())
        print(self.getAge())
#=========================================================
class Main:

    #====EDIT THIS FUNCTION TO READ AND RETURN LIST EMPLOYEE========
    def InputListEmployee(self):
        n = input('Enter the number of employees: ')
        listEmployee = []
        for i in range(1, int(n) + 1):
            print(f"Enter employees {i}")
            name = input("Enter name: ")
            salary = input("Enter salary: ")
            age = input("Enter age: ")
            listEmployee.append(Employee(name, salary, age))

        return listEmployee
        # end def

    #====================f1====================
    def f1(self):
        #=======DO NOT EDIT CODE BELOW===============
        employeeList = self.InputListEmployee()
        print("OUTPUT")
        #==========================================

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        for i in range(len(employeeList)):
            print(f"Employees {i+1}")
            employeeList[i].printEmployee()
        pass
        # end def


    #====================f2====================
    def f2(self):
        #=======DO NOT EDIT CODE BELOW===============
        employeeList = self.InputListEmployee()
        print("OUTPUT")
        #==========================================
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========

        employeeList.sort(key = lambda x: x.getAge(), reverse = True)
        for i in range(len(employeeList)):
            print(f"Employees {i+1}")
            employeeList[i].printEmployee()

        pass
        # end def



    #====================f3====================
    def f3(self):
        #=======DO NOT EDIT CODE BELOW===============
        employeeList = self.InputListEmployee()
        print("OUTPUT")
        #==========================================
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        for employee in employeeList:
            if int(employee.getAge()) < 18:
                employeeList.remove(employee)
        employeeList.sort(key = lambda x: x.getSalary(), reverse = True)
        for i in range(len(employeeList)):
            print(f"Employees {i+1}")
            employeeList[i].printEmployee()

        pass
        # end def




#==================DO NOT CHANGE THE CODE BELOW=====================
    def main(self):
        print(" 1. Test f1 (1 mark)")
        print(" 2. Test f2 (2 mark)")
        print(" 3. Test f3 (1 mark)")
        print(" Your selection (1 -> 3): ")
        choice = int(input())
        
        if choice == 1:
            self.f1()
        elif choice == 2:
            self.f2()
        elif choice == 3:
            self.f3()
        else:
            print("Wrong select")
        print("FINISH")
main = Main()
main.main()

