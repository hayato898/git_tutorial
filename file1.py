from random import randint as rd

def roll_dice():
    while True:
        dice_1 = rd(1, 6)
        dice_2 = rd(1, 6)
        if dice_1 == dice_2:
            break
    return dice_1

if __name__ == "__main__":
    result = roll_dice()
    print(result)