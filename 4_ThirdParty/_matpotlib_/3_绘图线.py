import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([6, 2, 13, 10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()

# 使用简写：
plt.plot(ypoints, ls = '-.')
plt.show()

# 设置线的颜色为红色：
plt.plot(ypoints, color = 'r')
plt.show()

# 设置线的颜色为绿色：
plt.plot(ypoints, c = '#8FBC8F')
plt.show()

# 设置线的颜色为绿色：
plt.plot(ypoints, c = 'SeaGreen')
plt.show()

# 设置线的宽度为 12.5：
plt.plot(ypoints, linewidth = '12.5')
plt.show()

# 绘制多条线：
y1 = np.array([3, 7, 5, 9])
y2 = np.array([6, 2, 13, 10])

plt.plot(y1)
plt.plot(y2)

plt.show()

# 绘制多条线，每个线的 x 坐标不同：
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 7, 5, 9])
x2 = np.array([4, 5, 6, 7])
y2 = np.array([6, 2, 13, 10])

plt.plot(x1, y1, x2, y2)
plt.show()