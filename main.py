"""
Dice Rolling Simulator
by Justin Berry
Python v3.9
"""
import random


class Die:
    """
    Creates new die with methods:
    roll
    """
    def __init__(self, sides: int):
        self.sides = sides

    def roll(self) -> int:
        """
        Rolls die, returns random number
        based on probability
        """
        result = random.randint(1, self.sides)
        return result


def main():
    """
    Runs simulator
    """
    choosing_sides = True

    print("----------\n"
          "Type 'stop' to end program at any time"
          )

    while choosing_sides:
        print("----------")
        inp = input("How many sides should the die have? (4, 6, 8, 12, etc):\n")

        if inp.isalpha():
            if inp == "stop":
                raise SystemExit()
        if inp.isdigit():
            inp = int(inp)
            if inp > 0:
                if inp < 1000:
                    die = Die(inp)
                    print("You rolled a:", die.roll())
                else:
                    print("Die must have less than 1000 sides.")
            else:
                print("Die must have more than 0 sides.")
        else:
            print("Input must be numeric (including '-').")


# Run game on compile:
if __name__ == "__main__":
    main()
