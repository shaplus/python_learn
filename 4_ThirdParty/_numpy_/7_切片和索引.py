import numpy as np

'''****************slice函数*****************'''
print ('示例1：')
a = np.arange(10)
s = slice(2,7,2)   # 从索引 2 开始到索引 7 停止，间隔为2
print (a[s])

'''****************直接索引*****************'''
print ('示例1：')
a = np.arange(10)  
b = a[2:7:2]   # 从索引 2 开始到索引 7 停止，间隔为 2
print(b)

print ('示例2：')
a = np.arange(10)  # [0 1 2 3 4 5 6 7 8 9]
b = a[5] 
print(b)

print ('示例3：')
a = np.arange(10)
print(a[2:])

print ('示例4：')
a = np.arange(10)  # [0 1 2 3 4 5 6 7 8 9]
print(a[2:5])

print ('示例5：')
a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print(a)
# 从某个索引处开始切割
print('从数组索引 a[1:] 处开始切割')
print(a[1:])

print ('示例6：')
a = np.array([[1,2,3],[3,4,5],[4,5,6]])  
print('a =')
print(a)

print('第2列元素：')
print (a[:,1])   # 第2列元素
print('第2行元素：')
print (a[1,:])   # 第2行元素
print('第2列及剩下的所有元素：')
print (a[:,1:])  # 第2列及剩下的所有元素
print('2-3行，2-3列元素：')
print (a[1:3,1:3])  # 2-3行，2-3列元素
