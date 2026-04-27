'''
创建目录结构：
my_math/
├── __init__.py
├── arithmetic.py
└── geometry.py
'''

'''使用包'''
import my_math  # noqa
print(my_math.add(1, 2))  # 输出 3
print(my_math.subtract(5, 3))  # 输出 2
print(my_math.area_of_circle(2))  # 输出 12.566370614359172
print(my_math.arithmetic.add(1, 2))  # 输出 3

