class Employee():
    def __init__(self, code, name, salary, allowance):
        self.__code = code
        self.__name = name
        self.__salary = salary
        self.__allowance = allowance
    def getCode(self):
        return self.__code
    def getName(self):
        return self.__name
    def getSalary(self):
        return self.__salary
    def getAllowance(self):
        return self.__allowance
    
    def setCode(self, code):
        self.__code = code
    def setName(self, name):
        self.__name = name
    def setSalary(self, salary):
        self.__salary = salary
    def setAllowance(self, allowance):
        self.__allowance = allowance
    
    def displayInfo(self):
        print(self.getCode())
        print(self.getName())
        print(self.getSalary())
        print(self.getAllowance())

class EmployeeTree():
    employeeList = list()
    fin = "input.txt"
    fout = "result.txt"
    def inputInfo(self, employee):
        with open(self.fin, 'w') as file:
            file.write(f"{employee.getCode()}\n")
            file.write(f"{employee.getName()}\n")
            file.write(f"{employee.getSalary()}\n")
            file.write(f"{employee.getAllowance()}\n")
    
    def outputInfo(self, file, employee):
        file.write(f"{employee.getCode()}\n")
        file.write(f"{employee.getName()}\n")
        file.write(f"{employee.getSalary()}\n")
        file.write(f"{employee.getAllowance()}\n")

    def insertEmployee(self, employee):
        index = len(self.employeeList)
        for i in range(len(self.employeeList)):
            if self.employeeList[i].getCode() > employee.getCode():
                index = i
                break
        # print(index)
        if index == len(self.employeeList):
            self.employeeList.append(employee)
        else:
            self.employeeList = self.employeeList[:index] + [employee] + self.employeeList[index:]

    def addEmployee(self):
        code = input("\nEnter employee code: ")
        code = int(code)
        name = input("Enter employee name: ")
        salary = input("Enter employee salary: ")
        allowance = input("Enter employee allowance: ")
        employee = Employee(code, name, salary, allowance)

        self.insertEmployee(employee)
        self.inputInfo(employee)

    def binarySearchEmployee(self, code):
        left = 0
        right = len(self.employeeList) - 1
        
        while left <= right:
            mid = (left + right) // 2
            # print("Left:", left, "Right:", right, "Mid:", mid)
            # print("Type of code at mid:", type(self.employeeList[mid].getCode()))
            # print("Type of searching code:", type(code))
            # print("Code at mid:", self.employeeList[mid].getCode())
            # print("Searching for code:", code)
            if int(self.employeeList[mid].getCode()) == code:
                # print("Employee found at index:", mid)
                return mid
            elif int(self.employeeList[mid].getCode()) < code:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
    
    def searchEmployee(self):
        code = int(input("\nEnter code: "))
        index = self.binarySearchEmployee(code)
        print("Search result index:", index)
        if index is False:
            print("Employee doesn't exist")
        else:
            self.employeeList[index].displayInfo()

    def deleteEmployee(self):
        code = int(input("\nEnter code: "))
        index = self.binarySearchEmployee(code)
        if not index:
            print("Employee doesn't exist")
        else:
            self.employeeList[index].displayInfo()
        self.employeeList.pop(index)
        print("Deletion complete")
    
    def salaryAllowanceDesc(self):
        sortedEmployeeList = sorted(self.employeeList, key = lambda x: int(x.getSalary()) + int(x.getAllowance()), reverse = True)
        with open(self.fout, "w") as file:
            for employee in sortedEmployeeList:
                self.outputInfo(file, employee)
        print("\nOutput completed")

    def mainMenu(self):
        while True:
            print("\nMAIN MENU:")
            print("1. ADD NEW EMPLOYEE")
            print("2. SEARCH EMPLOYEE BY CODE")
            print("3. DELETE EMPLOYEE")
            print("4. OUTPUT DESCENDING LIST OF SALARY + ALLOWANCE")
            print("5. EXIT")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.addEmployee()
            elif choice == '2':
                self.searchEmployee()
            elif choice == '3':
                self.deleteEmployee()
            elif choice == '4':
                self.salaryAllowanceDesc()
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        

employeeTree = EmployeeTree()
employeeTree.mainMenu()