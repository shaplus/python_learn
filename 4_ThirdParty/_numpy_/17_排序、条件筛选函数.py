from matplotlib.pylab import f
import numpy as np  

'''*****************1. numpy.sort()******************'''
print('1. numpy.sort()')

a = np.array([[3,7],[9,1]])  
print ('我们的数组是：')
print (a)
print ('\n')
print ('调用 sort() 函数：')
print (np.sort(a))
print ('\n')
print ('按列排序：')
print (np.sort(a, axis =  0))
print ('\n')
# 在 sort 函数中排序字段 
dt = np.dtype([('name',  'S10'),('age',  int)]) 
a = np.array([("raju",21),("anil",25),("ravi",  17),  ("amar",27)], dtype = dt)  
print ('我们的数组是：')
print (a)
print ('\n')
print ('按 name 排序：')
print (np.sort(a, order =  'name'))
print ('-'*50)

'''*****************2. numpy.argsort()******************'''
print('2. numpy.argsort()')

x = np.array([3,  1,  2])  
print ('我们的数组是：')
print (x)
print ('\n')
print ('对 x 调用 argsort() 函数：')
y = np.argsort(x)  
print (y)
print ('\n')
print ('以排序后的顺序重构原数组：')
print (x[y])
print ('\n')
print ('使用循环重构原数组：')
for i in y:  
    print (x[i], end=" ")
print ('\n')
print ('-'*50)

'''*****************3. numpy.lexsort()******************'''
print('3. numpy.lexsort()')

nm =  (1,1,2,2)
dv =  ('3',  '4', '3', '4') 
ind = np.lexsort((dv,nm))  
print ('调用 lexsort() 函数：') 
print (ind) 
print ('\n') 
print ('使用这个索引来获取排序后的数据：') 
print ([f'{nm[i]} {dv[i]}'  for i in ind])
print ('-'*50)

'''*****************4. msort、sort_complex、partition、argpartition******************'''
print('4. msort、sort_complex、partition、argpartition')

'''复数排序：sort_complex()'''
print('复数排序：sort_complex()')

print (np.sort_complex([5, 3, 6, 2, 1]))
print (np.sort_complex([1 + 2j, 2 - 1j, 3 - 2j, 3 - 3j, 3 + 5j]))
print ('-'*25)

'''分区排序：partition()'''
print('分区排序：partition()')

a = np.array([8, 6, 5, 7])
# 把数组中 第 2 小 的元素，放到索引 2 的位置
# 并且保证：
# 左边所有元素 ≤ 它
# 右边没有元素（因为是最后一位）
# 从第 0 个元素开始
print (np.partition(a, 2))
# 用第 1 小和第 3 小的元素，对数组进行分区
# 从第 0 个元素开始
print (np.partition(a, (1, 3)))
print ('-'*25)

'''分区排序：argpartition()'''
print('分区排序：argpartition()')

# 找到数组的第 3 小（index=2）的值和第 2 大（index=-2）的值
print ('找到数组的第 3 小（index=2）的值和第 2 大（index=-2）的值：')
arr = np.array([46, 57, 23, 39, 1, 10, 0, 120])
print (arr[np.argpartition(arr, 2)[2]])
print (arr[np.argpartition(arr, -2)[-2]])

# 同时找到第 3 和第 4 小的值。注意这里，用 [2,3] 同时将第 3 和第 4 小的排序好，然后可以分别通过下标 [2] 和 [3] 取得。
print ('同时找到第 3 和第 4 小的值：')
print (arr[np.argpartition(arr, [2,3])[2]])
print (arr[np.argpartition(arr, [2,3])[3]])
print ('-'*50)

'''*****************5. numpy.argmax() 和 numpy.argmin()******************'''
print('5. numpy.argmax() 和 numpy.argmin()')

a = np.array([[30,40,70],[80,20,10],[50,90,60]])  
print  ('我们的数组是：') 
print (a) 
print ('\n') 
print ('调用 argmax() 函数：') 
print (np.argmax(a)) 
print ('\n') 
print ('展开数组：') 
print (a.flatten()) 
print ('\n') 
print ('沿轴 0 的最大值索引：') 
maxindex = np.argmax(a, axis =  0)  
print (maxindex) 
print ('\n') 
print ('沿轴 1 的最大值索引：') 
maxindex = np.argmax(a, axis =  1)  
print (maxindex) 
print ('\n') 
print ('调用 argmin() 函数：') 
minindex = np.argmin(a)  
print (minindex) 
print ('\n') 
print ('展开数组中的最小值：') 
print (a.flatten()[minindex]) 
print ('\n') 
print ('沿轴 0 的最小值索引：') 
minindex = np.argmin(a, axis =  0)  
print (minindex) 
print ('\n') 
print ('沿轴 1 的最小值索引：') 
minindex = np.argmin(a, axis =  1)  
print (minindex)
print ('-'*50)

'''*****************6. numpy.nonzero()******************'''
print('6. numpy.nonzero()')

a = np.array([[30,40,0],[0,20,10],[50,0,60]])  
print ('我们的数组是：')
print (a)
print ('\n')
print ('调用 nonzero() 函数：')
print (np.nonzero (a))
print ('-'*50)

'''*****************7. numpy.where()******************'''
print('7. numpy.where()')

x = np.arange(9.).reshape(3,  3)  
print ('我们的数组是：')
print (x)
print ( '大于 3 的元素的索引：')
y = np.where(x >  3)  
print (y)
print ('使用这些索引来获取满足条件的元素：')
print (x[y])
print ('-'*50)

'''*****************8. numpy.extract()******************'''
print('8. numpy.extract()')

x = np.arange(9.).reshape(3,  3)  
print ('我们的数组是：')
print (x)
# 定义条件, 选择偶数元素
condition = np.mod(x,2)  ==  0  
print ('按元素的条件值：')
print (condition)
print ('使用条件提取元素：')
print (np.extract(condition, x))