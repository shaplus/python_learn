'''
构造与初始化
    - __init__(self, ...)：初始化方法，在创建对象时调用
    - __new__(cls, ...)：创建对象的方法，在__init__之前调用
    - __del__(self)：析构方法，在对象被销毁时调用
'''

'''************__init__**************'''
print('__init__ 方法')
class MyObject:
    def __init__(self, value):
        self.value = value

obj = MyObject(100)
print(obj.value)
print('------------------------------------')

'''************__new__**************'''
'''
__new__(cls, ...)：创建对象的方法(分配内存)，在__init__之前调用

super()
代表当前类的父类
所有 Python 类默认顶层父类是：object
所以：
super() ➜ 就是 object 类

object.__new__
Python 底层原生、唯一会真正开辟内存、创建空实例的方法
- 它是系统内置的底层方法
- 只有它能从内存里「抠一块空间，造出一个空白对象」
- 你自己写的 def __new__ 只是重写、拦截，没有造对象能力

括号里的 cls
cls：当前你这个类本身
告诉底层：请造一个「属于我这个类」的空对象

执行流程全景：
调用 A()
　↓
触发 A.__new__(cls)
　↓
super().__new__(cls)  # 【关键】object 底层开辟内存、生成空白实例
　↓
拿到空白实例，可自定义加工
　↓
return 实例
　↓
把实例传给 __init__(self) 做初始化
'''
print('__new__ 方法')
# 示例1：不重写__new__，直接返回父类的__new__结果
print('示例1：不重写__new__，直接返回父类的__new__结果')
class MyObject:
    def __new__(cls):
        print('__new__ 方法被调用')
        return super().__new__(cls)
    
    def __init__(self):
        print('__init__ 方法被调用')

obj = MyObject()
print(obj)
print('------------------')

# 示例2：重写__new__，返回自定义对象
print('示例2：重写__new__，返回自定义对象')
class Singleton:
    # 类属性：保存唯一实例
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            # 第一次：创建实例
            cls._instance = super().__new__(cls)
        # 之后全部返回同一个实例
        return cls._instance

# 测试
s1 = Singleton()
s2 = Singleton()
print(s1)
print(s2)

print(s1 is s2)   # True 完全同一个对象
print('------------------------------------')

'''************__del__**************'''
'''
__del__：销毁对象（回收内存、收尾清理）

触发时机：
当一个对象引用计数为 0、即将被垃圾回收 (GC) 时，
Python 解释器会自动调用该对象的 __del__ 方法。

核心：引用计数（必须懂）:
Python 靠「引用计数」管理内存：
每多一个变量指向对象，引用计数 +1
每少一个指向（del、变量销毁、函数结束），引用计数 -1
引用计数 == 0 → 立刻触发 __del__ → 回收内存
'''
print('__del__ 方法')

'''最简语法'''
print('1.最简语法')
class Demo:
    def __del__(self):
        print("对象被销毁，执行 __del__")

obj = Demo()
del obj
print('------------------')

'''引用计数'''
print('2.引用计数')
class Test:
    def __del__(self):
        print("=== 执行 __del__ ===")

# 1. 创建对象，引用计数=1
t = Test()

# 2. 新增引用，计数=2
t2 = t

# 3. 删除一个引用，计数=1，不会销毁
del t

print("---- 中间代码 ----")

# 4. 最后一个引用删除，计数=0，触发 __del__
del t2
print('------------------')

'''案例：模拟文件兜底关闭'''
print('3.案例：模拟文件兜底关闭')
class FileTool:
    def __init__(self, path):
        self.f = open(path, "r", encoding="utf-8")
        print("文件打开成功")

    def read(self):
        return self.f.read()

    # 对象销毁时，强制关闭文件
    def __del__(self):
        if self.f:
            self.f.close()
            print("文件已通过 __del__ 兜底关闭")

# 没有手动 close，也没有 with
f = FileTool("example.txt")
print(f.read())
# 函数/代码块结束，引用消失，自动触发 __del__ 关闭