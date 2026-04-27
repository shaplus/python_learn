'''
打印和输入
'''

# 打印
# 1. 使用print()函数打印文本和变量
print('打印文本和变量:')
print('Hello, World!')  # 输出: Hello, World!

# 2. 打印多个值，使用逗号分隔
print
name = 'Alice'
age = 25
print('姓名:', name, '年龄:', age)  # 输出: 姓名: Alice 年龄: 25

# 3. 使用格式化字符串打印变量
print('使用格式化字符串打印变量:')
print(f'姓名: {name}, 年龄: {age}')  # 输出: 姓名: Alice, 年龄: 25

# 4. 打印时指定分隔符和结束符
print('打印时指定分隔符和结束符:')
print('姓名:', name, '年龄:', age, sep=',')  # 输出: 姓名:Alice,年龄:25
print('姓名:', name, '年龄:', age, sep=',', end='.')  # 输出: 姓名:Alice,年龄:25.

# 5.打印结束后不换行
print('打印结束后不换行:')
print('姓名:', name, '年龄:', age, sep=',', end='')  # 输出: 姓名:Alice,年龄:25
print('这是同一行的文本')  # 输出: 这是同一行的文本

# 输入
# 1. 使用input()函数获取用户输入
print('获取用户输入:')
name = input('请输入您的姓名:')
print(f'您的姓名是: {name}')  # 输出: 您的姓名是: Alice
age = int(input('请输入您的年龄:'))
print(f'您的年龄是: {age}')  # 输出: 您的年龄是: 25

# 2. 输入转换
print('输入转换:')
height = float(input('请输入您的身高(米):'))
print(f'您的身高是: {height} 米')  # 输出: 您的身高是: 1.65 米
weight = float(input('请输入您的体重(千克):'))
print(f'您的体重是: {weight} 千克')  # 输出: 您的体重是: 60.0 千克

# 3. 输入提示信息
print('输入提示信息:')
name = input('请输入您的姓名:')
print(f'您的姓名是: {name}')  # 输出: 您的姓名是: Alice
age = int(input('请输入您的年龄:'))
print(f'您的年龄是: {age}')  # 输出: 您的年龄是: 25

# 4. 输入时去除多余的空格
print('输入时去除多余的空格:')
name = input('请输入您的姓名: ').strip()  # 去除输入的前后空格
print(f'您的姓名是: {name}')  # 输出: 您的姓名是: Alice
age = int(input('请输入您的年龄: ').strip())  # 去除输入的前后空格
print(f'您的年龄是: {age}')  # 输出: 您的年龄是: 25

# 5. 输入时指定默认值
print('输入时指定默认值:')
name = input('请输入您的姓名(默认: 未知): ') or '未知'
print(f'您的姓名是: {name}')  # 输出: 您的姓名是: 未知
age = int(input('请输入您的年龄(默认: 0): ') or 0)
print(f'您的年龄是: {age}')  # 输出: 您的年龄是: 0

# 6. 防止输入错误导致程序崩溃
print('防止输入错误导致程序崩溃:')
try:
    age = int(input('请输入您的年龄: '))
    print(f'您的年龄是: {age}')
except ValueError:
    print('输入的年龄格式不正确!')