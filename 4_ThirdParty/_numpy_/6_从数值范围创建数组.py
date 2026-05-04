import numpy as np

'''----------------1. numpy.arange----------------'''
'''
numpy 包中的使用 arange 函数创建数值范围并返回 ndarray 对象，函数格式如下：
numpy.arange(start, stop, step, dtype)
'''
print('1. numpy.arange')

'''生成 0 到 4 长度为 5 的数组:'''
print('生成 0 到 4 长度为 5 的数组:')
x = np.arange(5)  
print (x)
print('----------------')

'''设置返回类型位 float:'''
print('设置返回类型位 float:')
# 设置了 dtype
x = np.arange(5, dtype =  float)  
print (x)
print('----------------')

'''设置了起始值、终止值及步长：'''
print('设置了起始值、终止值及步长：')
# 设置了 start, stop, step
x = np.arange(0, 10, 2)  
print (x)
print('--------------------------------')

'''----------------2. numpy.linspace----------------'''
'''
numpy.linspace 函数用于创建一个一维数组，数组是一个等差数列构成的，格式如下：
np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
'''
print('2. numpy.linspace')

'''设置起始点为 1 ，终止点为 10，数列个数为 10'''
print('设置起始点为 1 ，终止点为 10，数列个数为 10')
x = np.linspace(1, 10, 10)  
print (x)
print('----------------')

'''设置元素全部是1的等差数列：'''
print('设置元素全部是1的等差数列：')
x = np.linspace(1, 1, 10)  
print (x)
print('----------------')

'''将 endpoint 设为 false，不包含终止值：'''
print('将 endpoint 设为 false，不包含终止值：')
a = np.linspace(10, 20,  5, endpoint =  False)  
print(a)
print('----------------')

'''设置 retstep 为 true，返回间距：'''
print('设置 retstep 为 true，返回间距：')
a, step = np.linspace(1,10,10,retstep= True)
print(a)
print('间距为', step)
print('--------------------------------')

'''----------------3. numpy.logspace----------------'''
'''
numpy.logspace 函数用于创建一个于等比数列。格式如下：
np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
相当于把对数等差化，生成一个等比数列。
'''
print('3. numpy.logspace')

# 默认底数是 10
# 先生成[1.0, 2.0, 3.0], 再生成[10^1, 10^2, 10^3]
a = np.logspace(1.0,  3.0, num =  3)  
print (a)
print('----------------')

# 更改底数为 2
# 先生成[1.0, 2.0, 3.0], 再生成[2^1, 2^2, 2^3]
a = np.logspace(1,3,3,base=2)
print (a)
print('--------------------------------')