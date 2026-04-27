'''类型转换'''

'''
目录
1. 整数转换为浮点数
2. 浮点数转换为整数
3. 字符串转换为整数
4. 字符串转换为浮点数
5. 字符串转换为布尔值
6. 布尔值转换为字符串
7. 元组转换为列表
8. 列表转换为元组
9. 字典转换为列表
10. 列表转换为字典
11. 集合转换为列表
12. 列表转换为集合
13. 集合转换为元组
14. 元组转换为集合
15. 字典转换为元组
16. 元组转换为字典
17. 字符串转换为列表
18. 列表转换为字符串
'''

# 1. 整数转换为浮点数
print("整数转换为浮点数:")
num = 10
print(num)
print(type(num))
num = float(num)
print(num)
print(type(num))

# 2. 浮点数转换为整数
print("浮点数转换为整数:")
num = 10.1
print(num)
print(type(num))
num = int(num)
print(num)
print(type(num))

# 3. 字符串转换为整数
print("字符串转换为整数:")
num = "10"
print(num)
print(type(num))
num = int(num)
print(num)
print(type(num))

# 4. 字符串转换为浮点数
print("字符串转换为浮点数:")
num = "10.0"
print(num)
print(type(num))
num = float(num)
print(num)
print(type(num))

# 5. 字符串转换为布尔值
print("字符串转换为布尔值:")
num = "True"
print(num)
print(type(num))
num = bool(num)
print(num)
print(type(num))

# 6. 布尔值转换为字符串
print("布尔值转换为字符串:")
num = True
print(num)
print(type(num))
num = str(num)
print(num)
print(type(num))

# 7. 元组转换为列表
print("元组转换为列表:")
num = (1, 2, 3)
print(num)
print(type(num))
num = list(num)
print(num)
print(type(num))

# 8. 列表转换为元组
print("列表转换为元组:")
num = [1, 2, 3]
print(num)
print(type(num))
num = tuple(num)
print(num)
print(type(num))

# 9. 字典转换为列表
print("字典转换为列表:")
num = {"name": "张三", "age": 18, "grade": "A"}
print(num)
print(type(num))
num = list(num.items())
print(num)
print(type(num))

# 10. 列表转换为字典
print("列表转换为字典:")
num = [("name", "张三"), ("age", 18), ("grade", "A")]
print(num)
print(type(num))
num = dict(num)
print(num)
print(type(num))

# 11. 集合转换为列表
print("集合转换为列表:")
num = {1, 2, 3}
print(num)
print(type(num))
num = list(num)
print(num)
print(type(num))

# 12. 列表转换为集合
print("列表转换为集合:")
num = [1, 2, 3]
print(num)
print(type(num))
num = set(num)
print(num)
print(type(num))
print('列表转换为集合后,会自动去重')
num = [1, 1, 2, 2, 3]
print("初始列表:", num)
print("去重后的集合:", set(num))

# 13. 集合转换为元组
print("集合转换为元组:")
num = {1, 2, 3}
print(num)
print(type(num))
num = tuple(num)
print(num)
print(type(num))

# 14. 元组转换为集合
print("元组转换为集合:")
num = (1, 2, 3)
print(num)
print(type(num))
num = set(num)
print(num)
print(type(num))

# 15. 字典转换为元组
print("字典转换为元组:")
num = {"name": "张三", "age": 18, "grade": "A"}
print(num)
print(type(num))
num = tuple(num.items())
print(num)
print(type(num))

# 16. 元组转换为字典
print("元组转换为字典:")
num = ("name", "张三"), ("age", 18), ("grade", "A")
print(num)
print(type(num))
num = dict(num)
print(num)
print(type(num))

# 17. 字符串转换为列表
print("字符串转换为列表:")
num = "hello"
print(num)
print(type(num))
num = list(num)
print(num)
print(type(num))

# 18. 列表转换为字符串
print("列表转换为字符串:")
num = ["h", "e", "l", "l", "o"]
print(num)
print(type(num))
num = "".join(num)
print(num)
print(type(num))
