'''
类：类是一个模板，用于定义对象的属性和方法。

class 类名:
    def __init__(self, 参数):
        # 初始化方法，用于设置对象的初始状态
        self.属性 = 参数
    
    def 方法名(self, 参数):
        # 方法定义
        pass
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name}, I'm {self.age} years old.")