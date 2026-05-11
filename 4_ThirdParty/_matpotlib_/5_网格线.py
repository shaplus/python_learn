import numpy as np
import matplotlib.pyplot as plt

'''以下实例添加一个简单的网格线，参数使用默认值：'''
x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])


plt.title("RUNOOB grid() Test")
plt.xlabel("x - label")
plt.ylabel("y - label")

plt.plot(x, y)

plt.grid()

plt.show()

'''以下实例添加一个简单的网格线，axis 参数使用 x，设置 x 轴方向显示网格线：'''
plt.title("RUNOOB grid() Test")
plt.xlabel("x - label")
plt.ylabel("y - label")

plt.plot(x, y)

plt.grid(axis='x') # 设置 y 就在轴方向显示网格线

plt.show()

'''以下实例添加一个简单的网格线，参数使用自定义值：'''
plt.title("RUNOOB grid() Test")
plt.xlabel("x - label")
plt.ylabel("y - label")

plt.plot(x, y)

plt.grid(color = 'r', linestyle = '--', linewidth = 0.5)

plt.show()