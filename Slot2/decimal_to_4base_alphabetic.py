def grade_convert(dgrade, mappings):
    for (t, grade) in mappings:
        if dgrade >= t:
            return grade
    return mappings[-1][1]

def main():
    try:
        input_func = raw_input #python2
    except NameError:
        input_func = input #python3
        
    flag = 0
    alphabetic = [(8.5, "A"), (7.0, "B"), (5.5, "C"), (4.0, "D"), (0.0, "F")]
    base4 = [(8.5, "4"), (7.0, "3"), (5.5, "2"), (4.0, "1"), (0.0, "0")]

    while flag == 0:
        try:
            grade = float(input_func("Enter the decimal grade (0 to 10): "))
            if 0 <= grade <= 10:
                print(f"Alphabetic grade is {grade_convert(grade, alphabetic)}")
                print(f"Base 4 grade is {grade_convert(grade, base4)}")
                flag = 1
            else:
                print("Invalid grade (not between 0 and 10). Please try again.")

        except ValueError:
            print("Invalid grade (not a nubmer). Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
