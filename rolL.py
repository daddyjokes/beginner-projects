import random
import re



numbers = []
commands = []

def check():
    global numbers
    global commands

    if len(numbers) == 2:
        numbers.append(numbers[0])
        if numbers[1] == "0":
            return False
    if len(numbers) == 3:
        if len(commands) == 1:
            commands.append("k")
        if len(commands) == 2:
            if commands[0] == "d":
                if commands[1] == "" or commands[1] == "k" or commands[1] == "kl":
                    return True
    return False

def roll_dice(times, sides):
    times = int(times)
    sides = int(sides)

    rolls = []
    for i in range(times):
        roll = random.randint(1, sides)
        rolls.append(roll)
    return rolls

def keeps(rolls, keep, keep_number):
    keep_number = int(keep_number)

    keeps = []
    temp = rolls.copy()
    if keep == "k":
        for i in range(keep_number):
            keeps.append(max(temp))
            temp.remove(max(temp))
    elif keep == "kl":
        for i in range(keep_number):
            keeps.append(min(temp))
            temp.remove(min(temp))
    return keeps

def add_up(list):
    total = 0
    for i in range(len(list)):
        total += list[i]
    return total

def arth(totals, all_commands):
    total = 0
    for i in range(len(totals)):
        if (i == 0):
            total += totals[i]
        else:
            if all_commands[i-1] == "+":
                total += totals[i]
            else:
                total -= totals[i]
    return total

def main():
    global numbers
    global commands

    print("rolL dice roller by Devin Zhang. 5/10/20\nFormat: 1d20+2, 13d12+8d6; 3d20k2 (keep highest two), 3d20kl2 (keep lowest two)\n")

    while True:
        requests = input("> ").lower()

        all_commands = list(filter(None, re.split("[^+-]", requests)))

        all_requests = []
        requests_split = requests.split("+")
        for i in range(len(requests_split)):
            new_split = []
            if "-" in requests_split[i]:
                new_split = requests_split[i].split("-")
                for i in range(len(new_split)):
                    all_requests.append(new_split[i])
            else:
                all_requests.append(requests_split[i])

        alls = []
        totals = []
        for i in range(len(all_requests)):
            total = 0

            userInput = all_requests[i]

            if userInput.isdigit():
                totals.append(int(userInput))
            else:
                numbers = list(filter(None, re.split("[^0-9]", userInput)))
                commands = list(filter(None, re.split("[0-9]", userInput)))

                if not check():
                    continue

                roll = roll_dice(numbers[0], numbers[1])

                rolls = keeps(roll, commands[1], numbers[2])

                total = add_up(rolls)

                alls.append(userInput + ": " + str(roll) + " = " + str(total))
                totals.append(total)

        for i in range(len(alls)):
            print(alls[i])
        print("\nTotal: " + str(arth(totals, all_commands)))
main()