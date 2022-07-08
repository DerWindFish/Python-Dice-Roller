import random

def parse_input(input_string):
    # Return 'input_string as the die selection
    if input_string.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(input_string)
    else:
        print("Please enter a number from 1 to 6.")
        raise SystemExit(1)

def roll_dice(num_dice):
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1, 20)
        roll_results.append(roll)
    return roll_results

# Get user input for which die they would like to roll
num_dice_input = input("How many d20 do you want to roll? [1-6] ")

num_dice = parse_input(num_dice_input)

# Roll the d20
roll_results = roll_dice(num_dice)
print(roll_results)

