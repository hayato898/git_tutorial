from random import randint as rd

import random

def roll_dice(n):
    prev = None
    count = 0

    while True:
        dice = random.randint(1, 6)

        if dice == prev:
            count += 1
        else:
            prev = dice
            count = 1  # 新しい目が出たのでカウントリセット

        if count == n:
            return dice


if __name__ == "__main__":
    result = roll_dice(3)
    print(result)