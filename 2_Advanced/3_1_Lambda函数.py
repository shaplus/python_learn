'''
Lambda函数是一种小型的匿名函数，使用lambda关键字定义，只能包含一个表达式。
语法：lambda 参数列表: 表达式

特点：
- 匿名：没有函数名
- 简洁：只能包含一个表达式
- 灵活：可以作为参数传递给其他函数

lambda 限制（不能做什么）：
- 不能写多行代码、不能 for/while/if 代码块
- 不能使用 return / yield / global / nonlocal
- 逻辑复杂不要用，可读性爆炸差
- 没有函数名，调试报错不直观

总结速记：
- 语法：lambda 参数:单行表达式
- 自动返回结果，无需 return
- 主打临时、简单、一次性逻辑
- 黄金搭档：sorted / map / filter / reduce
- 复杂逻辑 → 改用普通 def 函数
'''

'''**************1. 基本用法***************'''
print('示例1：基本用法')
# 示例1：简单的lambda函数
print('示例1：简单的lambda函数')
add = lambda a, b: a + b    #noqa
print(add(3, 5))  # 输出：8

# 默认参数
print('示例2：默认参数')
add_with_default = lambda x, y=2: x + y    #noqa
print(add_with_default(3))  # 输出：5
print(add_with_default(3, 4))  # 输出：7

# 可变参数
print('示例3：可变参数')
def add_all(*args):
    return sum(args)
print(add_all(1, 2, 3))  # 输出：6
print(add_all(4, 5, 6, 7))  # 输出：22

# 关键字参数
print('示例4：关键字参数')
add_with_keywords = lambda **kwargs: kwargs.get('x') + kwargs.get('y')    #noqa
print(add_with_keywords(x=3, y=4))  # 输出：7

# 三元表达式（lambda 里唯一的判断）
print('示例5：三元表达式')
add_with_ternary = lambda x, y: x - y if x > y else y - x    #noqa
print(add_with_ternary(3, 4))  # 输出：1
print(add_with_ternary(4, 3))  # 输出：1

'''**************2. 作为参数传递***************'''
print('作为参数传递')
# 示例1：作为sort()方法的key参数
print('示例1：作为sort()方法的key参数')
data = [{"name":"A", "age":18}, {"name":"B", "age":16}]
# 按 age 升序
res = sorted(data, key=lambda x: x["age"])
print(res)  # 输出：[{"name":"B", "age":16}, {"name":"A", "age":18}]

# 示例2：作为max()函数的key参数
print('示例2：作为max()函数的key参数')
numbers = [1, 3, 5, 2, 4]
max_num = max(numbers, key=lambda x: -x)  # 找到最小值（通过取反）
print(max_num)  # 输出：1

'''**************3. 其他应用***************'''
print('其他应用')
# 嵌套 lambda
print('示例6：嵌套 lambda')
add_with_nested = lambda x, y: lambda z: x + y + z    #noqa
print(add_with_nested(1, 2)(3))  # 输出：6
print(add_with_nested(4, 5)(6))  # 输出：15

# 闭包 + lambda（保留外层变量）
print('示例7：闭包 + lambda')
def outer(n):
    return lambda x: x * n

f2 = outer(2)
f3 = outer(3)
print(f2(5), f3(5)) # 10 15

# 列表推导式 + lambda 经典坑（必看面试题）
print('示例8：列表推导式 + lambda 经典坑')
funcs = [lambda x: x*i for i in range(3)]
for f in funcs:
    print(f(1))
# 错误输出：2 2 2
# 原因：lambda 延迟取值，循环结束 i=2
# 解决：加默认参数绑定即时变量
print('解决方法：')
funcs = [lambda x, i=i: x*i for i in range(3)]
for f in funcs:
    print(f(1))
# 输出：1 2 3


