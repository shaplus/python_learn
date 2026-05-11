import matplotlib.pyplot as plt

# 以下实例演示了如何使用 imread 函数从一张图像文件中读取图像数据，并将其显示出来：
# 读取图像文件，下载地址：https://static.jyshare.com/images/demo/map.jpeg
img = plt.imread('images/matplotlib/地球图.jpeg')

# 显示图像
plt.imshow(img)
plt.show()

'''
我们可以通过更改 numpy 数组来修改图像。

例如，如果我们将数组乘以一个数 0≤≤1，我们将图像变暗：
'''
# 读取图像文件，下载地址：https://static.jyshare.com/images/mix/tiger.jpeg
img_array = plt.imread('images/matplotlib/tiger.jpeg')
plt.imshow(img_array)
plt.show()
tiger = img_array/255
#print(tiger)

# 显示图像
plt.figure(figsize=(10,6))

for i in range(1,5):
    plt.subplot(2,2,i)
    x = 1 - 0.2*(i-1)
    plt.axis('off') #hide coordinate axes
    plt.title('x={:.1f}'.format(x))
    plt.imshow(tiger*x)

plt.show()

'''以下实例用于裁剪图像：'''
plt.figure(figsize=(6,6))
plt.imshow(tiger[200:500,250:750,:])
plt.axis('off')
plt.show()

'''如果我们将 RGB 颜色的绿色和蓝色坐标的数组元素设置为 0，我们将得到红色的图像：'''
red_tiger = tiger.copy()

red_tiger[:, :,[1,2]] = 0

plt.figure(figsize=(10,10))
plt.imshow(red_tiger)
plt.axis('off')
plt.show()