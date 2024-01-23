import math

def quadratic_polynomial(a, b, c, x):
    return a*x**2 + b*x + c

def check_solvability(a, b, c):
    if (b**2 - 4 * a * c) >= 0:
        return math.sqrt(b**2 - 4 * a * c)
    return 0

def check_triangle(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        return 1
    return 0

def perimeter_area_triangle(a, b, c):
    p = (a + b + c) / 2
    s = math.sqrt(p * (p-a) * (p-b) * (p-c))
    return p, s

def main():
    try:
        input_func = raw_input
    except NameError:
        input_func = input
    
    while True:
        try:
            a = float(input_func("Input real number a: "))
            b = float(input_func("Input real number b: "))
            c = float(input_func("Input real number c: "))
            x = float(input_func("Input real number x: "))  #Q3_1

            s1 = quadratic_polynomial(a, b, c, x)
            print(f"S1 = {s1}")                             #Q3_2

            s2 = check_solvability(a, b, c)                 #Q3_3 
            print(f"S2 = {s2}")

            break

        except ValueError:
            print("Please input valid real numbers")
        except Exception as e:
            print(f"Error: {e}")

    while True:
        try:
            a = float(input_func("Please reinput a: "))
            b = float(input_func("Please reinput b: "))
            c = float(input_func("Please reinput c: "))
                        
            if check_triangle(a, b, c):                     #Q3_4
                p, s = perimeter_area_triangle(a, b, c)
                print(f"Perimeter of the triangle with sides a, b, c: {p}")
                print(f"Area of the triangle with sides a, b, c: {s}")
            else:
                print("a, b, c are not side of a triangle") #Q3_5

            break
        
        except ValueError:
            print("Please input valid real numbers")
        except Exception as e:
            print(f"Error :{e}")

if __name__ == "__main__":
    main()