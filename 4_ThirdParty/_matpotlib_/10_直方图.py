import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


'''以下实例我们简单实用 hist() 来创建一个直方图:'''
# 生成一组随机数据
data = np.random.randn(1000)    # 生成 1000 个服从标准正态分布的随机数

# 绘制直方图
plt.hist(data, bins=30, color='skyblue', alpha=0.8)

# 设置图表属性
plt.title('RUNOOB hist() Test')
plt.xlabel('Value')
plt.ylabel('Frequency')

# 显示图表
plt.show()

'''以下实例演示了如何使用 hist() 函数绘制多个数据组的直方图，并进行比较：'''
# 生成三组随机数据
data1 = np.random.normal(0, 1, 1000)    # 生成 1000 个服从标准正态分布的随机数
data2 = np.random.normal(2, 1, 1000)    # 生成 1000 个服从 N(2, 1) 正态分布的随机数
data3 = np.random.normal(-2, 1, 1000)    # 生成 1000 个服从 N(-2, 1) 正态分布的随机数

# 绘制直方图
plt.hist(data1, bins=30, alpha=0.5, label='Data 1')
plt.hist(data2, bins=30, alpha=0.5, label='Data 2')
plt.hist(data3, bins=30, alpha=0.5, label='Data 3')

# 设置图表属性
plt.title('RUNOOB hist() TEST')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()

# 显示图表
plt.show()
# 以上实例中我们生成了三组不同的随机数据，并使用 hist() 函数绘制了它们的直方图。
# 通过设置不同的均值和标准差，我们可以生成具有不同分布特征的随机数据。
# 我们设置了 bins 参数为 30，这意味着将数据范围分成 30 个等宽的区间，然后统计每个区间内数据的频数。
# 我们设置了 alpha 参数为 0.5，这意味着每个直方图的颜色透明度为 50%。
# 我们使用 label 参数设置了每个直方图的标签，以便在图例中显示。
# 然后使用 legend() 函数显示图例。最后，我们使用 title()、xlabel() 和 ylabel() 函数设置了图表的标题和坐标轴标签。

'''结合 Pandas'''
'''以下实例我们结合 Pandas 来绘制直方图：'''
# 使用 NumPy 生成随机数
random_data = np.random.normal(170, 10, 250)
 
# 将数据转换为 Pandas DataFrame
dataframe = pd.DataFrame(random_data)
 
# 使用 Pandas hist() 方法绘制直方图
dataframe.hist()    # 本质上是pandas调用了 matplotlib.hist() 函数


# 设置图表属性
plt.title('RUNOOB hist() Test')
plt.xlabel('X-Value')
plt.ylabel('Y-Value')

# 显示图表
plt.show()

'''除了数据框之外，您还可以使用 Pandas 中的 Series 对象绘制直方图。只需将数据框中的列替换为 Series 对象即可。'''
# 生成随机数据
data = pd.Series(np.random.normal(size=100))

# 绘制直方图
# bins 参数指定了直方图中的柱子数量
plt.hist(data, bins=10)

# 设置图形标题和坐标轴标签
plt.title('RUNOOB hist() Tes')
plt.xlabel('X-Values')
plt.ylabel('Y-Values')

# 显示图形
plt.show()

