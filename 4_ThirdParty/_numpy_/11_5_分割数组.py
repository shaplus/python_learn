import numpy as np

'''*********************1. numpy.split**********************'''
print('1. numpy.split')

print('示例1：')
a = np.arange(9)
 
print ('第一个数组：')
print (a)
print ('\n')
 
print ('将数组分为三个大小相等的子数组：')
b = np.split(a,3)
print (b)
print ('\n')
 
print ('将数组在一维数组中表明的位置分割：')
b = np.split(a,[4,7])
print (b)
print('-----------------')

print('示例2：axis 为 0 时在水平方向分割，axis 为 1 时在垂直方向分割：')
a = np.arange(16).reshape(4, 4)
print('第一个数组：')
print(a)
print('\n')
print('默认分割（0轴）：')
b = np.split(a,2)
print(b)
print('\n')

print('沿垂直方向分割,分割后呈水平分布：')
c = np.split(a,2,1)
print(c)
print('\n')

print('沿垂直方向分割,分割后呈水平分布：')
d= np.hsplit(a,2)
print(d)

print('----------------------------------')

'''*********************2. numpy.hsplit**********************'''
print('2. numpy.hsplit')

harr = np.floor(10 * np.random.random((2, 6)))
print ('原array：')
print(harr)
 
print ('拆分后：')
print(np.hsplit(harr, 3))
print('----------------------------------')

'''*********************3. numpy.vsplit**********************'''
print('3. numpy.vsplit')

a = np.arange(16).reshape(4,4)
 
print ('第一个数组：')
print (a)
print ('\n')
 
print ('竖直分割：')
b = np.vsplit(a,2)
print (b)
print('----------------------------------')
