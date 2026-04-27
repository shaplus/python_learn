'''
简介：抽象类
- 抽象类是不能实例化的类，用于定义子类必须实现的方法。
- @abstractmethod：抽象方法，必须在子类中实现。
必须导入abc模块：
- from abc import ABC, abstractmethod

抽象类：一句话讲明白
- 抽象类就是一个 “只定规矩、不做实现” 的父类，
- 强制子类必须按规定实现某些方法，否则不能创建对象。
- 你可以把它理解成：接口规范 / 设计图纸 / 强制合同。

用途：为什么要用抽象类？
- 强制规范：子类必须实现所有抽象方法，确保一致的接口。
- 统一接口：子类可以使用统一的接口调用，无需关心实现细节。
- 便于维护扩展：可以方便地添加新的子类，而不会修改已有的代码。

总结：抽象类和抽象方法的作用
- 抽象类：定规范，不能实例化
- 抽象方法：只声明，不实现
- 子类：必须全部实现，否则不能实例化子类
- 用途：强制规范、统一接口、便于维护扩展
'''

# 抽象类示例
from abc import ABC, abstractmethod

# 定义一个抽象类 Shape
# 定义两个抽象方法：area() 和 perimeter()
# 子类必须实现这两个方法，否则不能实例化子类，直接报错
# 用途：强制规范、统一接口、便于维护扩展
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
# 实例化对象
circle = Circle(5)
rectangle = Rectangle(4, 6)

# 调用方法
print(circle.area())
print(circle.perimeter())
print(rectangle.area())
print(rectangle.perimeter())