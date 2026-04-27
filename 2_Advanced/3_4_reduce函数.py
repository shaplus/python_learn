'''
基本概念
reduce()函数用于对可迭代对象中的元素进行累积操作，返回一个单一的值。
它在functools模块中，需要先导入。

语法：
from functools import reduce
reduce(function, iterable, initializer=None)
参数：
- function：要应用的函数，用于对可迭代对象中的元素进行累积操作。
             它的参数是两个元素，第 1 个：累计值 a，第 2 个：当前元素 b。
             返回：新的累计值 a = 计算结果
- iterable：要应用函数的可迭代对象，如列表、元组、字符串等。
- initializer：可选的初始值，用于初始化累积操作。

执行流程（超级重要）：
序列：[1,2,3,4]
计算：a + b
第一步：a=1, b=2 → 3
第二步：a=3, b=3 → 6
第三步：a=6, b=4 → 10
最终结果：10

reduce 底层执行过程图解：
reduce(f, [x1, x2, x3, x4])
等于：f(f(f(x1,x2), x3), x4)

为什么要学 reduce？
- 一行代码完成累计 / 聚合
- 大数据流式处理常用
- 函数式编程核心


'''

'''***************1. 基本用法***************'''
'''示例1：计算列表的和'''
print('示例1：计算列表的和')
# 导入reduce函数
from functools import reduce    # noqa

numbers = [1, 2, 3, 4, 5]
# 无初始值，从序列的第一个元素开始累积
print('示例1：无初始值，从序列的第一个元素开始累积')
sum_result = reduce(lambda x, y: x + y, numbers)
print(sum_result)  # 输出：15 （1 + 2 + 3 + 4 + 5）

# 使用初始值，从初始值开始累积
print('示例1：使用初始值，从初始值开始累积')
sum_result_with_initial = reduce(lambda x, y: x + y, numbers, 10)
print(sum_result_with_initial)  # 输出：25（10 + 1 + 2 + 3 + 4 + 5）

'''示例2：列表求乘积'''
print('示例2：列表求乘积')
res = reduce(lambda a,b: a * b, [1,2,3,4])
print(res)   # 24

'''示例3：找最大值'''
print('示例3：找最大值')
res = reduce(lambda a,b: a if a>b else b, [7,8,12,10])
print(res)   # 12

'''示例4：拼接字符串'''
print('示例4：拼接字符串')
res = reduce(lambda a,b: a+b, ['a','b','c'])
print(res)   # 'abc'


