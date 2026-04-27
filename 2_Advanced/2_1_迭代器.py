'''
基本概念:
迭代器是一个实现了迭代器协议的对象，它可以用来遍历容器中的元素。迭代器协议要求对象实现两个方法：
- __iter__()：返回迭代器对象本身
- __next__()：返回容器中的下一个元素，如果没有更多元素则抛出StopIteration异常

可迭代对象（Iterable）:
可迭代对象是指可以被iter()函数调用并返回一个迭代器的对象，例如列表、元组、字符串、字典等。

- 列表每次遍历都创建一个新的迭代器，而元组和字符串的迭代器是可重复使用的。
- 字典的迭代器遍历键，而不是值。
- 集合的迭代器遍历集合中的元素。
- 集合的迭代器是无序的，每次遍历的顺序可能不同。

迭代器本质是一个对象，它实现了迭代器协议，可以用来遍历容器中的元素。
通过for等循环先调用iter()函数获取迭代器，
然后自动调用迭代器的__next__()方法，直到抛出StopIteration异常为止。
所以自己实现一个迭代器，需要实现__iter__()和__next__()方法。

'''

'''*************1. 可迭代对象（Iterable）***************'''
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "hello"
my_dict = {"a": 1, "b": 2}

# 使用iter()函数获取迭代器
list_iterator = iter(my_list)
tuple_iterator = iter(my_tuple)
str_iterator = iter(my_str)
dict_iterator = iter(my_dict)  # 字典的迭代器遍历键

'''*************2. 使用迭代器***************'''
# 手动使用迭代器：
print('手动使用迭代器：')
# 创建迭代器
numbers = [1, 2, 3, 4, 5]
iterator = numbers.__iter__()

# 手动调用next()获取元素
print(iterator)
print('手动调用next()获取元素：')
print(iterator.__next__())  # 输出：1
print(iterator.__next__())  # 输出：2
print(iterator.__next__())  # 输出：3
print(iterator.__next__())  # 输出：4
print(iterator.__next__())  # 输出：5
# print(iterator.__next__())  # 抛出StopIteration异常

# 使用for循环遍历：
print('使用for循环遍历：')
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
# 输出：1 2 3 4 5

'''*************3. 自定义迭代器***************'''
# 示例：创建一个自定义的迭代器，生成斐波那契数列
class FibonacciIterator:
    def __init__(self, max_num):
        self.max_num = max_num
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.a > self.max_num:
            raise StopIteration
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        return value

# 使用自定义迭代器
print('使用自定义迭代器：')
fib = FibonacciIterator(50)
print(fib)
print(fib.__iter__())
for num in fib:
    print(num)
# 输出：0 1 1 2 3 5 8 13 21 34

'''*************4. __iter__()返回生成器***************'''
# 示例：创建一个生成器函数，生成斐波那契数列
# 生成器函数使用def定义，包含yield语句。
# 当调用生成器函数时，它返回一个生成器对象，而不是执行函数体。
# 生成器的语法如下：
# def generator_name():
#     for value in values:
#         yield value
# 当def __iter__(self)存在field时，自动返回生成器对象
print('使用生成器函数：')
class FibonacciIterator:
    def __init__(self, max_num):
        self.max_num = max_num
        self.a, self.b = 0, 1
    
    def __iter__(self):
        def generator():
            while True:
                if self.a > self.max_num:
                    break
                value = self.a
                self.a, self.b = self.b, self.a + self.b
                yield value
        return generator()

print('使用生成器函数遍历：')
numbers = FibonacciIterator(5)
for num in numbers:
    print(num)
# 输出：0 1 1 2 3 5

print('手动调用next()获取元素：')
numbers = FibonacciIterator(5).__iter__()
print(numbers.__next__())
print(numbers.__next__())
print(numbers.__next__())
print(numbers.__next__())
print(numbers.__next__())
print(numbers.__next__())
# print(numbers.__next__()) # 抛出StopIteration异常
# 输出：0 1 1 2 3 5
