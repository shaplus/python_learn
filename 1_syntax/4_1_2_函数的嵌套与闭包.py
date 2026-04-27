'''
# 函数的嵌套与闭包

- 函数嵌套的基本形式如下：
def outer_function():
    # 外部函数代码
    def inner_function():
        # 内部函数代码
    # 调用内部函数
    inner_function()

- 闭包（Closure）
闭包是函数嵌套的重要应用，指的是内部函数引用了外部函数的变量，
并且内部函数在外部函数执行完毕后仍然能够访问这些变量。

嵌套函数的优缺点
优点
封装性：内部函数可以访问外部函数的变量，但外部不能访问内部函数的变量
闭包：可以创建带有状态的函数
装饰器：方便地修改函数行为
代码组织：将相关功能组织在一起
缺点
可读性：嵌套层次过深会降低代码可读性
性能：每次调用外部函数都会创建新的内部函数对象
调试难度：嵌套函数可能使调试变得复杂
'''

'''******************作用域规则*******************'''
print("作用域规则:")
'''1. 内部函数可以访问外部函数的变量'''
print("1. 内部函数可以访问外部函数的变量:")
def outer_function():
    outer_var = "外部变量"
    
    def inner_function():
        print(outer_var)  # 可以访问外部函数的变量
    
    inner_function()

outer_function()  # 输出: 外部变量
print("-----------------")

'''2. 内部函数可以修改外部函数的可变对象'''
print("2. 内部函数可以修改外部函数的可变对象:")
def outer_function():
    outer_list = [1, 2, 3]
    print("外部函数的可变对象:", outer_list)

    def inner_function():
        outer_list.append(4)  # 可以修改外部函数的可变对象
    
    inner_function()
    print(outer_list)  # 输出: [1, 2, 3, 4]

outer_function()
print("-----------------")

'''******************闭包*******************'''
print("闭包:")
'''闭包可以访问外部函数的变量，
并且在外部函数执行完毕后仍然能够访问这些变量。'''
print("闭包可以访问外部函数的变量:")
def outer_function():
    outer_var = "外部变量"
    
    def inner_function():
        print(outer_var)  # 可以访问外部函数的变量
    
    return inner_function  # 返回内部函数

inner_function = outer_function()  # 调用外部函数，返回内部函数
inner_function()  # 输出: 外部变量
print("-----------------")

'''闭包返回的内部函数所用到的外部变量会被锁定'''
print("闭包返回的内部函数所用到的外部变量会被锁定:")
def outer_function():
    outer_count = 0
    
    def inner_function():
        nonlocal outer_count  # 声明要修改外部函数的变量
        outer_count += 1
        print(outer_count)  # 可以访问外部函数的变量
    
    return inner_function  # 返回内部函数

inner_function1 = outer_function()  # 调用外部函数，返回内部函数
inner_function1()  # 输出: 1
inner_function1()  # 输出: 2
inner_function1()  # 输出: 3
inner_function2 = outer_function()  # 调用外部函数，返回内部函数
inner_function2()  # 输出: 1
inner_function2()  # 输出: 2
inner_function2()  # 输出: 3
