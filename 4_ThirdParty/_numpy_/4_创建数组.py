import numpy as np
'''----------------1. numpy.empty----------------'''
'''
numpy.empty 方法用来创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组：
注意： 数组元素为随机值，因为它们未初始化。
'''
print('1. numpy.empty')

a = np.empty((3,2), dtype = float, order = 'C')
print(a)
print('----------------------------------')

'''----------------2. numpy.zeros----------------'''
'''
创建指定大小的数组，数组元素以 0 来填充
'''
print('2. numpy.zeros')

'''默认为浮点数'''
print('默认为浮点数')
x = np.zeros(5) 
print(x)
 
'''设置类型为整数'''
print('设置类型为整数')
y = np.zeros((5,), dtype = int) 
print(y)
 
'''自定义类型'''
print('自定义类型')
z = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')])  
print(z)
print('----------------------------------')

'''----------------3. numpy.ones----------------'''
'''
创建指定形状的数组，数组元素以 1 来填充：
numpy.ones(shape, dtype = None, order = 'C')
'''
print('3. numpy.ones')

'''默认为浮点数'''
print('默认为浮点数')
x = np.ones(5) 
print(x)
 
'''自定义类型'''
print('自定义类型')
x = np.ones([2,2], dtype = int)
print(x)
print('----------------------------------')

'''----------------4. numpy.zeros_like----------------'''
'''
numpy.zeros_like 用于创建一个与给定数组具有相同形状的数组，数组元素以 0 来填充。
numpy.zeros_like(a, dtype=None, order='K', subok=True, shape=None)
'''
print('4. numpy.zeros_like')

# 创建一个 3x3 的二维数组
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
 
# 创建一个与 arr 形状相同的，所有元素都为 0 的数组
zeros_arr = np.zeros_like(arr)
print(zeros_arr)
print('----------------------------------')

'''----------------5. numpy.ones_like----------------'''
'''
参考 4. numpy.zeros_like
numpy.ones_like(a, dtype=None, order='K', subok=True, shape=None)
'''
print('5. numpy.ones_like')

# 创建一个 3x3 的二维数组
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
 
# 创建一个与 arr 形状相同的，所有元素都为 1 的数组
ones_arr = np.ones_like(arr)
print(ones_arr)
print('----------------------------------')
