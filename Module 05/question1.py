import random

num_dice = int(input("How many dice to roll? "))
total = 0

for numbers in range(num_dice):
    value = random.randint(1, 6)
    total += value

print(f"Sum of the dice is: {total}")