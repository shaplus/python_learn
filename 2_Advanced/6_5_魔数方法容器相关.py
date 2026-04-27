'''
容器相关
- __len__(self)：返回容器长度，用于len()
- __getitem__(self, key)：获取元素，用于obj[key]
- __setitem__(self, key, value)：设置元素，用于obj[key] = value
- __delitem__(self, key)：删除元素，用于del obj[key]
- __iter__(self)：返回迭代器，用于for循环
- __contains__(self, item)：检查元素是否存在，用于in运算符

总览：语法 ↔ 魔法方法
表格
语法	自动调用方法	作用
len(obj)	__len__(self)	获取长度
obj[key]	__getitem__(self, key)	取值
obj[key] = val	__setitem__(self, key, val)	赋值
del obj[key]	__delitem__(self, key)	删除元素
for x in obj	__iter__(self)	迭代遍历
x in obj	__contains__(self, item)	成员判断
'''

'''***********1. __len__(self)**********'''
'''
作用：让自定义对象支持 len()
要求：必须返回整数
'''
print('1. __len__(self)')

'''示例1'''
print('示例1')

class MyList:
    def __init__(self):
        self.data = [11, 22, 33]

    def __len__(self):
        # 返回容器元素个数
        return len(self.data)

obj = MyList()
print(len(obj))  # 3
print('----------------------------------')

'''***********2. __getitem__(self, key)**********'''
'''
作用：支持 obj[key] 取值
key 可以是：下标、字符串 key、切片 [1:5]
'''
print('2. __getitem__(self, key)')

'''示例1：自定义字典类取值'''
print('示例1：自定义字典类取值')

class MyDict:
    def __init__(self):
        self._cache = {"name": "张三", "age": 18}

    def __getitem__(self, key):
        # 自定义取值逻辑
        return self._cache.get(key, "不存在")

d = MyDict()
print(d["name"])   # 张三
print(d["addr"])   # 不存在
print('----------------------------------')

'''***********3. __setitem__(self, key, value)**********'''
'''
作用：支持 obj[key] = value 赋值 / 新增
'''
print('3. __setitem__(self, key, value)')

class MyCache:
    def __init__(self):
        self.box = {}

    def __setitem__(self, key, value):
        # 自定义写入规则
        self.box[key] = value
        print(f"写入 {key} = {value}")

c = MyCache()
c["score"] = 99
c["level"] = 5
print(c.box)  # {'score': 99, 'level': 5}
print('----------------------------------')

'''***********4. __delitem__(self, key)**********'''
'''作用：支持 del obj[key] 删除元素'''
print('4. __delitem__(self, key)')

class MyBox:
    def __init__(self):
        self.data = {"a": 1, "b": 2}

    def __delitem__(self, key):
        if key in self.data:
            del self.data[key]
            print(f"删除 {key}")

b = MyBox()
del b["a"]
print(b.data)  # {'b': 2}
print('----------------------------------')

'''***********5. __iter__(self)**********'''
'''作用：返回迭代器，用于for循环'''
print('5. __iter__(self)')

print('示例1：自定义数组类迭代')
class MyArr:
    def __init__(self):
        self.arr = [10, 20, 30]

    def __iter__(self):
        # 返回迭代器
        return iter(self.arr)

for num in MyArr():
    print(num)

print('进阶：自己手写迭代器（理解底层）')
class Counter:
    def __iter__(self):
        self.n = 1
        return self

    def __next__(self):
        if self.n > 3:
            raise StopIteration
        res = self.n
        self.n += 1
        return res

for i in Counter():
    print(i)
print('----------------------------------')

'''***********6. __contains__(self, item)**********'''
'''作用：支持 x in obj 检查元素是否存在，必须返回 True / False'''
print('6. __contains__(self, item)')

class MySet:
    def __init__(self):
        self.items = [5, 6, 7]

    def __contains__(self, item):
        return item in self.items

s = MySet()
print(5 in s)   # True
print(9 in s)   # False
print('----------------------------------')

'''***********7. 综合实战：手写一个简易自定义列表**********'''
print('7. 综合实战：手写一个简易自定义列表')
class CustomList:
    def __init__(self):
        self._data = {}

    # 长度
    def __len__(self):
        return len(self._data)

    # 取值 obj[idx]
    def __getitem__(self, idx):
        return self._data.get(idx)

    # 赋值 obj[idx] = val
    def __setitem__(self, idx, val):
        self._data[idx] = val

    # 删除 del obj[idx]
    def __delitem__(self, idx):
        if idx in self:
            del self._data[idx]

    # 可迭代 for in
    def __iter__(self):
        return iter(self._data.keys())

    # in 判断
    def __contains__(self, item):
        return item in self._data.keys()


# 测试
lst = CustomList()
lst._data = {'a': 1, 'b': 2, 'c': 3}

print(lst._data)
print(len(lst))         # 3
print(lst['a'])           # 1
lst['b'] = 99
print(lst['b'])           # 99
del lst['c']
print('c' in lst)         # False

for x in lst:
    print(x)
