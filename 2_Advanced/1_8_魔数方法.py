'''
魔术方法是Python中特殊的方法，以双下划线开头和结尾，用于实现特定的功能。

常用的魔数方法：
__init__：初始化方法，用于创建对象时调用。
__str__：字符串表示方法，用于将对象转换为字符串。
__repr__：返回对象的正式字符串表示，用于调试和日志记录。
__len__：长度方法，用于获取对象的长度。
__getitem__：获取对象的元素，用于索引操作。
__setitem__：设置对象的元素，用于索引赋值操作。
__delitem__：删除对象的元素，用于索引删除操作。
__iter__：迭代器，用于对象的迭代操作。
__next__：实现迭代器协议，用于获取下一个迭代的元素。
__call__：使对象可调用，用于对象作为函数调用。
__add__：加法方法，用于对象的加法操作。
__sub__：减法方法，用于对象的减法操作。
__mul__：乘法方法，用于对象的乘法操作。
__div__：除法方法，用于对象的除法操作。
__mod__：取余方法，用于对象的取余操作。
__pow__：指数方法，用于对象的指数操作。
'''

# 示例
class MyList:
    def __init__(self, *args):
        self.items = list(args)
    
    def __str__(self):
        return f"MyList({self.items})"
    
    def __repr__(self):
        return f"MyList({self.items})"
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, value):
        self.items[index] = value
    
    def __delitem__(self, index):
        del self.items[index]
    
    def __iter__(self):
        return iter(self.items)
    
# 实例化对象
my_list = MyList(1, 2, 3)
print(my_list)
print(repr(my_list))
print(len(my_list))
print(my_list[0])
my_list[0] = 100
print(my_list)
del my_list[0]
print(my_list)
for item in my_list:
    print(item)