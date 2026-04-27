'''
生成器
生成器是一种特殊的迭代器，它可以在迭代过程中使用yield语句动态生成值，而不是在创建时就确定所有值。
生成器的语法类似于列表推导式，但是用括号()替换方括号[]。
- 生成器更加节省内存，特别适合处理大数据集。

生成器函数使用def定义，包含yield语句。
当调用生成器函数时，它返回一个生成器对象，而不是执行函数体。

生成器的语法如下：
def generator_name():
    for value in values:
        yield value

生成器的优势
- 节省内存：生成器不会一次性存储所有值，而是按需生成
- 惰性计算：只有在需要时才计算下一个值
- 无限序列：可以表示无限序列，如斐波那契数列
- 代码简洁：比自定义迭代器的代码更简洁
'''

# 生成器函数
print('生成器函数')
def generator_name(max_num):
    for i in range(max_num):
        yield i

# 使用生成器函数
fib = generator_name(5)
print(fib)  # 输出：<generator object generator_name at 0x100000000>
for num in fib:
    print(num)  # 输出：0 1 2 3 4 

# 列表推导式（创建完整列表，占用内存）
print('列表推导式')
squares_list = [x**2 for x in range(10)]
print(squares_list)  # 输出：[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 生成器表达式（按需生成，节省内存）
# 生成器表达式的语法类似于列表推导式，但是用括号()替换方括号[]。
# 生成器表达式可以用于创建生成器对象，而不是直接生成列表。
# 生成器表达式的语法如下：
# (expression for variable in iterable if condition)
# 例如：
print('生成器表达式')
generator = (i for i in range(5))
print(generator)  # 输出：<generator object <genexpr> at 0x100000000>
for num in generator:
    print(num)  # 输出：0 1 2 3 4 

# yield语句的工作原理
'''
当生成器函数执行到yield语句时，会暂停执行并返回yield后面的值。
当再次调用next()时，会从暂停的地方继续执行，直到遇到下一个yield语句或函数结束。
'''
print('yield语句的工作原理')
def simple_generator():
    print("开始执行")
    yield 1
    print("继续执行")
    yield 2
    print("结束执行")

# 通过next()函数调用生成器函数
print('通过next()函数调用生成器函数')
gen = simple_generator()
print(next(gen))  # 输出：开始执行，然后输出1
print(next(gen))  # 输出：继续执行，然后输出2
# print(next(gen))  # 输出：结束执行，然后抛出StopIteration异常

# 通过for循环调用生成器函数
print('通过for循环调用生成器函数')
gen = simple_generator()
for num in gen:
    print(num)  # 输出：1 2

