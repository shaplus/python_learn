'''猜数字游戏'''

import random

# 生成一个随机数，范围在1-100之间
secret_number = random.randint(1, 100)

# 提示用户输入猜测的数字
guess = None
while guess != secret_number:
    guess = int(input("请输入你猜的数字（1-100）："))
    if guess < secret_number:
        print("太小了！")
    elif guess > secret_number:
        print("太大了！")
    else:
        print("恭喜你，猜对了！")
        break