import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family']=['STFangsong']

'''*********************subplot() **************************'''
'''以下实例绘制了两个子图：'''
#plot 1:
xpoints = np.array([0, 6])
ypoints = np.array([0, 100])

plt.subplot(1, 2, 1)
plt.plot(xpoints,ypoints)
plt.title("plot 1")

#plot 2:
x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("plot 2")

plt.suptitle("RUNOOB subplot Test")
plt.show()

'''以下实例绘制了四个子图：'''
#plot 1:
x = np.array([0, 6])
y = np.array([0, 100])

plt.subplot(2, 2, 1)
plt.plot(x,y)
plt.title("plot 1")

#plot 2:
x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])

plt.subplot(2, 2, 2)
plt.plot(x,y)
plt.title("plot 2")

#plot 3:
x = np.array([1, 2, 3, 4])
y = np.array([3, 5, 7, 9])

plt.subplot(2, 2, 3)
plt.plot(x,y)
plt.title("plot 3")

#plot 4:
x = np.array([1, 2, 3, 4])
y = np.array([4, 5, 6, 7])

plt.subplot(2, 2, 4)
plt.plot(x,y)
plt.title("plot 4")

plt.suptitle("RUNOOB subplot Test")
plt.show()

'''*********************subplots() **************************'''

'''创建一个画像和子图'''
fig, ax = plt.subplots()
fig.suptitle("subplots() Test1")

x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

ax.plot(x, y)
ax.set_title('Simple plot')
plt.show()

'''以下实例绘制了 2x2 的子图网格：'''
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
fig.suptitle("subplots() Test2")

# 生成数据
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(x)

# 在不同子图中绘图
axs[0, 0].plot(x, y1)
axs[0, 0].set_title('sin(x)')

axs[0, 1].plot(x, y2)
axs[0, 1].set_title('cos(x)')

axs[1, 0].plot(x, y3)
axs[1, 0].set_title('tan(x)')

axs[1, 1].plot(x, y4)
axs[1, 1].set_title('exp(x)')

plt.tight_layout()
plt.show()

'''创建两个子图'''
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
f.suptitle("subplots() Test3")

ax1.plot(x, y1)
ax1.set_title('Sharing Y axis')
ax2.plot(x, y2)
plt.show()

'''更改图表的编号'''
fig, ax = plt.subplots(num=8, clear=True)
fig.suptitle("subplots() Test4")

ax.plot(x, y1)
ax.set_title('figure 8')
plt.show()

'''========== sharex 和 sharey 参数示例 =========='''
# 示例1: sharex=True 和 sharey=True - 所有子图共享x轴和y轴
fig, axs = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(10, 6))
fig.suptitle('sharex=True, sharey=True (所有子图共享坐标轴)')

x = np.linspace(0, 2*np.pi, 100)
axs[0, 0].plot(x, np.sin(x))
axs[0, 0].set_title('sin(x)')

axs[0, 1].plot(x, np.cos(x))
axs[0, 1].set_title('cos(x)')

axs[1, 0].plot(x, np.sin(2*x))
axs[1, 0].set_title('sin(2x)')

axs[1, 1].plot(x, np.cos(2*x))
axs[1, 1].set_title('cos(2x)')

plt.tight_layout()
plt.show()

# 示例2: sharex='col' - 每列共享x轴
fig, axs = plt.subplots(2, 2, sharex='col', figsize=(10, 6))
fig.suptitle('sharex="col" (每列共享X轴)')

axs[0, 0].plot(x, np.sin(x))
axs[0, 0].set_title('sin(x)')

axs[0, 1].plot(x*2, np.cos(x))  # 第二列使用不同的x范围
axs[0, 1].set_title('cos(x) with x*2')

axs[1, 0].plot(x, np.sin(2*x))
axs[1, 0].set_title('sin(2x)')

axs[1, 1].plot(x*2, np.cos(2*x))
axs[1, 1].set_title('cos(2x) with x*2')

plt.tight_layout()
plt.show()

# 示例3: sharey='row' - 每行共享y轴
fig, axs = plt.subplots(2, 2, sharey='row', figsize=(10, 6))
fig.suptitle('sharey="row" (每行共享Y轴)')

axs[0, 0].plot(x, np.sin(x))
axs[0, 0].set_title('sin(x)')

axs[0, 1].plot(x, np.cos(x)*2)  # 第一行共享y轴
axs[0, 1].set_title('cos(x)*2')

axs[1, 0].plot(x, np.exp(x)*0.1)  # 第二行共享y轴
axs[1, 0].set_title('exp(x)*0.1')

axs[1, 1].plot(x, np.tan(x)*0.1)
axs[1, 1].set_title('tan(x)*0.1')

plt.tight_layout()
plt.show()
