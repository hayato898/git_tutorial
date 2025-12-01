from random import randint as rd

def roll_dice(n):
    prev = None
    count = 0

    while True:
        dice = rd.randint(1, 6)

        if dice == prev:
            count += 1
        else:
            prev = dice
            count = 1  

        if count == n:
            return dice

if __name__ == "__main__":
    result = roll_dice(4)
    print(result)