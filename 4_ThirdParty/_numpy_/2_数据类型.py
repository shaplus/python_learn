import numpy as np
'''
使用dtype创建数据类型
'''

'''--------------1. 使用标量类型----------------'''
print('1. 使用标量类型')

'''1.1 使用全称'''
print('1.1 使用全称')
dt = np.dtype(np.int32)     # 返回 dtype 对象
print(dt)
print('-----------------')

'''1.2 使用缩写'''
print('1.2 使用缩写')
dt = np.dtype('c16')
print(dt)
print('-----------------')

'''1.3 字节顺序标注'''
print('1.3 字节顺序标注')
dt = np.dtype('<i4')     # 小端字节顺序
print(dt)
print('----------------------------------')

'''--------------2. 使用结构化数据类型----------------'''
'''
传入外层列表、里面每个元素是长度为 2 的元组，
自动解析为：结构化类型 → 字段名 + 字段类型。
第一项：必须是字符串 = 自定义字段名
第二项：numpy 合法 dtype = 类型
'''
print('2. 使用结构化数据类型')

'''2.1 创建结构化数据类型'''
print('2.1 创建结构化数据类型')
dt = np.dtype([('name', 'S10'), ('age', np.int32)])
print(dt)
print('-----------------')

'''2.2 将数据类型应用于 ndarray 对象'''
print('2.2 将数据类型应用于 ndarray 对象')
dt = np.dtype([('age',np.int8)]) 
a = np.array([(10,),(20,),(30,)], dtype = dt) 
print(a)
print(a.dtype)
print(a['age'])
print('-----------------')

'''
2.3 定义一个结构化数据类型 student
包含字符串字段 name，整数字段 age，及浮点字段 marks
并将这个 dtype 应用到 ndarray 对象
'''
print('2.3 定义一个结构化数据类型 student')
student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')]) 
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student) 
print('student:', student)
print('a:', a)
print('a.dtype:', a.dtype)
print('a["name"]:', a['name'])
print('a["age"]:', a['age'])
print('a["marks"]:', a['marks'])
print('-----------------')
