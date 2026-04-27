
'''集合'''
# 集合是无序的、不可重复的数据集合
# 集合使用{}定义，元素之间用逗号分隔

# 1.集合的基本操作
#1.1 集合的创建
# 创建一个空集合
my_set = set() # 注意：使用{}创建的是一个空字典，而不是空集合
print(my_set)  # 输出: set()

# 1.2 创建一个包含元素的集合
my_set = {1, 2, 3, 4, 5}
print(my_set)  # 输出: {1, 2, 3, 4, 5}

# 1.3 集合的添加
print('集合的添加:')
my_set = {1, 2, 3, 4, 5}
print(my_set)  # 输出: {1, 2, 3, 4, 5}
# 添加单个元素
my_set.add(6)
print('add()方法添加单个元素:')
print(my_set)  # 输出: {1, 2, 3, 4, 5, 6}
# 添加多个元素
my_set.update([7, 8, 9])
print('update()方法添加多个元素:')
print(my_set)  # 输出: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# 1.4 集合的删除
print('集合的删除:')
print('remove()方法删除元素:')
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(my_set)  # 输出: {1, 2, 3, 4, 5, 6, 7, 8, 9}
# 删除元素
my_set.remove(5)
print(my_set)  # 输出: {1, 2, 3, 4, 6, 7, 8, 9}
# 删除不存在的元素会引发KeyError异常
# my_set.remove(10)  # KeyError: 10
# 删除不存在的元素不会引发异常
print('discard()方法删除不存在的元素不会引发异常:')
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(my_set)  # 输出: {1, 2, 3, 4, 5, 6, 7, 8, 9}
my_set.discard(10)
print(my_set)  # 输出: {1, 2, 3, 4, 6, 7, 8, 9}
my_set.discard(6)
print(my_set)  # 输出: {1, 2, 3, 4, 7, 8, 9}
print('pop()方法随机删除一个元素:')
deleted_element = my_set.pop()  # 随机删除一个元素
print(my_set)  # 输出: {2, 3, 4, 7, 8, 9}
print(f"删除的元素: {deleted_element}")
# 清空集合
print('clear()方法清空集合:')
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(my_set)  # 输出: {2, 3, 4, 7, 8, 9}
my_set.clear()
print(my_set)  # 输出: set()

# 2. 集合的数学运算
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a)
print(b)

# 2.1 并集
print('集合的并集:')
c = a | b  # 或者使用 a.union(b)
print(c)  # 输出: {1, 2, 3, 4, 5, 6, 7, 8}
c = a.union(b)
print(c)  # 输出: {1, 2, 3, 4, 5, 6, 7, 8}

# 2.2 交集
print('集合的交集:')
c = a & b  # 或者使用 a.intersection(b)
print(c)  # 输出: {4, 5}
c = a.intersection(b)
print(c)  # 输出: {4, 5}

# 2.3 差集
print('集合的差集:')
c = a - b  # 或者使用 a.difference(b)
print(c)  # 输出: {1, 2, 3}
c = a.difference(b)
print(c)  # 输出: {1, 2, 3}

# 2.4 对称差集（只在其中一个集合中出现的元素）
print('集合的对称差集:')
c = a ^ b  # 或者使用 a.symmetric_difference(b)
print(c)  # 输出: {1, 2, 3, 6, 7, 8}
c = a.symmetric_difference(b)
print(c)  # 输出: {1, 2, 3, 6, 7, 8}