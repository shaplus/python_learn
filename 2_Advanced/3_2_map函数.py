'''
基本概念:
map()函数用于对可迭代对象中的每个元素应用指定的函数，返回一个新的迭代器。

语法：map(函数, 可迭代对象, ...)
参数：
- 函数：要应用的函数。
- 可迭代对象：要应用函数的可迭代对象，如列表、元组、字符串等。
- ...：可选的更多可迭代对象，每个对象的元素会对应应用到函数的参数上。
返回值：
- 新的迭代器，包含应用函数后的结果。
- 注意：返回的是一个迭代器，需要使用 list() 等函数转换为列表。
- 注意：map() 函数不会修改原始可迭代对象，只是对每个元素应用函数。
- 注意：map() 函数可以同时对多个可迭代对象应用函数，每个对象的元素会对应应用到函数的参数上。
'''
'''***************1. 基本用法***************'''
# 示例1：对单个可迭代对象应用函数
print('示例1：对单个可迭代对象应用函数')
# 使用lambda函数
print('示例1：使用lambda函数')
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # 输出：[1, 4, 9, 16, 25]

# 使用普通函数
print('示例1：使用普通函数')
def double(x):
    return x * 2

doubled = map(double, numbers)
print(list(doubled))  # 输出：[2, 4, 6, 8, 10]

# 示例2：对多个可迭代对象应用函数
print('示例2：对多个可迭代对象应用函数')
# 对两个列表对应元素求和
print('示例2：对两个列表对应元素求和')
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
sums = map(lambda x, y: x + y, list1, list2)
print(list(sums))  # 输出：[7, 9, 11, 13, 15]

# 对三个列表对应元素求乘积
print('示例2：对三个列表对应元素求乘积')
list3 = [2, 2, 2, 2, 2]
products = map(lambda x, y, z: x * y * z, list1, list2, list3)
print(list(products))  # 输出：[12, 28, 48, 72, 100]

# 示例3：长度不一致：取最短
print('示例3：长度不一致：取最短')
a = [1, 2]
b = [10, 20, 30, 40]

res = map(lambda x,y:x+y, a, b)
print(list(res))  # 只取2组

# 示例4：关键特性：map 返回「迭代器」
print('示例4：关键特性：map 返回「迭代器」')
lst = [1,2,3]
it = map(lambda x:x*2, lst)

print(next(it))  # 2
print(next(it))  # 4
print(next(it))  # 6
# 迭代器遍历完后，再调用 next() 会报错
#next(it)  # 

# 迭代器遍历完就空了
print(list(it))  # []

'''***************2. 经典实用场景***************'''
# 场景 1：批量类型转换（最常用）
print('场景 1：批量类型转换（最常用）')
# 字符串列表 转 数字列表
str_nums = ["1", "2", "3", "4"]
int_nums = list(map(int, str_nums))
print(int_nums)  # [1, 2, 3, 4]

# 场景 2：输入快速处理（刷题 / 日常）
print('场景 2：输入快速处理（刷题 / 日常）')
# 输入：1 2 3 4
data = list(map(int, input().split()))
print(data)  # [1, 2, 3, 4]

# 场景 3：字符串批量操作
print('场景 3：字符串批量操作')
words = ["apple", "banana", "cat"]
upper_words = list(map(str.upper, words))
print(upper_words)
# ['APPLE', 'BANANA', 'CAT']
