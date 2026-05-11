import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# 显示灰度图像
# 生成一个二维随机数组
img = np.random.rand(10, 10)

# 绘制灰度图像
plt.imshow(img, cmap='gray')

# 显示图像
plt.show()

'''显示彩色图像'''
# 生成一个随机的彩色图像
img = np.random.rand(10, 10, 3)

# 绘制彩色图像
plt.imshow(img)

# 显示图像
plt.show()
# 以上实例中我们生成了一个 10x10 的随机彩色图像，并使用 imshow() 函数将其显示出来。
# 由于彩色图像是三维数组，因此不需要设置 cmap 参数。

'''显示热力图'''
# 生成一个二维随机数组
data = np.random.rand(10, 10)

# 绘制热力图
plt.imshow(data, cmap='hot')

# 显示图像
plt.colorbar()
plt.show()

'''显示地图'''
# 加载地图图像, 下载地址：https://static.jyshare.com/images/demo/map.jpeg
img = Image.open('images/matplotlib/地球图.jpeg')

# 转换为数组
data = np.array(img)

# 绘制地图
plt.imshow(data)

# 隐藏坐标轴
plt.axis('off')

# 显示图像
plt.show()
# 以上实例中我们加载了一张地图图像，并将其转换为数组。
# 然后，我们使用 imshow() 函数将其显示出来，并使用 axis('off') 函数隐藏了坐标轴，以便更好地查看地图。

'''显示矩阵'''
# 生成一个随机矩阵
data = np.random.rand(10, 10)

# 绘制矩阵
plt.imshow(data)

# 显示图像
plt.show()

'''
以下创建了一个 4x4 的二维 numpy 数组，并对其进行了三种不同的 imshow 图像展示。

第一张展示了灰度的色彩映射方式，并且没有进行颜色的混合（blending）。
第二张展示了使用viridis颜色映射的图像，同样没有进行颜色的混合。
第三张展示了使用viridis颜色映射的图像，并且使用了双立方插值方法进行颜色混合。
'''
n = 4

# 创建一个 n x n 的二维numpy数组
a = np.reshape(np.linspace(0,1,n**2), (n,n))

plt.figure(figsize=(12,4.5))

# 第一张图展示灰度的色彩映射方式，并且没有进行颜色的混合
plt.subplot(131)
plt.imshow(a, cmap='gray', interpolation='nearest')
plt.xticks(range(n))
plt.yticks(range(n))
# 灰度映射，无混合
plt.title('Gray color map, no blending', y=1.02, fontsize=12)

# 第二张图展示使用viridis颜色映射的图像，同样没有进行颜色的混合
plt.subplot(132)
plt.imshow(a, cmap='viridis', interpolation='nearest')
plt.yticks([])
plt.xticks(range(n))
# Viridis映射，无混合
plt.title('Viridis color map, no blending', y=1.02, fontsize=12)

# 第三张图展示使用viridis颜色映射的图像，并且使用了双立方插值方法进行颜色混合
plt.subplot(133)
plt.imshow(a, cmap='viridis', interpolation='bicubic')
plt.yticks([])
plt.xticks(range(n))
# Viridis 映射，双立方混合
plt.title('Viridis color map, bicubic blending', y=1.02, fontsize=12)

plt.show()