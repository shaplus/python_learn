# NumPy Matplotlib
Matplotlib 是 Python 的绘图库。 它可与 NumPy 一起使用，提供了一种有效的 MatLab 开源替代方案。 它也可以和图形工具包一起使用，如 PyQt 和 wxPython。

pip3 安装：
```bash
pip3 install matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple
```
Linux 系统也可以使用 Linux 包管理器来安装：
- Debian / Ubuntu：
```bash
sudo apt-get install python-matplotlib
```
- Fedora / Redhat：
```bash
sudo yum install python-matplotlib
```

安装完后，你可以使用 python -m pip list 命令来查看是否安装了 matplotlib 模块。
```bash
$ pip show matplotlib        
matplotlib        3.3.0
```

作为线性图的替代，可以通过向 plot() 函数添加格式字符串来显示离散值。 可以使用以下格式化字符。
字符	|描述
---	|---
'-'	|实线样式
'--'	|短横线样式
'-.'	|点划线样式
':'	|虚线样式
'.'	|点标记
','	|像素标记
'o'	|圆标记
'v'	|倒三角标记
'^'	|正三角标记
'&lt;'	|左三角标记
'&gt;'	|右三角标记
'1'	|下箭头标记
'2'	|上箭头标记
'3'	|左箭头标记
'4'	|右箭头标记
's'	|正方形标记
'p'	|五边形标记
'*'	|星形标记
'h'	|六边形标记 1
'H'	|六边形标记 2
'+'	|加号标记
'x'	|X 标记
'D'	|菱形标记
'd'	|窄菱形标记
'&#124;'	|竖直线标记
'_'	|水平线标记

以下是颜色的缩写：
字符	|颜色
---	|---
'b'	|蓝色
'g'	|绿色
'r'	|红色
'c'	|青色
'm'	|品红色
'y'	|黄色
'k'	|黑色
'w'	|白色

## subplot()
subplot() 函数允许你在同一图中绘制不同的东西。

## bar()
pyplot 子模块提供 bar() 函数来生成条形图。

## numpy.histogram()
numpy.histogram() 函数是数据的频率分布的图形表示。 水平尺寸相等的矩形对应于类间隔，称为 bin，变量 height 对应于频率。

numpy.histogram()函数将输入数组和 bin 作为两个参数。 bin 数组中的连续元素用作每个 bin 的边界。

```python
data = [1,2,3,4,5,6,7]
counts, bins = np.histogram(data, bins=3)
```
- counts：每一段有几个数
- bins：每一段的分界线

bins 个数 永远比 counts 多 1
区间默认：左包含、右不包含
np.histogram =
把一堆数字切成好几段，每段帮你数有多少个数

## plt()
Matplotlib 可以将直方图的数字表示转换为图形。 pyplot 子模块的 plt() 函数将包含数据和 bin 数组的数组作为参数，并转换为直方图。