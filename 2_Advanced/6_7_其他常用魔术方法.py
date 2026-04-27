'''
其他常用魔术方法
    - __call__(self, ...)：使对象可调用，如obj()
    - __getattr__(self, name)：当访问不存在的属性时调用
    - __setattr__(self, name, value)：设置属性时调用
    - __getattribute__(self, name)：访问任何属性时调用
    - __dir__(self)：返回对象的属性列表，用于dir()
'''

'''***************1.__call__(self, ...)***************'''
'''
作用
让自定义实例像函数一样：

语法本质：
obj(参数) ➜ 自动执行 obj.__call__(...)

实战场景
类当做函数工厂
回调对象、闭包替代
机器学习 / 框架中常用（模型实例直接 model(x) 预测）
'''

'''***************1.__call__(self, ...)***************'''
print('1.__call__(self, ...)')

class Demo:
    def __call__(self, a, b):
        return a + b

d = Demo()
# 对象直接加括号调用
print(d(3, 5))   # 8
print('------------------------------------')

'''***************2.__setattr__(self, name, value)***************'''
'''
触发时机
只要执行：
self.xxx = 值
obj.xxx = 值
都会自动触发：__setattr__(self, name, value)
name：属性名字符串
value：要赋的值

致命大坑
不要直接在里面写：
self.name = value   # 无限递归爆炸
因为 self.xxx = 又会触发 __setattr__

用途
数据校验、类型限制
只读属性、权限控制
统一日志、加密赋值
'''
print('2.__setattr__(self, name, value)')

class Person:
    def __setattr__(self, name, value):
        print(f"赋值：{name} = {value}")
        # 必须用 super 真正赋值，否则无限递归
        super().__setattr__(name, value)

p = Person()
p.name = "小明"
p.age = 18
print(p.name)
print(p.age)
print('------------------------------------')

'''***************3.__getattr__(self, name, value)***************'''
'''
getattr ：访问不存在的属性才触发
触发条件
访问 obj.xxx
xxx 不存在
才会走：__getattr__(self, name)
'''
print('3.__getattr__(self, name, value)')

class Person:
    def __init__(self):
        self.name = "小红"

    def __getattr__(self, name):
        print(f"属性 {name} 不存在")
        return None 

p = Person()
print(p.name)   # 正常存在，不触发
print(p.age)     # 不存在 → 触发 __getattr__
print('------------------------------------')

'''***************4.__getattribute__(self, name)***************'''
'''
核心区别（必考）
__getattribute__
只要访问任何属性：不管存在不存在，一律先拦截
__getattr__
只有属性不存在 / 抛异常才触发

执行顺序
obj.xxx
↓
__getattribute__ 先执行
↓
如果找不到/报错
↓
才走 __getattr__

高危坑点
__getattribute__ 内部绝对不要直接写 self.xxx
直接无限递归崩溃，必须用 super()

getattr vs getattribute 终极对比
表格
方法	触发时机	优先级
__getattribute__	所有属性访问	最高，先执行
__getattr__	仅不存在的属性	兜底、最后执行

记忆：
attribute → 全部拦截
attr → 只管找不到的属性
'''
print('4.__getattribute__(self, name)')

class Demo:
    def __init__(self):
        self.a = 10

    def __getattribute__(self, name):
        print(f"拦截访问属性：{name}")
        # 真正获取属性，交给父类
        return super().__getattribute__(name)

d = Demo()
print(d.a)
# 访问不存在的 d.b 同样会先进入 __getattribute__
#print(d.b)
print('------------------------------------')

'''***************5.__dir__(self)***************'''
'''
作用
调用：dir(obj)自动触发 __dir__(self)
需要返回一个字符串列表，代表对外展示的属性 / 方法名

用途
隐藏内部私有属性
精简对外 API 展示
隐藏魔法方法、内部字段，更整洁
'''
print('5.__dir__(self)')

class Student:
    def __init__(self):
        self.name = "小王"
        self.score = 90

    def __dir__(self):
        # 自定义返回的属性列表
        return ["name", "score", "info"]

s = Student()
print(dir(s))
print('------------------------------------')

'''***************6.综合完整示例（五大方法放一起）***************'''
print('6.综合完整示例（五大方法放一起）')
class TestObj:
    # 1. 对象可调用
    def __call__(self, x):
        return x * 2

    # 2. 拦截所有属性赋值
    def __setattr__(self, name, value):
        print(f"[赋值] {name} = {value}")
        super().__setattr__(name, value)

    # 3. 拦截所有属性读取
    def __getattribute__(self, name):
        print(f"[访问属性] {name}")
        return super().__getattribute__(name)

    # 4. 不存在属性兜底
    def __getattr__(self, name):
        print(f"[警告] 属性 {name} 不存在")
        return None

    # 5. 自定义 dir 列表
    def __dir__(self):
        return ["data", "info"]


t = TestObj()
t.data = 100     # __setattr__
print(t.data)    # __getattribute__
print(t.abc)     # __getattribute__ → 不存在 → __getattr__
print(t(5))      # __call__
print(dir(t))    # __dir__