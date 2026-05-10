import numpy as np

'''*****************1. numpy.dot()*********************'''
print('1. numpy.dot()：')

# a的行与b的列相乘
# 计算式：[[1*11+2*13, 1*12+2*14],[3*11+4*13, 3*12+4*14]]
a = np.array([[1,2],[3,4]])
b = np.array([[11,12],[13,14]])
print(np.dot(a,b))
print('-'*50)

'''*****************2. numpy.vdot()*********************'''
print('2. numpy.vdot()：')

# 计算式：1*11 + 2*12 + 3*13 + 4*14 = 130
a = np.array([[1,2],[3,4]]) 
b = np.array([[11,12],[13,14]]) 
 
# vdot 将数组展开计算内积
print (np.vdot(a,b))
print('-'*50)

'''*****************3. numpy.inner()*********************'''
print('3. numpy.inner()：')

print('示例1:')
print (np.inner(np.array([1,2,3]),np.array([0,1,0])))
# 等价于 1*0+2*1+3*0
print('-'*25)

print('示例2:多维数组实例')
a = np.array([[1,2], [3,4]]) 
 
print ('数组 a：')
print (a)
b = np.array([[11, 12], [13, 14]]) 
 
print ('数组 b：')
print (b)
 
# 内积计算式：
# 1*11+2*12, 1*13+2*14 
# 3*11+4*12, 3*13+4*14
print ('内积：')
print (np.inner(a,b))
print('-'*50)

'''*****************4. numpy.matmul()*********************'''
print('4. numpy.matmul()：')

print('示例1:')
a = [[1,0],[0,1]] 
b = [[4,1],[2,2]] 
print (np.matmul(a,b))
print('-'*25)

print('示例2:维度大于二的数组')
# a:[[[0,1],[2,3]],[[4,5],[6,7]]]
# b:[[[0,1],[2,3]]]
# 对b广播成三维和a对应相乘
# 计算式：
# [[[0*0+1*0,0*1+2*3],[2*0+3*2,2*1+3*3]],[[4*0+5*2,4*1+5*3],[6*0+7*2,6*1+7*3]]]
a = np.arange(8).reshape(2,2,2) 
b = np.arange(4).reshape(2,2) 
print (np.matmul(a,b))
print('-'*50)

'''*****************5. numpy.linalg.det()*********************'''
print('5. numpy.linalg.det()：')

print('示例1:')
a = np.array([[1,2],[3,4]])
print (np.linalg.det(a))
print('-'*25)
print('示例2:')
b = np.array([[6,1,1], [4, -2, 5], [2,8,7]]) 
print (b)
print (np.linalg.det(b))
print (6*(-2*7 - 5*8) - 1*(4*7 - 5*2) + 1*(4*8 - -2*2))
print('-'*50)

'''*****************6. numpy.linalg.inv()*********************'''
print('6. numpy.linalg.inv()：')

print('示例1:')
x = np.array([[1,2],[3,4]]) 
y = np.linalg.inv(x) 
print (x)
print (y)
print (np.dot(x,y))
print('-'*25)

print('示例2:')
a = np.array([[1,1,1],[0,2,5],[2,5,-1]]) 
 
print ('数组 a：')
print (a)
ainv = np.linalg.inv(a) 
 
print ('a 的逆：')
print (ainv)
 
print ('矩阵 b：')
b = np.array([[6],[-4],[27]]) 
print (b)
 
print ('计算：A^(-1)B：')
x = np.linalg.solve(a,b) 
print (x)
# 这就是线性方向 x = 5, y = 3, z = -2 的解
print('-'*50)
