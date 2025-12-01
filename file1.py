#filename: file.py
from random import randint as rd

# 関数
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

# 実行
if __name__ == "__main__":
    result = roll_dice(5)
    print(result)
