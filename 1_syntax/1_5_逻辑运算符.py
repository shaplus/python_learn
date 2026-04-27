'''逻辑运算符用于连接多个条件表达式，返回一个布尔值（True或False）。常见的逻辑运算符包括：
- and：当两个条件都为True时，返回True，否则返回False。  
- or：当至少有一个条件为True时，返回True，否则返回False。
- not：用于取反一个条件，如果条件为True，则返回False；如果条件为False，则返回True。
逻辑运算符的优先级：not > and > or。
例如：
逻辑运算符
运算符	描述	例子	结果
and	与	True and False	False
or	或	True or False	True
not	非	not True	False
'''

x = True
y = False

print('x=', x)
print('y=', y)
print('x and y:', x and y)  # False
print('x or y:', x or y)  # True
print('not x:', not x)  # False
print('x ^ y:', x ^ y)  # True
