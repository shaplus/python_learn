import numpy as np

'''********************广播(Broadcast)********************'''
print('广播(Broadcast)：')

print('示例1：')
a = np.array([1,2,3,4]) 
b = np.array([10,20,30,40]) 
c = a * b 
print (c)
print('-----------------')

print('示例2：')
# 当运算中的 2 个数组的形状不同时，numpy 将自动触发广播机制。如：
a = np.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])
b = np.array([0,1,2])
print(a + b)
print('-----------------')

print('示例3：')
# 4x3 的二维数组与长为 3 的一维数组相加，等效于把数组 b 在二维上重复 4 次再运算：
a = np.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])
b = np.array([1,2,3])
bb = np.tile(b, (4, 1))  # 重复 b 的各个维度
print(bb)
print(a + bb)
print(a + b)    # 等价于 a + np.tile(b, (4, 1))
print('-----------------')
