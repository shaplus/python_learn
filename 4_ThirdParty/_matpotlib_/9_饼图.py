import matplotlib.pyplot as plt
import numpy as np

'''以下实例我们简单实用 pie() 来创建一个饼图:'''
y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show()

'''设置饼图各个扇形的标签与颜色：'''
plt.pie(y,
        labels=['A','B','C','D'], # 设置饼图标签
        colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"], # 设置饼图颜色
       )
plt.title("RUNOOB Pie Test") # 设置标题
plt.show()

'''突出显示第二个扇形，并格式化输出百分比：'''
# 数据
sizes = [15, 30, 45, 10]

# 饼图的标签
labels = ['A', 'B', 'C', 'D']

# 饼图的颜色
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

# 突出显示第二个扇形
explode = (0, 0.1, 0, 0)

# 绘制饼图
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)

# 标题
plt.title("RUNOOB Pie Test")

# 显示图形
plt.show()
# 我们定义了一个包含 4 个元素的列表 sizes，它表示各个类别在总体中所占的比例。
# 然后，我们定义了一个包含 4 个元素的列表 labels，它表示各个类别的标签。
# 接下来，我们定义了一个包含 4 个元素的列表 colors，它表示每个类别的颜色。
# 然后，我们定义了一个包含 4 个元素的元组 explode，它用来指定是否突出某个扇形。
# 接着，我们调用 plt.pie 函数来绘制饼图，其中传入了上述参数。
# 最后，我们添加了一个标题，并调用 plt.show() 来显示图形。

'''示例2'''
y = np.array([35, 25, 25, 15])

plt.pie(y,
        labels=['A','B','C','D'], # 设置饼图标签
        colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"], # 设置饼图颜色
        explode=(0, 0.2, 0, 0), # 第二部分突出显示，值越大，距离中心越远
        autopct='%.2f%%', # 格式化输出百分比
       )
plt.title("RUNOOB Pie Test")
plt.show()