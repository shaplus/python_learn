import numpy as np

'''----------------1. numpy.asarray----------------'''
'''
numpy.asarray(a, dtype = None, order = None)
'''
print('1. numpy.asarray')

'''将列表转换为 ndarray'''
print('将列表转换为 ndarray')
x =  [1,2,3] 
a = np.asarray(x)  
print (a)
print('----------------')

'''将元组转换为 ndarray'''
print('将元组转换为 ndarray')
x =  (1,2,3) 
a = np.asarray(x)  
print (a)
print('----------------')

'''将多维数组转换为 ndarray'''
print('将多维数组转换为 ndarray')
print(1)
x =  [[1,2,3],[4,5,6]]
a = np.asarray(x)  
print (a)

print(2)
x =  [(1,2),(4,5)] 
a = np.asarray(x)  
print (a)
print('----------------')

'''设置了 dtype 参数'''
print('设置了 dtype 参数')
x =  [1,2,3] 
a = np.asarray(x, dtype =  float)  
print (a)
print('--------------------------------')

'''----------------2. numpy.frombuffer----------------'''
'''
numpy.frombuffer 用于实现动态数组。
numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)
'''
print('2. numpy.frombuffer')

s =  b'Hello World ' 
a = np.frombuffer(s, dtype =  'S2')  
print (a)
a = a.reshape(2,3)
print (a)
print('--------------------------------')

'''----------------3. numpy.fromiter----------------'''
'''
numpy.fromiter 方法从可迭代对象中建立 ndarray 对象，返回一维数组。
numpy.fromiter(iterable, dtype, count=-1)
'''
print('3. numpy.fromiter')
# 使用 range 函数创建列表对象  
list=range(5)
it=iter(list)
 
# 使用迭代器创建 ndarray 
x=np.fromiter(it, dtype=float)
print(x)
print('--------------------------------')