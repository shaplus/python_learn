import numpy as np

'''*****************1. numpy.amin() 和 numpy.amax()********************'''
# axis = 几，就是把第几个维度压扁，求剩下维度的最小值。
print('1. numpy.amin() 和 numpy.amax()')

a = np.array([[3,7,5],[8,4,3],[2,4,9]])  
print ('我们的数组是：')
print (a)
print ('\n')
print ('调用 amin() 函数：')
print (np.amin(a,1))    # 沿着【列】压缩，求每行的最小值
print ('\n')
print ('再次调用 amin() 函数：')
print (np.amin(a,0))    # 沿着【行】压缩，求每列的最小值
print ('\n')
print ('调用 amax() 函数：')
print (np.amax(a))
print ('\n')
print ('再次调用 amax() 函数：')
print (np.amax(a, axis =  0))    # 沿着【行】压缩，求每列的最大值
print('-'*50)

'''*****************2. numpy.ptp()********************'''
print('2. numpy.ptp()')

a = np.array([[3,7,5],[8,4,3],[2,4,9]])  
print ('我们的数组是：')
print (a)
print ('\n')
print ('调用 ptp() 函数：')
print (np.ptp(a))   # 求整个数组的峰-峰值
print ('\n')
print ('沿轴 1 调用 ptp() 函数：')
print (np.ptp(a, axis =  1))   # 沿着【列】压缩，求每行的峰-峰值
print ('\n')
print ('沿轴 0 调用 ptp() 函数：')
print (np.ptp(a, axis =  0))   # 沿着【行】压缩，求每列的峰-峰值
print('-'*50)

'''*****************3. numpy.percentile()********************'''
print('3. numpy.percentile()')

a = np.array([[10, 7, 4], [3, 2, 1]])
print ('我们的数组是：')
print (a)
 
print ('调用 percentile() 函数：')
# 50% 的分位数，就是 a 里排序之后的中位数
print (np.percentile(a, 50)) 
 
# axis 为 0，在纵列上求
print (np.percentile(a, 50, axis=0)) 
 
# axis 为 1，在横行上求
print (np.percentile(a, 50, axis=1)) 
 
# 保持维度不变
print (np.percentile(a, 50, axis=1, keepdims=True))
print('-'*50)

'''*****************4. numpy.median()********************'''
print('4. numpy.median()')

a = np.array([[30,65,70],[80,95,10],[50,90,60]])  
print ('我们的数组是：')
print (a)
print ('\n')
print ('调用 median() 函数：')
print (np.median(a))
print ('\n')
print ('沿轴 0 调用 median() 函数：')
print (np.median(a, axis =  0))
print ('\n')
print ('沿轴 1 调用 median() 函数：')
print (np.median(a, axis =  1))
print('-'*50)

'''*****************5. numpy.mean()********************'''
print('5. numpy.mean()')

a = np.array([[1,2,3],[3,4,5],[4,5,6]])  
print ('我们的数组是：')
print (a)
print ('\n')
print ('调用 mean() 函数：')
print (np.mean(a))
print ('\n')
print ('沿轴 0 调用 mean() 函数：')
print (np.mean(a, axis =  0))
print ('\n')
print ('沿轴 1 调用 mean() 函数：')
print (np.mean(a, axis =  1))

'''*****************6. numpy.average()********************'''
print('6. numpy.average()')

a = np.array([1,2,3,4])  
print ('我们的数组是：')
print (a)
print ('\n')
print ('调用 average() 函数：')
print (np.average(a))
print ('\n')
# 不指定权重时相当于 mean 函数
wts = np.array([4,3,2,1])  
print ('再次调用 average() 函数：')
print (np.average(a,weights = wts))
print ('\n')
# 如果 returned 参数设为 true，则返回权重的和  
print ('权重的和：')
print (np.average([1,2,3,  4],weights =  [4,3,2,1], returned =  True))
print('-'*25)

print('在多维数组中，可以指定用于计算的轴。')
a = np.arange(6).reshape(3,2)  
print ('我们的数组是：')
print (a)
print ('\n')
print ('修改后的数组：')
wt = np.array([3,5])  
print (np.average(a, axis =  1, weights = wt))
print ('\n')
print ('修改后的数组：')
print (np.average(a, axis =  1, weights = wt, returned =  True))
print('-'*50)

'''*****************7. numpy.std()********************'''
print('7. numpy.std()')

print (np.std([1,2,3,4]))
print('-'*50)

'''*****************8. numpy.var()********************'''
print('8. numpy.var()')

print (np.var([1,2,3,4]))
print('-'*50)

