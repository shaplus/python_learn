'''
函数是一段可重用的代码块，用于执行特定的任务。在Python中，使用def关键字来定义函数。

目录:
1. 函数的定义与调用
2. 函数的参数类型
2.1 位置参数
2.2 默认参数
2.3 可变参数
2.4 关键字参数1
2.5 关键字参数2
2.6 混合参数
3. 函数的返回值
3.1 返回单个值
3.2 返回多个值
3.3 返回字典
3.4 不返回值
4. 函数的作用域
4.1 局部变量
4.2 全局变量
4.3 非局部变量
5. 匿名函数
5.1 定义一个简单的lambda函数
5.2 与内置函数结合使用
5.3 用于排序
'''

# 1. 函数的定义与调用
'''
基本语法:
def 函数名(参数列表):
    """文档字符串"""
    # 函数体
    return 返回值
'''

def greet(name):
    """问候函数"""
    return f"Hello, {name}!"
#调用函数
print("调用函数:")
print(greet("张三"))  # 输出: Hello, 张三!

# 2. 函数的参数类型
# 位置参数
#最基本的参数类型，按照位置顺序传递。
def add(a, b):
    """添加两个数"""
    return a + b

result = add(3, 5)
print("位置参数:", result)  # 输出: 8

# 默认参数
#默认参数是指在函数定义时，为参数指定默认值的参数。
#默认参数必须放在参数列表的最后面。
def add(a, b=2):
    """添加两个数"""
    return a + b

result = add(3)
print("默认参数:", result)  # 输出: 5
result = add(3, 4)
print("默认参数:", result)  # 输出: 7

# 可变参数
#可变参数是指在函数定义时，可以传递任意数量的参数的参数。
print("可变参数:")
def add(*args):
    """添加任意数量的数，返回它们的和。"""
    print(args)
    return sum(args)

result = add(1, 2, 3, 4, 5)
print(result)  # 输出: 15

# 关键字参数1
print("关键字参数1:")
def add(a, b):
    """添加两个数"""
    print(a, b)
    return a ** b

result1 = add(b=3, a=2)
print(result1)  # 输出: 8
result2 = add(b=2, a=3)
print(result2)  # 输出: 9

# 关键字参数2
#允许传递任意数量的关键字参数，使用**前缀。
print("关键字参数2:")
def print_kwargs(**kwargs):
    """打印任意数量的关键字参数。"""
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(a=3, b=5, c=2)

# 混合参数
print("混合参数:")
def mix_params(a, b=1, *args, **kwargs):
    """打印所有参数"""
    print(f'a={a}, b={b}, args={args}, kwargs={kwargs}')

mix_params(1, 2, 3, 4, 5, name="张三", age=18)
mix_params(1, name="李四", age=19)
mix_params(1)

# 3. 函数的返回值
# 返回单个值
print("返回单个值:")
def add(a, b):
    """添加两个数"""
    return a + b

result = add(3, 5)
print(result)  # 输出: 8

# 返回多个值
print("返回多个值:")
def add_sub(a, b):
    """添加和减去两个数"""
    return a + b, a - b

print(add_sub(3, 5))
result1, result2 = add_sub(3, 5)
print(result1)  # 输出: 8
print(result2)  # 输出: -2

# 返回字典
print("返回字典:")
def get_info(name, age, grade):
    """返回学生信息字典"""
    return {"name": name, "age": age, "grade": grade}

info = get_info("张三", 18, "A")
print(info)  # 输出: {'name': '张三', 'age': 18, 'grade': 'A'}

# 不返回值
print("不返回值:")
def print_info(name, age, grade):
    """打印学生信息"""
    print(f"姓名: {name}, 年龄: {age}, 等级: {grade}")

print_info("张三", 18, "A")

# 4. 函数的作用域
# 局部变量
print("局部变量:")
def my_function():
    x = 10  # 局部变量
    print(x)

my_function()  # 输出：10
# print(x)  # 报错：NameError: name 'x' is not defined

# 全局变量
print("全局变量:")
def print_global_x():
    print("函数内打印全局变量:", global_x)

def modify_global_x():
    global global_x
    global_x = 100  # 全局变量
    print("函数内修改全局变量:", global_x)

global_x = 1000  # 全局变量
print("全局变量:", global_x)
print_global_x()  # 输出：1000
modify_global_x()  # 输出：100
print("全局变量:", global_x)  # 输出：100

# 非局部变量
#在嵌套函数中，使用nonlocal关键字访问外部函数的变量。
print("非局部变量:")
def outer_function():
    x = 10
    print(f"Outer: {x}")
    
    def inner_function():
        nonlocal x  # 声明要修改外部函数的变量
        x = 20
        print(f"Inner: {x}")
    
    inner_function()
    print(f"Outer: {x}")

outer_function()
# 输出：
# Inner: 20
# Outer: 20

# 5. 匿名函数
#匿名函数是指没有名称的函数，通常用于临时任务。
#匿名函数的定义语法为：lambda参数列表: 表达式
# 定义一个简单的lambda函数
print("定义一个简单的lambda函数:")
lambda_add = lambda x, y: x + y     # noqa
print("lambda函数:", lambda_add(3, 5))  # 输出：8

# 与内置函数结合使用
#map()函数可以将一个函数应用到一个可迭代对象的每个元素上。
#filter()函数可以过滤出满足条件的元素。
#reduce()函数可以对序列中的元素进行累计操作，返回一个值。
print("与内置函数结合使用:")
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # 输出：[1, 4, 9, 16, 25]

# 用于排序
print("用于排序:")
students = [("Alice", 25), ("Bob", 20), ("Charlie", 22)]
print("排序前:", students)
students.sort(key=lambda student: student[1])  # 按年龄排序
print("排序后:", students)  # 输出：[('Bob', 20), ('Charlie', 22), ('Alice', 25)]

