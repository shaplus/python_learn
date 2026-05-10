import numpy as np

'''*****************1. 无复制*********************'''
print('1. 无复制：')

a = np.arange(6)  
print ('我们的数组是：')
print (a)
print ('调用 id() 函数：')
print (id(a))
print ('a 赋值给 b：')
b = a 
print (b)
print ('b 拥有相同 id()：')
print (id(b))
print ('修改 b 的形状：')
b.resize(3,2)
print (b)
print ('a 的形状也修改了：')
print (a)
print('-'*50)

'''*****************2. 视图或浅拷贝*********************'''
print('2. 视图或浅拷贝：')

print('新数组的维数变化不会改变原始数据的维数：')
# 最开始 a 是个 3X2 的数组
a = np.arange(6).reshape(3,2)  
print ('数组 a：')
print (a)
print ('创建 a 的视图：')
b = a.view()  
print (b)
print ('两个数组的 id() 不同：')
print ('a 的 id()：')
print (id(a))
print ('b 的 id()：' )
print (id(b))
# 修改 b 的形状，并不会修改 a
b.resize(2,3)
print ('b 的形状：')
print (b)
print ('a 的形状：')
print (a)
print('-'*25)

print('使用切片创建视图修改数据会影响到原始数组：')
arr = np.arange(12)
print ('我们的数组：')
print (arr)
print ('创建切片：')
a=arr[3:]
b=arr[3:]
a[1]=123
b[2]=234
print(arr)
print(id(a),id(b),id(arr[3:]))
# 变量 a,b 都是 arr 的一部分视图，对视图的修改会直接反映到原数据中。
# 但是我们观察 a,b 的 id，他们是不同的，
# 也就是说，视图虽然指向原数据，但是他们和赋值引用还是有区别的。
print('-'*50)

'''*****************3. 副本或深拷贝*********************'''
print('3. 副本或深拷贝：')

# ndarray.copy() 函数创建一个副本。 
# 对副本数据进行修改，不会影响到原始数据，它们物理内存不在同一位置。

a = np.array([[10,10],  [2,3],  [4,5]])  
print ('数组 a：')
print (a)
print ('创建 a 的深层副本：')
b = a.copy()  
print ('数组 b：')
print (b)
# b 与 a 不共享任何内容  
print ('我们能够写入 b 来写入 a 吗？')
print (b is a)
print ('修改 b 的内容：')
b[0,0]  =  100  
print ('修改后的数组 b：')
print (b)
print ('a 保持不变：')
print (a)
