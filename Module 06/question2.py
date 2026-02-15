import random

def dice_roll(sides):
    return random.randint(1,sides)

dice_value = 0
num_sides = int(input("Enter the sides of dice: "))
while dice_value != num_sides:
    dice_value = dice_roll(num_sides)
    print(dice_value)