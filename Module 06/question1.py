import random

def dice_roll():
    return random.randint(1, 6)

dice_value = 0
while dice_value != 6:
    dice_value = dice_roll()
    print(dice_value)
