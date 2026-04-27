'''
2. 数据类型
Python中常见的数据类型有：

数据类型	描述	例子
整数 (int)	整数，包括正整数、负整数和0	10, -5, 0
浮点数 (float)	带小数点的数	3.14, -0.5
字符串 (str)	由字符组成的序列，用引号包围	"Hello", 'Python'
布尔值 (bool)	只有两个值：True（真）和 False（假）	True, False
列表 (list)	有序的可变序列，用方括号包围	[1, 2, 3], ["a", "b"]
字典 (dict)	键值对的集合，用花括号包围	{"name": "Alice", "age": 18}
'''
#整数
num1 = 88
print(num1)

#浮点数
num2 = 6.66
print(num2)

#字符串
str1 = "Hello, World!"
print(str1)
print(type(str1))

#布尔值
is_people = True
print(is_people)
print(type(is_people))

#列表
list1 = [1, 2, 3, 4, 5]
fruit = ["apple", "banana", "orange"]
print(list1)
print(fruit)
print(type(list1))
print(type(fruit))

#字典
person = {"name": "Alice", "age": 18, "city": "NewYork"}
print(person)
print(person["name"])
print(type(person["name"]))
print(person["age"])
print(type(person["age"]))
print(person["city"])
print(type(person["city"]))
print(type(person))