from random import randint as rd

def roll_dice():
    while True:
        dice = rd(1, 6)
        if dice == 6:
            break
    return dice

if __name__ == "__main__":
    result = roll_dice()
    print(result)