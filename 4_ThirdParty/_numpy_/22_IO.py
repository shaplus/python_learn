import numpy as np 

'''**************1. numpy.save()***************'''
print('1. numpy.save()')

a = np.array([1,2,3,4,5]) 
 
# 保存到 outfile.npy 文件上
np.save('4_ThirdParty/_numpy_/outfile.npy',a) 
 
# 保存到 outfile2.npy 文件上，如果文件路径末尾没有扩展名 .npy，该扩展名会被自动加上
np.save('4_ThirdParty/_numpy_/outfile2',a)
print('-'*50)

'''**************2. numpy.load()***************'''
print('2. numpy.load()')
b = np.load('4_ThirdParty/_numpy_/outfile.npy')
print(b)
print('-'*50)

'''**************3. np.savez()***************'''
print('3. np.savez()')

a = np.array([[1,2,3],[4,5,6]])
b = np.arange(0, 1.0, 0.1)
c = np.sin(b)
# c 使用了关键字参数 sin_array
np.savez("4_ThirdParty/_numpy_/runoob.npz", a, b, sin_array = c)
r = np.load("4_ThirdParty/_numpy_/runoob.npz")  
print(r.files) # 查看各个数组名称
print(r["arr_0"]) # 数组 a
print(r["arr_1"]) # 数组 b
print(r["sin_array"]) # 数组 c
print('-'*50)

'''**************4. np.savetxt()&np.loadtxt()***************'''
print('4. np.savetxt()&np.loadtxt()')

a = np.array([1,2,3,4,5]) 
np.savetxt('4_ThirdParty/_numpy_/out1.txt',a) 
b = np.loadtxt('4_ThirdParty/_numpy_/out1.txt')  

print(b)
print('-'*25)

print('使用 delimiter 参数：')
a=np.arange(0,10,0.5).reshape(4,-1)
np.savetxt("4_ThirdParty/_numpy_/out2.txt",a,fmt="%d",delimiter=",") # 改为保存为整数，以逗号分隔
b = np.loadtxt("4_ThirdParty/_numpy_/out2.txt",delimiter=",") # load 时也要指定为逗号分隔
print(b)