import matplotlib.pyplot as plt
import matplotlib.markers
import numpy as np

# 以下实例定义了实心圆标记：
ypoints = np.array([1,3,4,5,8,9,6,1,3,4,5,2,4])

plt.plot(ypoints, marker = 'o')
plt.show()

# 以下实例定义了 * 标记：
plt.plot(ypoints, marker = '*')
plt.show()

# 以下实例定义了下箭头：
plt.plot([1, 2, 3], marker=matplotlib.markers.CARETDOWNBASE)
plt.show()

# o:r，o 表示实心圆标记，: 表示虚线，r 表示颜色为红色。
ypoints = np.array([6, 2, 13, 10])

plt.plot(ypoints, 'o:r')
plt.show()

# 设置标记大小：
plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()

# 设置标记内部颜色：
plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
plt.show()

# 自定义标记内部与边框的颜色：
plt.plot(ypoints, marker = 'o', ms = 20, mec = "#302BC1", mfc = "#C229D3")
plt.show()