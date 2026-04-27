'''
字符串表示
    - __str__(self)：返回对象的字符串表示，用于str()和print()
    - __repr__(self)：返回对象的官方字符串表示，用于repr()
    - __format__(self, format_spec)：用于格式化输出

str 与 repr 完整区别表
表格
项目 | __str__ | __repr__
面向人群 | 普通用户 | 开发者、调试
输出风格 | 简短、友好、易懂 | 完整、精确、可重建
触发方式 | print() / str() | repr ()、容器、终端变量
缺失时 | 不生效 | 充当 str 的兜底
强制格式 | 无强制规范 | 建议：类名 (参数)
用途 | 日志展示、前端文案 | 调试、日志排错、开发

开发最佳实践（必记）
1. 日常类，至少必写 repr
保证调试时能看到对象属性，不看内存地址
2. 面向用户输出、展示文案，再额外写 str
3. 内部服务、工具类、模型类：
只写 __repr__ 完全够用
4. 数据模型（ORM、实体类）：
两个都写，str 给业务看，repr 给 debug 看


'''

'''***********__str__ 方法**********'''
'''
当你执行：
print(对象)
str(对象)
f"{对象}"
解释器会自动调用这个类的 __str__ 方法
必须 return 一个字符串

不写 __str__ 会怎样？
默认原生输出：类名 + 内存地址，看不懂、毫无意义
'''
print('__str__ 方法')


'''手写 str 标准写法'''
print('1.手写 str 标准写法')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 自定义打印格式
    def __str__(self):
        # 必须返回字符串
        return f"Person(姓名:{self.name}, 年龄:{self.age})"

p = Person("张三", 18)
print(p)         # 自动调用 __str__
print(str(p))    # 主动转字符串，也会调用
print('------------------------------------')

'''***********__repr__ 方法**********'''
'''
__repr__：开发者 / 解释器 视图
官方设计初衷：
\boldsymbol{repr} 输出原则：尽可能还原对象，可直接复制代码重建实例

触发场景
交互式终端 / REPL 直接敲变量
容器包裹对象：list(obj)、[]、dict、set 里的对象
单独 repr(obj)
格式化：%r
没有定义 __str__ 时，print 会自动降级用 __repr__
'''
print('__repr__ 方法\n')


# 一般写法
print('1.一般写法')
class Cat:
    def __str__(self):
        return "用户看：可爱小猫"

    def __repr__(self):
        return "Cat(name='咪咪', age=2)"

c = Cat()

print(c)         # 优先 __str__
print(repr(c))   # 强制 __repr__
print(str(c))    # 强制 __str__

# 容器内一律走 repr
print([c, c])    
print('----------------')


# 规范写法
'''
!r 是什么？
{x!r} = 等价 repr(x)
{x!s} = 等价 str(x)
写 __repr__ 强烈建议加 !r，格式统一、避免字符串不带引号等问题。
'''
print('2.规范写法')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        # !r 代表用 repr 格式化变量，更规范
        return f"Person(name={self.name!r}, age={self.age!r})"

p = Person("李四", 20)
print(repr(p))
print('------------------------------------')

'''***********__format__ 方法**********'''
'''
定义
__format__(self, format_spec)
专门控制：对象在 f-string / format() 格式化时的输出样式

触发场景
f"{obj:自定义格式}"
str.format() 里格式化对象
format(obj, 格式字符串)
优先级：
__format__ > __str__ > __repr__

方法参数说明
def __format__(self, format_spec):
    pass
- self：当前实例
- format_spec：格式说明符
    就是冒号后面的内容，例如：f"{x:xxx}" 里的 xxx
'''
print('__format__ 方法')


'''1.最简基础示例'''
print('1.最简基础示例')
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __format__(self, format_spec):
        # format_spec 就是 :后面的格式
        if not format_spec:
            # 没传格式，默认简洁输出
            return f"({self.x}, {self.y})"
        # 自定义分支
        if format_spec == "raw":
            return f"x={self.x},y={self.y}"
        elif format_spec == "star":
            return f"*{self.x}|{self.y}*"
        # 未知格式兜底
        return f"({self.x},{self.y})"

p = Point(3, 4)

print(p)
print(format(p))          # 无格式
print(f"{p}")            # 无格式
print(f"{p:raw}")        # 自定义raw格式
print(f"{p:star}")       # 自定义star格式
