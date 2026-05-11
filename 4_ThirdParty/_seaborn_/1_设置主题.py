import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

'''默认主题'''
# 使用默认主题
sns.set_theme()

# 创建简单数据
np.random.seed(42)
data = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100)
})

# 绘制图表
sns.scatterplot(x='x', y='y', data=data)
plt.title('Simple Scatter Plot')
plt.show()



'''自定义主题1'''
# 设置主题和颜色调色板
sns.set_theme(style="darkgrid", palette="pastel")
# 示例数据
products = ["Product A", "Product B", "Product C", "Product D"]
sales = [120, 210, 150, 180]

# 创建柱状图
sns.barplot(x=products, y=sales)

# 添加标签和标题
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Product Sales by Category")

# 显示图表
plt.show()



'''自定义主题2'''
# 设置深色网格风格，配明亮调色板
sns.set_theme(
    style='darkgrid',
    palette='bright',
    font='sans-serif',
    font_scale=1.2,
    rc={'figure.figsize': (12, 8)}
)

# 创建简单分类数据
data = pd.DataFrame({
    'category': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'value': [1, 2, 3, 4, 5, 6, 7, 8, 9]
})

# 绘制图表
sns.boxplot(x='category', y='value', data=data)
plt.title('Value Distribution by Category')
plt.show()

'''使用不同的 context'''
# 创建数据
np.random.seed(42)
data = pd.DataFrame({
    'x': np.arange(20),
    'y': np.random.randn(20).cumsum()
})

# 演示 paper 上下文（最小尺寸）
sns.set_theme(context='paper', style='whitegrid')
sns.lineplot(x='x', y='y', data=data)
plt.title('Context: paper')
plt.show()

# 演示 notebook 上下文（默认）
sns.set_theme(context='notebook', style='whitegrid')
sns.lineplot(x='x', y='y', data=data)
plt.title('Context: notebook (default)')
plt.show()

# 演示 talk 上下文（较大尺寸）
sns.set_theme(context='talk', style='whitegrid')
sns.lineplot(x='x', y='y', data=data)
plt.title('Context: talk')
plt.show()

# 演示 poster 上下文（最大尺寸）
sns.set_theme(context='poster', style='whitegrid')
sns.lineplot(x='x', y='y', data=data)
plt.title('Context: poster')
plt.show()