import copy
'''列表'''
# 列表是有序的集合，可以随时添加和删除其中的元素
'''
目录
1. 列表的创建
1.1 创建空列表
1.2 创建包含元素的列表
1.3 用列表推导式创建列表
2. 列表的基本操作
2.1 访问列表元素
2.2 切片操作
2.3 修改列表元素
2.4 添加元素
2.5 删除元素
2.6 清空列表
3. 列表的常用方法
3.1 统计元素出现的次数
3.2 对列表进行排序
3.3 反转列表
3.4 列表的浅拷贝
3.5 列表的深拷贝
3.6 列表的长度
3.7 列表的成员资格测试
3.8 列表的索引操作
3.9 列表的遍历
3.10 带索引的遍历


列表的常用方法
方法	    描述
append()	在列表末尾添加元素
insert()	在指定位置插入元素
remove()	删除第一个匹配的元素
pop()	    移除并返回指定位置的元素（默认为最后一个）
clear()	    清空列表
index()	    返回第一个匹配元素的索引
count()	    统计元素出现的次数
sort()	    对列表进行排序
reverse()	反转列表
copy()	    返回列表的浅拷贝
'''

# 1. 列表的创建
# 创建空列表

empty_list = []
# 或者
empty_list = list()

# 创建包含元素的列表
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "apple", True, 3.14]  # 列表可以包含不同类型的元素
print('numbers:', numbers)
print('fruits:', fruits)
print('mixed:', mixed)

# 用列表推导式创建列表
print('列表推导式:')
squares = [x**2 for x in range(1, 6)]
print(squares)  # 输出: [1, 4, 9, 16, 25]

# 2.列表的基本操作
# 访问列表元素
print('访问列表元素:')
print(numbers[0])  # 输出: 1
print(fruits[1])   # 输出: banana
print(mixed[3])    # 输出: 3.14

#切片操作
print('切片操作:')
numbers = [1, 2, 3, 4, 5]
print(numbers[1:4])  # 输出: [2, 3, 4]

# 修改列表元素
print('修改列表元素:')
numbers = [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers)  # 输出: [10, 2, 3, 4, 5, 6]

# 添加元素
print('添加元素:')
numbers = [1, 2, 3, 4, 5]
numbers.append(6)  # 在列表末尾添加元素
print(numbers)  # 输出: [1, 2, 3, 4, 5, 6]

numbers = [1, 2, 3, 4, 5]
numbers.insert(0, 0)  # 在索引0的位置插入元素0
print(numbers)  # 输出: [0, 1, 2, 3, 4, 5, 6]

# 删除元素
print('删除元素:')
numbers = [1, 2, 3, 4, 5]
del numbers[0]  # 删除索引为0的元素
print(numbers)  # 输出: [2, 3, 4, 5]

numbers = [1, 2, 3, 4, 5]
popped_number = numbers.pop(0)  # 删除并返回索引为0的元素
print(popped_number)  # 输出: 1
print(numbers)  # 输出: [2, 3, 4, 5]

numbers = [1, 2, 3, 4, 5]
poped_number = numbers.pop()  # 删除并返回最后一个元素
print(poped_number)  # 输出: 5
print(numbers)  # 输出: [1, 2, 3, 4]

# 清空列表
print('清空列表:')
numbers = [1, 2, 3, 4, 5]
numbers.clear()
print(numbers)  # 输出: []

# 列表的其他方法
# 统计元素出现的次数
print('统计元素出现的次数:')
numbers = [1, 2, 3, 4, 5, 2, 3, 4]
print(numbers.count(2))  # 输出: 2

# 对列表进行排序
print('对列表进行排序:')
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
numbers.sort()
print(numbers)  # 输出: [1, 1, 2, 3, 3, 5, 5, 5, 6, 9]
numbers.sort(reverse=True)  # 降序排序
print(numbers)  # 输出: [9, 6, 5, 5, 5, 3, 3, 2, 1, 1]

# 反转列表
print('反转列表:')
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # 输出: [5, 4, 3, 2, 1]

# 列表的浅拷贝
print('列表的浅拷贝:')
numbers = [1, 2, 3, 4, 5]
copied_numbers = numbers.copy()
print(copied_numbers)  # 输出: [1, 2, 3, 4, 5]
# 注意：浅拷贝不会复制嵌套的可变对象，如列表、字典等。
numbers = [1, 2, 3, [4, 5]]
copied_numbers = numbers.copy()
copied_numbers[3][0] = 100
print(numbers)  # 输出: [1, 2, 3, [100, 5]]
print(copied_numbers)  # 输出: [1, 2, 3, [100, 5]]
# 注意：嵌套的可变对象（如列表）不会被复制，而是引用原始对象。

# 列表的深拷贝
print('列表的深拷贝:')
numbers = [1, 2, 3, [4, 5]]
copied_numbers = copy.deepcopy(numbers)
copied_numbers[3][0] = 100
print(numbers)  # 输出: [1, 2, 3, [4, 5]]
print(copied_numbers)  # 输出: [1, 2, 3, [100, 5]]
# 注意：深拷贝会复制嵌套的可变对象，包括嵌套的列表、字典等。

# 列表的长度
print('列表的长度:')
numbers = [1, 2, 3, 4, 5]
print(len(numbers))  # 输出: 5

# 列表的成员资格测试
print('列表的成员资格测试:')
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)  # 输出: True
print(6 in numbers)  # 输出: False

# 列表的索引操作
print('列表的索引操作:')
numbers = [1, 2, 3, 4, 5]
print(numbers.index(3))  # 输出: 2
print(numbers.index(5, 3))  # 输出: 4, 从索引3开始查找5的索引

# 列表的遍历
print('列表的遍历:')
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)

# 带索引的遍历
print('带索引的遍历:')
numbers = [1, 2, 3, 4, 5]
numbers = enumerate(numbers)
print(numbers)
for i, n in numbers:
    print(f"索引: {i}, 值: {n}")