import random
import re


def roll_dice(dice):
    # Dice request format = INTEGER+d+INTEGER (4d6, 1d10, 99d99)
    rolled_total = 0
    dice_split = dice.split("d")
    times = int(dice_split[0])
    sides = int(dice_split[1])

    for i in range(times):
        roll = random.randint(1, sides)
        rolled_total += roll
        if i < times-1:
            print(roll, end = "+")
        else:
            print(roll)
    return rolled_total


def main():
    print("Dice Roller / Calculator v1\nInput mathematical operations or roll dice (e.g. 4d6+2)\n")
    while True:
        try:
            equation = ""

            # Format input to remove all characters besides numbers, operators, and "d" for processing
            raw_input = input("> ").lower()
            inputs = re.sub("[^d0123456789+\-/*()]", "", raw_input)

            # Split equation into items but keep operators
            operation = re.split("([+\-*/])",inputs)

            # Convert dice requests to integers
            for i in range(len(operation)):
                # Detect if input is raw number or dice request
                detect = re.search("d", operation[i])
                if detect is None:
                    None
                else:
                    operation[i] = roll_dice(operation[i])
                equation += str(operation[i])

            total = eval(equation)

            print("\nTotal: " + str(total) + "\n")
        except:
            print("Invalid Input.")
main()