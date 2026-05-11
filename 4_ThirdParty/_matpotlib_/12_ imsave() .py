import matplotlib.pyplot as plt
import numpy as np

'''以下是一个使用 imsave() 方法保存图像的简单实例：'''
# 创建一个二维的图像数据
img_data = np.random.random((100, 100))

# 显示图像
plt.imshow(img_data, cmap='hot')
plt.show()

# 保存图像到磁盘上
plt.imsave('images/matplotlib/保存图片1.png', img_data, cmap='hot')

'''以下实例演示了如何使用 imsave() 方法将一个灰度图像和一幅彩色图像保存到当前目录上：'''
# 创建一幅灰度图像
img_gray = np.random.random((100, 100))

# 创建一幅彩色图像
img_color = np.random.random((100, 100, 3))

# 显示灰度图像
plt.imshow(img_gray, cmap='gray')
plt.show()


# 保存灰度图像到磁盘上
plt.imsave('images/matplotlib/保存图片2.png', img_gray, cmap='gray')

# 显示彩色图像
plt.imshow(img_color)
plt.show()

# 保存彩色图像到磁盘上
plt.imsave('images/matplotlib/保存图片3.jpg', img_color)
