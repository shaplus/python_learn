import copy
'''字典'''
'''
字典是无序的键值对集合，使用大括号{}定义，键必须是唯一的，可以是任何不可变类型，
值可以是任何类型。
'''

'''
目录
1. 创建字典
1.1 创建一个空字典
1.2 创建一个包含元素的字典
1.3 使用dict()函数创建字典
2. 字典的基本操作
2.1 访问字典中的元素
2.2 字典的添加和修改操作
2.3 字典的删除操作
2.4 字典的清空操作
3. 字典的其他操作
3.1 字典的成员资格测试操作
3.2 字典的长度操作
3.3 get()方法访问字典中的元素
3.4 items()方法遍历字典中的键值对
3.5 keys()方法遍历字典中的键
3.6 values()方法遍历字典中的值
3.7 popitem()方法删除并返回字典中的最后一个键值对
3.8 update()方法可以同时更新多个键值对
3.9 setdefault()方法可以在字典中设置默认值
3.10 字典的复制操作
'''

# **************1. 创建字典*************
# 1.1 创建一个空字典
my_dict = {}
# 或者
my_dict = dict()

# 1.2 创建一个包含元素的字典
print('创建一个包含元素的字典:')
my_dict = {'name': '张三', 'age': 18, 'gender': '男'}
print(my_dict)
print(type(my_dict))  # 输出: <class 'dict'>
#或者使用dict()函数创建字典
my_dict = dict(name='张三', age=18, gender='男')
print(my_dict)
print(type(my_dict))  # 输出: <class 'dict'>

# **************2. 字典的基本操作*************
# 2.1 访问字典中的元素
print('访问字典中的元素:')
my_dict = {'name': '张三', 'age': 18, 'gender': '男'}
print(my_dict['name'])  # 输出: 张三
print(my_dict['age'])   # 输出: 18
print(my_dict['gender'])  # 输出: 男
# 注意：访问不存在的键会引发KeyError异常
# print(my_dict['address'])  # KeyError: 'address'

# 2.2 字典的添加和修改
print('字典的添加和修改:')
my_dict = {'name': '张三', 'age': 18, 'gender': '男'}
print(my_dict)  # 输出: {'name': '张三', 'age': 18, 'gender': '男'}
# 添加新的键值对
my_dict['address'] = '北京市'
print(my_dict)  # 输出: {'name': '张三', 'age': 18, 'gender': '男', 'address': '北京市'}
# 修改已存在的键的值
my_dict['age'] = 19
print(my_dict)  # 输出: {'name': '张三', 'age': 19, 'gender': '男', 'address': '北京市'}    

# 2.3 字典的删除
print('字典的删除:')
my_dict = {'name': '张三', 'age': 18, 'gender': '男', 'address': '北京市'}
print(my_dict)  # 输出: {'name': '张三', 'age': 18, 'gender': '男', 'address': '北京市'}
# 删除指定键值对
del my_dict['address']
print(my_dict)  # 输出: {'name': '张三', 'age': 18, 'gender': '男'}
# 使用pop()方法删除并返回指定键的值
age = my_dict.pop('age')
print(f"删除的年龄: {age}")  # 输出: 删除的年龄: 18
print(my_dict)  # 输出: {'name': '张三', 'gender': '男'}

# 2.4 清空字典
print('清空字典:')
my_dict = {'name': '张三', 'age': 18, 'gender': '男'}
print(my_dict)  # 输出: {'name': '张三', 'age': 18, 'gender': '男'}
my_dict.clear()
print(my_dict)  # 输出: {}

# **************3. 字典的其他操作*************
# 3.1 字典的成员资格测试操作
print('字典的成员资格测试操作:')
my_dict = {'name': '张三', 'age': 18, 'gender': '男'}
print('name' in my_dict)  # 输出: True
print('address' in my_dict)  # 输出: False

# 3.2 字典的长度操作
print('字典的长度操作:')
my_dict = {'name': '张三', 'age': 18, 'gender': '男'}
print(len(my_dict))  # 输出: 3

# 3.3 get()方法访问字典中的元素
print('get()方法访问字典中的元素:')
my_dict = {'name': '张三', 'age': 18, 'gender': '男'}
print(my_dict.get('name'))  # 输出: 张三
print(my_dict.get('age'))   # 输出: 18
print(my_dict.get('gender'))  # 输出: 男
# 注意：get不存在的键时，会返回 None 而不是引发 KeyError
print(my_dict.get('address'))  # 输出: None
print(my_dict.get('address', '默认值'))  # 输出: 默认值

# 3.4 items()方法遍历字典中的键值对
print('items()方法遍历字典中的键值对:')
my_dict = {'name': '张三', 'age': 18, 'gender': '男'}
my_dict = my_dict.items()
print(my_dict)
for key, value in my_dict:
    print(f"{key}: {value}")
# 输出:
# name: 张三
# age: 18
# gender: 男

# 3.5 keys()方法遍历字典中的键
print('keys()方法遍历字典中的键:')
my_dict = {'name': '张三', 'age': 18, 'gender': '男'}
for key in my_dict.keys():
    print(key)
# 输出:
# name
# age
# gender

# 3.6 values()方法遍历字典中的值
print('values()方法遍历字典中的值:')
my_dict = {'name': '张三', 'age': 18, 'gender': '男'}
for value in my_dict.values():
    print(value)
# 输出:
# 张三
# 18
# 男

# 3.7 popitem()方法删除并返回字典中的最后一个键值对
print('popitem()方法删除并返回字典中的最后一个键值对:')
my_dict = {'name': '张三', 'age': 18, 'gender': '男'}
print(my_dict.popitem())  # 输出: ('gender', '男')
print(my_dict)  # 输出: {'name': '张三', 'age': 18}

# 3.8 update()方法可以同时更新多个键值对
print('update()方法可以同时更新多个键值对:')
my_dict = {'name': '张三', 'age': 18, 'gender': '男'}
print(my_dict)  # 输出: {'name': '张三', 'age': 18, 'gender': '男'}
my_dict.update({'email': 'zhangsan@example.com', 'phone': '1234567890'})
print(my_dict)  # 输出: {'name': '张三', 'age': 18, 'gender': '男', 'email': 'zhangsan@example.com', 'phone': '1234567890'}

# 3.9 setdefault()方法可以在字典中设置默认值
print('setdefault()方法可以在字典中设置默认值:')
my_dict = {'name': '张三', 'age': 18, 'gender': '男'}
print(my_dict)  # 输出: {'name': '张三', 'age': 18, 'gender': '男'}
# 如果键存在，返回对应的值
print(my_dict.setdefault('name', '李四'))  # 输出: 张三
# 如果键不存在，设置默认值并返回
print(my_dict.setdefault('address', '北京市'))  # 输出: 北京市
print(my_dict)  # 输出: {'name': '张三', 'age': 18, 'gender': '男', 'address': '北京市'}

# 3.10 字典的复制
print('字典的复制:')
my_dict = {'name': '张三', 'age': 18, 'gender': '男'}
print(my_dict)  # 输出: {'name': '张三', 'age': 18, 'gender': '男'}
# 使用copy()方法复制字典
new_dict = my_dict.copy()
print(new_dict)  # 输出: {'name': '张三', 'age': 18, 'gender': '男'}
# 注意：copy()方法是浅复制，如果字典中包含可变对象（如列表、字典等），则复制的是引用，而不是对象本身。
print('字典的浅复制:')
my_dict = {'name': '张三', 'age': 18, 'address': ['北京市', '上海市']}
print(my_dict)  # 输出: {'name': '张三', 'age': 18, 'address': ['北京市', '上海市']}
new_dict = my_dict.copy()
new_dict['address'][0] = '广州市'
print(my_dict)  # 输出: {'name': '张三', 'age': 18, 'address': ['北京市', '上海市']}
print(new_dict)  # 输出: {'name': '张三', 'age': 18, 'address': ['广州市', '上海市']}
# 注意：如果字典中包含可变对象，复制的是引用，而不是对象本身。
# 如果需要深复制，可以使用 copy.deepcopy() 方法。
print('字典的深复制:')
my_dict = {'name': '张三', 'age': 18, 'address': ['北京市', '上海市']}
print(my_dict)  # 输出: {'name': '张三', 'age': 18, 'address': ['北京市', '上海市']}
new_dict = copy.deepcopy(my_dict)
new_dict['address'][0] = '广州市'
print(my_dict)  # 输出: {'name': '张三', 'age': 18, 'address': ['北京市', '上海市']}
print(new_dict)  # 输出: {'name': '张三', 'age': 18, 'address': ['广州市', '上海市']}
