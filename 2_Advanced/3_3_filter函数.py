'''
基本概念:
filter()函数用于过滤可迭代对象中的元素，返回符合条件的元素组成的迭代器。

语法：filter(函数, 可迭代对象)
参数：
可迭代对象：列表、元组、字符串等
函数：返回 True 或 False 的函数
返回：迭代器
'''

'''**************1. 基本用法***************'''
# 示例1：过滤偶数
print('示例1：过滤偶数')
# 使用lambda函数
print('示例1：使用lambda函数')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # 输出：[2, 4, 6, 8, 10]

# 使用普通函数
print('示例1：使用普通函数')
def is_odd(x):
    return x % 2 != 0

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))  # 输出：[1, 3, 5, 7, 9]

# 示例2：过滤非空字符串
print('示例2：过滤非空字符串')
strings = ["hello", "", "world", " ", "python", ""]
non_empty = filter(lambda s: s.strip(), strings)
print(list(non_empty))  # 输出：['hello', 'world', 'python']

'''**************2. 进阶***************'''
'''过滤字典 / 复杂数据'''
print('过滤字典 / 复杂数据')
users = [
    {"name":"A", "age":16},
    {"name":"B", "age":22},
    {"name":"C", "age":19}
]

adult = list(filter(lambda u: u["age"] >= 18, users))
print(adult)  # 输出：[{'name': 'B', 'age': 22}]

'''filter VS 列表推导式'''
# filter() 函数可以更简洁地实现过滤操作，而列表推导式则需要使用 if 语句。
# filter
print('filter')
res = list(filter(lambda x: x%2==0, [1,2,3,4]))
print(res)  # 输出：[2, 4]

# 列表推导式（替代方案）
print('列表推导式（替代方案）')
res = [x for x in [1,2,3,4] if x%2==0]
print(res)  # 输出：[2, 4]

'''map & filter 链式组合（高级常用）'''
# 先过滤，再加工：
print('map & filter 链式组合（高级常用）:')
nums = [1,2,3,4,5,6]
# 1. filter：只留偶数
# 2. map：每个数平方
res = list(map(lambda x:x**2, filter(lambda x:x%2==0, nums)))
print(res)  # [4, 16, 36]
