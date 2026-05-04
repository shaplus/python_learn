import numpy as np 

'''---------------1. ndarray.ndim----------------'''
'''
数组的秩（rank），即数组的维度数量或轴的数量。
'''
print('1. ndarray.ndim')

'''一个一维数组的秩为1'''
a = np.arange(24)  
print ('a.ndim =', a.ndim)             # a 现只有一个维度

'''一个三维数组的秩为3'''
# 现在调整其大小
b = a.reshape(2,4,3)  # b 现在拥有三个维度
print ('b.ndim =', b.ndim)             # b 现在有三个维度
print('----------------------------------')

'''----------------2. ndarray.shape----------------'''
'''
数组的维度，表示数组在每个轴上的大小。对于二维数组（矩阵），表示其行数和列数。
# 输出元组顺序是高维到低维
'''
print('2. ndarray.shape')

'''打印一个三维数组的形状'''
print('打印一个三维数组的形状')
a = np.array([[[1,2,3,4],[4,5,6,7],[7,8,9,10]],[[1,2,3,4],[4,5,6,7],[7,8,9,10]]])  
print ('a.shape =', a.shape)
print('-----------------')

'''调整数组大小的三种方法'''
'''
a.shape =  (3,2)  直接赋值被弃用
'''
print('调整数组大小的三种方法：')
# 1. 使用 reshape 对象方法
a = np.array([[1,2,3],[4,5,6]]) 
a = a.reshape(3,2)
print('a = a.reshape(3,2)')
print (a)

# 2. 使用 resize 方法
a = np.array([[1,2,3],[4,5,6]]) 
a.resize((3,2), refcheck=False)
print('a.resize((3,2), refcheck=False)')
print (a)

# 3. 使用 reshape 类方法
np.reshape(a, (3,2))
print('np.reshape(a, (3,2))')
print (a)
print('-----------------')

'''reshape 的特性'''
'''
ndarray.reshape 通常返回的是非拷贝副本，即改变返回后数组的元素，原数组对应元素的值也会改变。
'''
print('reshape 的特性')
a=np.array([[1,2,3],[4,5,6]])
b=a.reshape((6,))
print('a =\n', a)
print('b =\n', b)
print('改变b[0] = 666')
b[0] = 666
print('改变后的a =\n', a)
print('改变后的b =\n', b)
print('----------------------------------')

'''----------------3. ndarray.itemsize----------------'''
'''
ndarray.itemsize 以字节的形式返回数组中每一个元素的大小。
数组中每个元素占用字节数。
例如，一个元素类型为 float64 的数组 itemsize 属性值为 8
(float64 占用 64 个 bits，每个字节长度为 8，所以 64/8，占用 8 个字节），
又如，一个元素类型为 complex32 的数组 itemsize 属性值为 4（32/8）。
'''
print('3. ndarray.itemsize')
x = np.array([1,2,3,4,5], dtype = np.int8)  
print ('x.itemsize =', x.itemsize)
 
# 数组的 dtype 现在为 float64（八个字节） 
y = np.array([1,2,3,4,5], dtype = np.float64)  
print ('y.itemsize =', y.itemsize)
print('----------------------------------')

'''----------------4. ndarray.flags----------------'''
print('4. ndarray.flags')
x = np.array([1,2,3,4,5])  
print('x.flags =')
print (x.flags)
print('-----------------')

'''改变ndarray.flags的属性'''
'''
虽然把 a.flags.writeable 改为了 False（只读），但是在数组 b 上的操作仍然会影响数组 a，
因为数组 a 和数组 b 共享底层的数据缓冲区。这是由于 reshape 操作不会创建新的数据副本，
而是使用相同的数据，只是以新的形状进行解释。
'''
print('改变ndarray.flags的属性')
a = np.array([[1, 2, 3], [4, 5, 6]])
b = a.reshape((3, 2))
print('a =\n', a)
print('b =\n', b)
a.flags.writeable = False
print('改变b[0][0] = 666')
b[0][0] = 666
print('改变后的a =\n', a)
print('改变后的b =\n', b)
print('a.flags =\n', a.flags)
print('----------------------------------')