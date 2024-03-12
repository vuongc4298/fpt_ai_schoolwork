import random
class Main:

    #====================GuessNumber function====================
    def GuessNumber(self, number):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        lower = 0
        higher = int(number) + 1
        while True:
            guess = random.randint(lower, higher)
            c = input(f"Is  {guess} too high(h), too low(l), or correct(c): ")
            if c.lower() == "h":
                higher = guess - 1
                continue
            elif c.lower() == "l":
                lower = guess + 1
                continue
            elif c.lower() == "c":
                print(f"Welldone! The computer guessed your number {guess} correctly!")
                break
            else:
                print("Invalid input!")
                continue
        pass
        # end def

#==================DO NOT CHANGE THE CODE BELOW=====================
    def main(self):
        number = input("Enter a range for guessed number: ")
        print("OUTPUT")
        self.GuessNumber(number)
        print("FINISH")
main = Main()
main.main()

