from random import randint as rd

def roll_dice():
    return rd(1, 6)
print("You rolled a", roll_dice())