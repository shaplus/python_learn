import matplotlib.pyplot as plt
import numpy as np

'''以下实例我们简单实用 bar() 来创建一个柱形图:'''

x = np.array(["Runoob-1", "Runoob-2", "Runoob-3", "C-RUNOOB"])
y = np.array([12, 22, 6, 18])

plt.bar(x,y)
plt.show()

'''垂直方向的柱形图可以使用 barh() 方法来设置：'''
plt.barh(x,y)
plt.show()

'''设置柱形图颜色：'''
plt.bar(x, y, color = "#4CAF50")
plt.show()

'''自定义各个柱形的颜色：'''
plt.bar(x, y,  color = ["#FF0048","red","hotpink","#556B2F"])
plt.show()

'''设置柱形图宽度，bar() 方法使用 width 设置，barh() 方法使用 height 设置 height'''
plt.bar(x, y, width = 0.9)
plt.show()