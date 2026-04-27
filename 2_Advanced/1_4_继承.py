'''
继承是子类继承父类的属性和方法，实现代码复用，同时可以添加或重写方法

基本语法：
class 子类名(父类名):
    def __init__(self, 参数):
        super().__init__(父类参数)  # 调用父类的初始化方法
        # 子类的初始化代码
    
    # 子类可以添加新方法或重写父类方法
'''

# 父类：人
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name}, I'm {self.age} years old.")

# 子类：学生
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # 调用父类的初始化方法
        self._student_id = student_id
    
    def study(self, subject):
        print(f"{self.name} is studying {subject}")
    
    def greet(self):  # 重写父类的greet方法
        print(f"Hello, I'm {self.name}, a student with ID {self._student_id}")

# 实例化对象
s1 = Student("Alice", 20, "123456")

# 调用方法
print('调用方法：')
s1.greet()
s1.study("Math")