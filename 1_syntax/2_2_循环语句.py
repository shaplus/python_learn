'''
循环语句（for循环和while循环）用于重复执行代码块，直到满足某个条件为止。

for循环的基本语法如下：

for 变量 in 可迭代对象:
    语句块

while循环的基本语法如下：

while 条件:
    语句块
在for循环中，变量会依次取可迭代对象中的每个元素，并执行语句块。在while循环中，只要条件为真，就会一直执行语句块。
'''

# for循环示例
# 遍历列表中的元素
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
# 输出：apple
# 输出：banana
# 输出：cherry 

# 遍历字符串中的字符
for char in "hello":
    print(char)
# 输出：h
# 输出：e
# 输出：l
# 输出：l
# 输出：o

# 使用range函数生成数字序列
for i in range(5):
    print(i)
# 输出：0
# 输出：1
# 输出：2
# 输出：3
# 输出：4

# while循环示例
# 计算1到10的和
sum = 0
i = 1
while i <= 10:
    sum += i
    i += 1
print(sum)
# 输出：55

# 循环控制语句
# break语句
for i in range(5):
    if i == 3:
        break
    print(i)
# 输出：0
# 输出：1
# 输出：2

# continue语句
for i in range(5):
    if i == 3:
        continue
    print(i)
# 输出：0
# 输出：1
# 输出：2
# 输出：4

# pass语句
for i in range(5):
    if i == 3:
        pass  # 占位符，不执行任何操作
    print(i)

# 循环占位变量
for _ in range(5):
    print('循环占位变量')
