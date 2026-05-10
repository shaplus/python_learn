import numpy as np

'''*****************1. 转置矩阵*********************'''
print('1. 转置矩阵：')

a = np.arange(12).reshape(3,4)
 
print ('原数组：')
print (a)
print ('\n')
 
print ('转置数组：')
print (a.T)
print('-'*50)

'''*****************2. matlib.empty()*********************'''
print('2. matlib.empty()：')

print (np.matlib.empty((2,2)))
# 填充为随机数据
print('-'*50)


'''*****************3. numpy.matlib.zeros()*********************'''
print('3. numpy.matlib.zeros()：')

print (np.matlib.zeros((2,2)))
print('-'*50)

'''*****************4. numpy.matlib.ones()*********************'''
print('4. numpy.matlib.ones()：')

print (np.matlib.ones((2,2)))
print('-'*50)

'''*****************5. numpy.matlib.eye()*********************'''
print('5. numpy.matlib.eye()：')

print (np.matlib.eye(n =  3, M =  4, k =  0, dtype =  float))
print('-'*50)

'''*****************6. numpy.matlib.identity()*********************'''
print('6. numpy.matlib.identity()：')

print (np.matlib.identity(5, dtype =  float))
print('-'*50)

'''*****************7. numpy.matlib.rand()*********************'''
print('7. numpy.matlib.rand()：')

print (np.matlib.rand(3,3))
print('-'*50)

'''*****************8. 矩阵与arrayarray的互换*********************'''
print('8. 矩阵与arrayarray的互换：')

print('示例1:')
i = np.matrix('1,2;3,4')  
print (i)
print('-'*25)

print('示例2:')
j = np.asarray(i)  
print (j)
print('-'*25)

print('示例3:')
k = np.asmatrix (j)  
print (k)
print('-'*25)