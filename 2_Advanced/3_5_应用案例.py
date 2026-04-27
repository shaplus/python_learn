from functools import reduce
'''***************1. 数据处理***************'''
# 示例：处理用户数据
print('示例1：处理用户数据')
# 原始用户数据
users = [
    {"name": "Alice", "age": 25, "score": 85},
    {"name": "Bob", "age": 30, "score": 75},
    {"name": "Charlie", "age": 20, "score": 90},
    {"name": "David", "age": 35, "score": 65},
    {"name": "Eve", "age": 28, "score": 80}
]

# 1. 提取所有用户的姓名
names = list(map(lambda user: user["name"], users))
print("所有用户姓名：", names)  # 输出：['Alice', 'Bob', 'Charlie', 'David', 'Eve']

# 2. 过滤出年龄大于25的用户
older_than_25 = list(map(lambda user: user["name"]+ str(user["age"]), filter(lambda user: user["age"] > 25, users)))
print("年龄大于25的用户：", older_than_25) 


# 3. 计算所有用户的平均分数
total_score = reduce(lambda x, y: x + y, map(lambda user: user["score"], users))
average_score = total_score / len(users)
print("平均分数：", average_score)  # 输出：80.0

'''***************2. 字符串处理***************'''
# 示例：处理字符串列表
print('示例2：处理字符串列表')
strings = ["  hello  ", "WORLD", "python", "  programming  ", "LANGUAGE"]

# 1. 去除首尾空格并转换为小写
processed = list(map(lambda s: s.strip().lower(), strings))
print("处理后的字符串：", processed)  # 输出：['hello', 'world', 'python', 'programming', 'language']

# 2. 过滤出长度大于5的字符串
long_strings = list(filter(lambda s: len(s) > 5, processed))
print("长度大于5的字符串：", long_strings)  # 输出：['python', 'programming', 'language']

'''***************3. 数学运算***************'''
# 示例：计算阶乘
print('示例3：计算阶乘')

def factorial(n):
    if n <= 1:
        return 1
    return reduce(lambda x, y: x * y, range(1, n+1))

print(factorial(5))  # 输出：120
print(factorial(10))  # 输出：3628800

