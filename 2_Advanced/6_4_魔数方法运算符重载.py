'''
- 算术运算符：__add__, __sub__, __mul__, __truediv__等
- 比较运算符：__eq__, __ne__, __lt__, __gt__等
- 增量赋值运算符：__iadd__, __isub__等

三大类运算符 本质区别总结
1. 算术运算：add / sub…
无副作用
不修改原对象
返回新实例
对应：+ - * /
2. 比较运算：eq / lt…
纯判断
返回布尔值
对应：== != < >
3. 就地赋值：iadd / isub…
原地修改自身属性
必须 return self
对应：+= -= *= /=

极简记忆口诀
普通运算（+ - * /）：
__add__ 造新对象，不改自己
比较运算（== > <）：
__eq__ 判内容，返回 True/False
赋值运算（+= -=）：
__iadd__ 改自己，最后 return self
'''

'''***********算术运算符**********'''
'''
Python 语法糖本质：
a + b → 自动调用 a.__add__(b)

对应关系一览
表格
运算符	魔法方法	作用
+	__add__(self, other)	加法
-	__sub__(self, other)	减法
*	__mul__(self, other)	乘法
/	__truediv__(self, other)	真除法（浮点数结果）
//	__floordiv__(self, other)	地板除
%	__mod__(self, other)	取模 / 余数
**	__pow__(self, other)	幂运算

规则
语法：self 运算符 other
左边对象调用自身魔法方法，传入右边对象
必须返回新对象 / 新值，不修改自身
'''
print('算术运算符')

'''1.最简基础示例'''
print('1.最简基础示例')
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # +
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # -
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    # *
    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    # /
    def __truediv__(self, other):
        return Vector(self.x / other.x, self.y / other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(10, 20)
v2 = Vector(2, 4)

print(v1 + v2)
print(v1 - v2)
print(v1 * v2)
print(v1 / v2)
print('--------------------------------')

'''***********比较运算符**********'''
'''
对应关系一览
表格
运算符	魔法方法	含义
==	__eq__(self, other)	等于（Equal）
!=	__ne__(self, other)	不等于（Not Equal）
<	__lt__(self, other)	小于（Less Than）
>	__gt__(self, other)	大于（Greater Than）
<=	__le__(self, other)	小于等于（Less Than or Equal）
>=	__ge__(self, other)	大于等于（Greater Than or Equal）

关键规则
所有比较方法必须返回 bool（True / False）
默认 == 是内存地址比较，重写 __eq__ 才能按内容比较
写全太麻烦：可用 functools.total_ordering 装饰器一键补全
'''
print('比较运算符')

'''示例1：按数值大小比较'''
print('示例1：按数值大小比较')
class Number:
    def __init__(self, value):
        self.value = value

    # ==
    def __eq__(self, other):
        return self.value == other.value

    # <
    def __lt__(self, other):
        return self.value < other.value

    # >
    def __gt__(self, other):
        return self.value > other.value


a = Number(10)
b = Number(20)

print(a == b)
print(a < b)
print(a > b)
print('--------------------------------')

'''***********增量赋值运算符**********'''
'''
运算符	魔法方法	作用
+=	__iadd__(self, other)	就地加法
-=	__isub__(self, other)	就地减法
*=	__imul__(self, other)	就地乘法
/=	__itruediv__(self, other)	就地除法

核心区别（重中之重）
普通算术 __add__
不修改原对象
返回全新对象
增量赋值 __iadd__
就地修改 self 自身
必须返回 self
'''
print('增量赋值运算符\n')

# 示例1：与普通算术运算符的区别
print('示例1：与普通算术运算符的区别')
class Point:
    def __init__(self, x):
        self.x = x

    # 普通 + ：返回新对象
    def __add__(self, other):
        return Point(self.x + other.x)

    # 就地 += ：修改自己，返回 self
    def __iadd__(self, other):
        self.x += other.x
        return self     # 必须返回 self，否则 += 无效果

    def __repr__(self):
        return f"Point({self.x})"


p1 = Point(10)
p2 = Point(5)

# 普通加法：产生新对象
p3 = p1 + p2
print(p1)
print(p3)

# 增量赋值：修改原对象
p1 += p2
print(p1)


'''***********拓展：一键快速开发**********'''
'''如果需要大量比较运算符，不用一个个手写：'''
print('拓展：一键快速开发\n')
from functools import total_ordering    # noqa

@total_ordering
class Score:
    def __init__(self, num):
        self.num = num

    def __eq__(self, other):
        return self.num == other.num

    def __lt__(self, other):
        return self.num < other.num
    # 自动补全 > >= <= != 全部方法

print('自动补全 > >= <= != 全部方法')
print(Score(10) == Score(10))
print(Score(10) < Score(20))
print(Score(10) > Score(20))
print(Score(10) <= Score(20))
print(Score(10) >= Score(20))