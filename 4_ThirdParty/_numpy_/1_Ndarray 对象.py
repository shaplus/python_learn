import numpy as np 

'''创建 ndarray 对象'''
print('创建 ndarray 对象')
a = np.array([1,2,3])  
print(a)    # [1 2 3]
print('-----------------')

'''多于一个维度的 ndarray 对象'''
print('多于一个维度的 ndarray 对象')
a = np.array([[1,2,3],[4,5,6]])
print(a)    # [[1 2 3]
#  [4 5 6]]
print('-----------------')

'''指定最小维度'''
print('指定最小维度')
a = np.array([1, 2, 3, 4, 5], ndmin =  3)  
print (a)    # [[[1 2 3 4 5]]]
print('-----------------')

'''dtype 参数'''
print('dtype 参数')
a = np.array([1, 2, 3, 4, 5], dtype = np.float32)  
print (a)    # [1. 2. 3. 4. 5.]
print('-----------------')
