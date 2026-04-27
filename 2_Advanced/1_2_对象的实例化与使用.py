'''
1.对象的实例化
2.访问属性
3.调用方法

self参数的理解:
- self是一个特殊的参数，它代表类的实例本身。在方法中，通过self可以访问实例的属性和其他方法。
注意：
- self参数必须放在方法参数列表的最前面，其他参数可以按照任意顺序排列。
- 调用方法时，不需要传递self参数，Python会自动传递。
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name}, I'm {self.age} years old.")

# 实例化对象
p1 = Person("Alice", 30)

# 访问属性
print('访问属性：')
print(p1.name)
print(p1.age)

# 调用方法
print('调用方法：')
p1.greet()
