import numpy as np

'''*********************修改数组维度**********************'''
print('修改数组维度')

'''1. numpy.broadcast()'''
print('1. numpy.broadcast()')

print('示例1：基本广播操作')
x = np.array([[1], [2], [3]])  # 形状: (3, 1)
y = np.array([4, 5, 6])        # 形状: (3,)

# 创建广播对象
b = np.broadcast(x, y)

print("x 的形状:", x.shape)
print("y 的形状:", y.shape)
print("广播后的形状:", b.shape)  # (3, 3)
print('-----------------')

print('示例2：使用迭代器')
# 工作原理：
# r 迭代器遍历广播后的 x：[[1,1,1], [2,2,2], [3,3,3]]
# c 迭代器遍历广播后的 y：[[4,5,6], [4,5,6], [4,5,6]]
b = np.broadcast(x, y)
r, c = b.iters  # 获取两个迭代器

print(next(r), next(c))  # 1 4
print(next(r), next(c))  # 1 5
print('-----------------')

print('示例3：手动实现广播相加')
b = np.broadcast(x, y)
c = np.empty(b.shape)      # 创建空数组
c.flat = [u + v for u, v in b]  # 使用 flat 属性填充

print("手动广播相加结果:")
print(c)

print("\nNumPy 自动广播结果:")
print(x + y)
print('----------------------------------')

'''2. numpy.broadcast_to()'''
print('2. numpy.broadcast_to()')

a = np.arange(4).reshape(1,4)
 
print ('原数组：')
print (a)
print ('\n')
 
print ('调用 broadcast_to 函数之后：')
print (np.broadcast_to(a,(4,4)))
print('----------------------------------')

'''3. numpy.expand_dims()'''
print('3. numpy.expand_dims()')

x = np.array(([1,2],[3,4]))
 
print ('数组 x：')
print (x)
print ('\n')
y = np.expand_dims(x, axis = 0)
 
print ('数组 y：')
print (y)
print ('\n')
 
print ('数组 x 和 y 的形状：')
print (x.shape, y.shape)
print ('\n')
# 在位置 1 插入轴
y = np.expand_dims(x, axis = 1)
 
print ('在位置 1 插入轴之后的数组 y：')  # (2, 2) (2, 1, 2)
print (y)

# 查看数组 x 和 y 的维度
print ('x.ndim 和 y.ndim：')
print (x.ndim,y.ndim)

# 查看数组 x 和 y 的形状
print ('x.shape 和 y.shape：')
print (x.shape, y.shape)
print('----------------------------------')

'''4. numpy.squeeze()'''
print('4. numpy.squeeze()')

x = np.arange(9).reshape(1,3,3)
 
print ('数组 x：')
print (x)
print ('\n')
y = np.squeeze(x, axis = 0)
 
print ('数组 y：')
print (y)
print ('\n')
 
print ('数组 x 和 y 的形状：')
print (x.shape, y.shape)

