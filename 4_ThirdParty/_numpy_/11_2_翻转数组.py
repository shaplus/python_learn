import numpy as np

'''*********************翻转数组**********************'''
print('翻转数组')

'''1. numpy.transpose()'''
print('1. numpy.transpose()')

a = np.arange(12).reshape(3,4)
 
print ('原数组：')
print (a )
print ('\n')
 
print ('对换数组：')
print (np.transpose(a))
print('-----------------')

'''2. numpy.ndarray.T'''
print('2. numpy.ndarray.T')

a = np.arange(12).reshape(3,4)
 
print ('原数组：')
print (a)
print ('\n')
 
print ('转置数组：')
print (a.T)
print('-----------------')

'''3. numpy.rollaxis()'''
print('3. numpy.rollaxis()')

print('示例1：')
# 创建了三维的 ndarray
a = np.arange(8).reshape(2,2,2)
 
print ('原数组：')
print (a)
print ('获取数组中一个值：')
print(np.where(a==6))   
print(a[1,1,0])  # 为 6
print ('\n')
 
 
# 将轴 2 滚动到轴 0（宽度到深度）
 
print ('调用 rollaxis 函数：')
b = np.rollaxis(a,2,0)
print (b)
# 查看元素 a[1,1,0]，即 6 的坐标，变成 [0, 1, 1]
# 最后一个 0 移动到最前面
print(np.where(b==6))   
print ('\n')
 
# 将轴 2 滚动到轴 1：（宽度到高度）
 
print ('调用 rollaxis 函数：')
c = np.rollaxis(a,2,1)
print (c)
# 查看元素 a[1,1,0]，即 6 的坐标，变成 [1, 0, 1]
# 最后的 0 和 它前面的 1 对换位置
print(np.where(c==6))   
print ('\n')
print('-----------------')

print('示例2：')
arr = np.random.rand(2,3,4,5)  # (2,3,4,5)
print(arr.shape)

res = np.rollaxis(arr, axis=0, start=3)
print(res.shape)  # (2,4,5,3)
print('-----------------')

'''4. numpy.moveaxis()'''
print('4. numpy.moveaxis()')

print('示例1：')
print('将轴 1 移动到轴 3：')
arr = np.random.rand(2,3,4,5)  # (2,3,4,5)
print(arr.shape)

# 轴1到轴3，移动后( , , ,3)，其他轴自动挤开，相对顺序不变,移动后(2,4,5,3)
res = np.moveaxis(arr, source=1, destination=3)
print(res.shape)  # (2,4,5,3)
print('-----------------')

print('示例2：')
print('一次移动多个轴：')

arr = np.random.rand(2,3,4,5)  # (2,3,4,5)
print(arr.shape)

# 轴0到轴3，轴2到轴1，移动后( ,4, ,2)，其他轴自动挤开，相对顺序不变,移动后(3,4,5,2)
res = np.moveaxis(arr, [0,2], [3,1])
print(res.shape)  # (3,4,5,2)
print('-----------------')

'''5. numpy.swapaxes()'''
print('5. numpy.swapaxes()')

arr = np.random.rand(2,3,4,5)  # (2,3,4,5)
print(arr.shape)

# 交换轴 0 和轴 2
res = np.swapaxes(arr, 0, 2)
print(res.shape)  # (4,3,2,5)
print('-----------------')
