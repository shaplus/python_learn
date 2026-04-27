'''
属性装饰器用于将方法转换为属性，方便访问。

属性装饰器：
- @property：将方法转换为属性，允许直接访问方法。
- @setter：设置属性的值。
- @deleter：删除属性。
- @classmethod：类方法，第一个参数是cls，代表类本身。
- @staticmethod：静态方法，没有参数，只能调用类属性和实例属性。
- @abstractmethod：抽象方法，必须在子类中实现。

@property：就是当你 “读取” 这个名字时，Python 自动帮你调用一下这个方法。
@setter：就是当你 “设置” 这个名字时，Python 自动帮你调用一下这个方法。
@deleter：就是当你 “删除” 这个名字时，Python 自动帮你调用一下这个方法。
'''

# 属性装饰器示例
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age
    
    # 读取age属性时，自动调用age方法
    @property
    def age(self):
        return self._age
    
    # 设置age属性时，自动调用age方法
    @age.setter
    def age(self, value):
        self._age = value
    
    # 删除age属性时，自动调用age方法
    @age.deleter
    def age(self):
        del self._age
        print("Age property deleted.")

# 实例化对象
p1 = Person("Alice", 30)

# 调用属性
print('调用属性：')
print(p1.age)

# 设置属性
print('设置属性：')
p1.age = 31
print(p1.age)

# 删除属性
print('删除属性：')
del p1.age