'''
装饰器（Decorator）
基本概念
装饰器是一种特殊的函数，它可以修改其他函数或类的行为。
装饰器使用@装饰器名称的语法应用于函数或类。
'''

'''*************1. 简单装饰器*****************'''
print('简单装饰器')
print('*' * 20)
print('示例1')
def simple_decorator(func):
    def wrapper():
        print("开始执行")
        func()
        print("结束执行")
    return wrapper

# 使用简单装饰器
#本质是：simple_function = simple_decorator(simple_function)
@simple_decorator
def simple_function():
    print("这是一个简单的函数")

# 调用装饰器后的函数
simple_function()  # 输出：开始执行，然后输出这是一个简单的函数，然后输出结束执行
print(simple_function.__name__)     # 输出：wrapper
print('*' * 20)
'''******************************'''
# 记录函数执行时间的装饰器
print('示例2')
import time     #noqa

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} 执行时间：{end_time - start_time:.4f}秒")
        return result
    return wrapper

# 使用装饰器
#本质是：slow_function = timer(slow_function)
@timer
def slow_function():
    time.sleep(1)
    print("函数执行完成")

slow_function()
print(slow_function.__name__)     # 输出：wrapper
# 输出：函数执行完成，然后输出执行时间
print('*' * 20)
'''*******2. 保留原函数信息的装饰器*****************'''
print('保留原函数信息的装饰器:')
from functools import wraps  #noqa

def wrapper(func):
    @wraps(func)       # 关键
    def inner(*args, **kwargs):
        return func(*args, **kwargs)
    return inner

@wrapper
def simple_function():
    print("这是一个简单的函数")

simple_function()
print(simple_function.__name__)     # 输出：simple_function
print('*' * 20)
'''*************3. 带参数的装饰器*****************'''
print('带参数的装饰器:')
# 示例：创建一个带参数的装饰器，用于限制函数的调用次数
def limit_calls(max_calls):
    def decorator(func):
        calls = 0
        
        def wrapper(*args, **kwargs):
            nonlocal calls
            if calls >= max_calls:
                raise ValueError(f"函数 {func.__name__} 已达到最大调用次数 {max_calls}")
            calls += 1
            return func(*args, **kwargs)
        
        return wrapper
    return decorator

# 使用带参数的装饰器
#本质是：greet = limit_calls(3)(greet)
@limit_calls(3)
def greet(name):
    print(f"Hello, {name}!")

try:
    greet("Alice")  # 正常执行
    greet("Bob")    # 正常执行
    greet("Charlie")  # 正常执行
    greet("David")  # 抛出ValueError异常
except ValueError as e:
    print(f"捕获到异常: {e}")
print('*' * 20)

'''*************4. 装饰器局部变量范围*****************'''
print('装饰器局部变量范围:')
def create_shared_counter():
    count_all = 0  # 这里只创建一次

    # 这才是真正的装饰器
    def counter(func):
        count_private = 0  # 每个函数实例都有自己的计数器
        def wrapper(*args, **kwargs):
            nonlocal count_all
            nonlocal count_private
            count_all += 1
            count_private += 1
            print(f"总调用次数：{count_all}")
            print(f"{func.__name__}调用次数：{count_private}")
            return func(*args, **kwargs)
        return wrapper

    return counter


# 先创建一个共享计数器
shared_counter = create_shared_counter()

# 使用共享计数器
#本质是：f1 = shared_counter(f1)
#本质是：f2 = shared_counter(f2)
@shared_counter
def f1(): pass

@shared_counter
def f2(): pass

f1()  # 1
f2()  # 2
f1()  # 3
print('*' * 20)

'''**************5. 类装饰器****************'''
#示例：创建一个类装饰器，用于记录方法的调用次数
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.calls = 0
    
    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f"函数 {self.func.__name__} 已调用 {self.calls} 次")
        return self.func(*args, **kwargs)

# 使用类装饰器
#本质是：add = CountCalls(add)，add是一个类实例
@CountCalls
def add(a, b):
    return a + b

print(add(1, 2))  # 输出调用次数，然后输出3
print(add(3, 4))  # 输出调用次数，然后输出7
print('*' * 20)

'''***************6. 多个装饰器的使用***************'''
#多个装饰器可以同时应用于一个函数，它们的执行顺序是从下到上。
#示例：
def decorator1(func):
    def wrapper(*args, **kwargs):
        print("装饰器1开始")
        result = func(*args, **kwargs)
        print("装饰器1结束")
        return result
    return wrapper

def decorator2(func):
    def wrapper(*args, **kwargs):
        print("装饰器2开始")
        result = func(*args, **kwargs)
        print("装饰器2结束")
        return result
    return wrapper

# 多个装饰器
#本质是：hello = decorator1(decorator2(hello))
@decorator1
@decorator2
def hello():
    print("Hello!")

hello()
# 输出顺序：
# 装饰器1开始
# 装饰器2开始
# Hello!
# 装饰器2结束
# 装饰器1结束
print('*' * 20)

