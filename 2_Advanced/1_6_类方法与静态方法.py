'''
类方法与静态方法：

一、类方法（@classmethod）
第一个参数固定：cls（代表当前类，Python 自动传入）
能访问 / 修改：类属性、类方法、静态方法
不能直接访问：实例属性、实例方法（没有 self）
调用方式：
类直接调用：类名.方法()
实例调用：对象.方法()
常用场景：
操作类级别的公共数据
替代构造方法，实现多种创建对象方式
统一初始化、工厂方法

二、静态方法（@staticmethod）
没有默认参数：无 self、无 cls
能访问：只能通过类名访问类属性 / 方法
不能访问：实例属性、实例方法
调用方式：
类直接调用：类名.方法()
实例调用：对象.方法()
本质：就是写在类里的普通工具函数，仅逻辑归类
'''

# 类方法示例
#类方法使用@classmethod装饰器定义，第一个参数是cls，代表类本身。
class Person:
    count = 0  # 类属性
    
    def __init__(self, name):
        self.name = name
        Person.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count

# 实例化对象
p1 = Person("Alice")
p2 = Person("Bob")

# 调用类方法
print('类方法示例：')
print('调用类方法：')
print(Person.get_count())
print(p1.get_count())
print(p2.get_count())

# 静态方法示例
# 静态方法使用@staticmethod装饰器定义，没有参数，只能调用类属性和实例属性。
class Math:
    @staticmethod
    def add(a, b):
        return a + b
    @staticmethod
    def subtract(a, b):
        return a - b

# 调用静态方法
print('静态方法示例：')
print('调用静态方法：')
print(Math.add(3, 5))
print(Math.subtract(10, 4))