'''
多态：多态是指不同对象对同一方法的响应不同，实现代码的灵活性和可扩展性。
'''

# 父类：动物
class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print(f"{self.name} is making a sound.")

# 子类：狗
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def make_sound(self):
        print(f"{self.name} is barking.")

# 子类：猫
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def make_sound(self):
        print(f"{self.name} is meowing.")
# 实例化对象
d1 = Dog("Buddy")
c1 = Cat("Kitty")

# 调用方法
# 多态：根据对象的具体类型调用对应的方法
# 这是多态的一个重要特征，允许使用通用的接口来处理不同的对象
print('调用方法：')
d1.make_sound()
c1.make_sound()