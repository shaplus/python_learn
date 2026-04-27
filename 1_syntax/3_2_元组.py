import copy
'''元组'''
# 元组是不可变的序列类型，使用圆括号()定义
# 元组中的元素可以是任意类型，可以包含重复的元素

#目录
'''
1. 创建一个元组
1.1 创建空元组
1.2 创建一个包含元素的元组
2. 元组的基本操作
2.1 访问元组中的元素
2.2 元组的切片操作
2.3 元组的连接和重复
2.4 元组的成员资格测试操作
2.5 元组的长度操作
2.6 元组的不可变性操作
2.7 元组的索引操作
2.8 统计元素出现的次数操作
3. 元组的其他操作
3.1 元组的解包操作
3.2 元组的嵌套操作
3.3 元组的索引和切片
3.4 元组的内置函数
3.5 元组的浅拷贝和深拷贝
'''

# **************1. 创建一个元组*************
# 创建一个空元组
my_tuple = ()
# 或者
my_tuple = tuple()

# 创建一个包含元素的元组
print('创建一个包含元素的元组:')
single_tuple = (100,)  # 注意：单元素元组需要在元素后面加逗号，否则会被解释为普通的括号表达式
my_tuple = (1, 2, 3, 'hello', [4, 5])
print(single_tuple)  # 输出: (100,)
print(type(single_tuple))  # 输出: <class 'tuple'>
print(my_tuple)
print(type(my_tuple))  # 输出: <class 'tuple'>

# **************2. 元组的基本操作*************
# 访问元组中的元素
print('访问元组中的元素:')
my_tuple = (1, 2, 3, 'hello', [4, 5])
print(my_tuple[0])  # 输出: 1
print(my_tuple[-1])  # 输出: [4, 5]     # 负索引访问

# 元组的切片操作
print('元组的切片操作:')
my_tuple = (1, 2, 3, 'hello', [4, 5])
print(my_tuple[1:4])  # 输出: (2, 3, 'hello')
print(my_tuple[:3])  # 输出: (1, 2, 3)
print(my_tuple[3:5])  # 输出: ('hello', [4, 5])
print(my_tuple[::2])  # 输出: (1, 3, [4, 5])     # 步长为2

# 元组的连接和重复
print('元组的连接和重复:')
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
print(tuple1 + tuple2)  # 输出: (1, 2, 3, 'a', 'b', 'c')
print(tuple1 * 2)  # 输出: (1, 2, 3, 1, 2, 3)

# 元组的成员资格测试
print('元组的成员资格测试:')
my_tuple = (1, 2, 3, 'hello', [4, 5])
print(1 in my_tuple)  # 输出: True
print('hello' in my_tuple)  # 输出: True
print(6 not in my_tuple)  # 输出: True

# 元组的长度
print('元组的长度:')
my_tuple = (1, 2, 3, 'hello', [4, 5])
print(len(my_tuple))  # 输出: 5

# 元组的不可变性
print('元组的不可变性:')
my_tuple = (1, 2, 3, 'hello', [4, 5])
# my_tuple[0] = 10  # 这会引发 TypeError，因为元组是不可变的

# 元组的索引
print('元组的索引:')
my_tuple = (1, 2, 3, 'hello', [4, 5])
print(my_tuple.index(2))  # 输出: 1
print(my_tuple.index('hello'))  # 输出: 3
print(my_tuple.index([4, 5]))  # 输出: 4

# 统计元素出现的次数
print('统计元素出现的次数:')
my_tuple = (1, 2, 3, 'hello', [4, 5])
print(my_tuple.count(2))  # 输出: 1
print(my_tuple.count('hello'))  # 输出: 1
print(my_tuple.count([4, 5]))  # 输出: 1

# **************3. 元组的其他操作*************
# 元组的解包
print('元组的解包:')
my_tuple = (1, 2, 3, 'hello', [4, 5])
a, b, c, d, e = my_tuple
print(a, b, c, d, e)  # 输出: 1 2 3 hello [4, 5]
# 注意：解包时，变量的数量必须与元组中的元素数量相匹配，否则会引发 ValueError。

# 元组的嵌套
print('元组的嵌套:')
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple)  # 输出: ((1, 2), (3, 4), (5, 6))
print(nested_tuple[0])  # 输出: (1, 2)
print(nested_tuple[0][0])  # 输出: 1

# 元组的索引和切片
print('元组的索引和切片:')
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple[0:2])  # 输出: ((1, 2), (3, 4))
print(nested_tuple[0][0])  # 输出: 1
print(nested_tuple[0][1])  # 输出: 2

# 元组的内置函数
print('元组的内置函数:')
my_tuple = (1, 2, 3, 4, 5)
print(max(my_tuple))  # 输出: 5
print(min(my_tuple))  # 输出: 1

# 注意：元组没有像列表那样的修改方法（如 append、extend、remove 等），因为它是不可变的。    

# 元组的浅拷贝和深拷贝
print('元组的浅拷贝和深拷贝:')
print('浅拷贝:')
my_tuple = (1, 2, 3, 'hello', [4, 5])
shallow_copy = copy.copy(my_tuple)  # 浅拷贝
shallow_copy[4][0] = 10  # 修改浅拷贝中的列表元素
print(my_tuple)  # 输出: (1, 2, 3, 'hello', [4, 5])
print(shallow_copy)  # 输出: (1, 2, 3, 'hello', [4, 5])
print('深拷贝:')
my_tuple = (1, 2, 3, 'hello', [4, 5])
deep_copy = copy.deepcopy(my_tuple)  # 深拷贝
deep_copy[4][0] = 10  # 修改深拷贝中的列表元素
print(my_tuple)  # 输出: (1, 2, 3, 'hello', [4, 5])
print(deep_copy)  # 输出: (1, 2, 3, 'hello', [4, 5])
# 注意：深拷贝会创建一个新的元组，而浅拷贝只是创建一个新的元组，但是元组中的可变对象（如列表）会引用原始对象。
