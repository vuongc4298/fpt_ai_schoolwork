class Pupil:
    def __init__(self, rollno, name, grade):
        self.rollno = rollno
        self.name = name
        self.grade = grade
    
class PupilManager:
    subjects = ["English", "Maths", "Physics", "Chemistry", "CS"]

    def __init__(self):
        self.pupils = []
    
    def main_menu(self):
        while True:
            print("\nMAIN MENU:")
            print("1. REPORT")
            print("2. ADMIN")
            print("3. EXIT")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.report_menu()
            elif choice == '2':
                self.admin_menu()
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    def admin_menu(self):
        while True:
            print("\nADMIN MENU:")
            print("1. CREATE PUPIL RECORD")
            print("2. DISPLAY ALL PUPIL RECORDS")
            print("3. SEARCH PUPIL RECORD")
            print("4. MODIFY PUPIL RECORD")
            print("5. DELETE PUPIL RECORD")
            print("6. BACK TO MAIN MENU")

            admin_choice = input("Enter your choice: ")

            if admin_choice == '1':
                self.create_pupil_record()

            elif admin_choice == '2':
                self.display_all_pupil_records()

            elif admin_choice == '3':
                self.search_pupil_record()

            elif admin_choice == '4':
                self.modify_pupil_record()

            elif admin_choice == '5':
                self.delete_pupil_record()

            elif admin_choice == '6':
                break

            else:
                print("Invalid choice. Please try again.")

    def get_pupil(self, rollno):
        for pupil in self.pupils:
            if pupil.rollno == rollno:
                return pupil
        return False
    
    def create_pupil_record(self):
        flag = 'y'
        while flag == 'y':
            rollno = input("Enter roll number: ")
            name = input("Enter name: ")
            grade = dict()
            for subject in self.subjects:
                grade[subject] = input((f"Enter Marks in {subject}: "))
            pupil = Pupil(rollno, name, grade)
            self.pupils.append(pupil)
            flag = input("Want to enter more record (y/n)?: ")

    def report_menu(self):
        while True:
            print("\nREPORT MENU:")
            print("1. CLASS RESULT")
            print("2. PUPIL REPORT CARD")
            print("3. BACK TO MAIN MENU")

            report_choice = input("Enter your choice: ")

            if report_choice == '1':
                self.class_result()
                pass
            elif report_choice == '2':
                self.pupil_report_card()
                pass
            elif report_choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")        
    
    def display_all_pupils(self):
        print("PUPIL DETAILS...")
        for pupil in self.pupils:
            print(f"Roll Number: {pupil.rollno}")
            print(f"Name: {pupil.name}")
            for subject in self.subjects:
                print(f"{subject}: {pupil.grade[subject]}")
    
    def search_pupil_record(self):
        rollno = input("Enter the rollno you want to search: ")
        pupil = self.get_pupil(rollno)
        if not pupil:
            print("Pupil not found.")
        else:
            print("PUPIL DETAILS...")
            print(f"Roll Number: {pupil.rollno}")
            print(f"Name: {pupil.name}")
            for subject in self.subjects:
                print(f"{subject}: {pupil.grade[subject]}")

    def modify_pupil_record(self):
        print("MODIFY RECORD")
        rollno = input("Enter roll number: ")
        pupil = self.get_pupil(rollno)
        if not pupil:
            print("Pupil not found.")
        else:
            print(f"Name: {pupil.name}")
            edit = input("Want to edit (y/n)?")
            if edit == 'n':
                pass
            elif edit == 'y':
                new_name = input("Enter new name: ")
                pupil.name = new_name
            for subject in self.subjects:
                print(f"{subject}: {pupil.grade[subject]}")
                edit = input("Want to edit (y/n)?")
                if edit == 'n':
                    pass
                elif edit == 'y':
                    new_grade = input(f"Enter new grade for {subject}: ")
                    pupil.grade[subject] = new_grade
            print("Record updated")
            print("PUPIL DETAILS...")
            print(f"Roll Number: {pupil.rollno}")
            print(f"Name: {pupil.name}")
            for subject in self.subjects:
                print(f"{subject}: {pupil.grade[subject]}")

    def delete_pupil_record(self):
        print("DELETE RECORD")
        rollno = input("Enter roll number: ")
        pupil = self.get_pupil(rollno)
        if not pupil:
            print("Pupil not found.")
        else:
            print("PUPIL DETAILS...")
            print(f"Roll Number: {pupil.rollno}")
            print(f"Name: {pupil.name}")
            for subject in self.subjects:
                print(f"{subject}: {pupil.grade[subject]}")
            self.pupils.remove(pupil)
            print("Record found and deleted")

    def class_result(self):
        headers = "RollNo" + "{:<20}".format("Name") + "".join("{:<10}".format(subject for subject in self.subjects))
        print(headers)
        for pupil in self.pupils:
            s = "RollNo" + "{:<20}".format("Name") + "".join("{:<10}".format(pupil.grade[subject] for subject in self.subjects))
            print(s)

    def pupil_report_card(self):
        rollno = input("Enter the rollno you want to search: ")
        pupil = self.get_pupil(rollno)
        if not pupil:
            print("Pupil not found.")
        else:
            print("PUPIL DETAILS...")
            print(f"Roll Number: {pupil.rollno}")
            print(f"Name: {pupil.name}")
            for subject in self.subjects:
                print(f"{subject}: {pupil.grade[subject]}")

pupil_manager = PupilManager()
pupil_manager.main_menu()
