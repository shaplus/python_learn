# Matplotlib imread() 方法
imread() 方法是 Matplotlib 库中的一个函数，用于从图像文件中读取图像数据。

imread() 方法返回一个 numpy.ndarray 对象，其形状是 (nrows, ncols, nchannels)，表示读取的图像的行数、列数和通道数：

如果图像是灰度图像，则 nchannels 为 1。
如果是彩色图像，则 nchannels 为 3 或 4，分别表示红、绿、蓝三个颜色通道和一个 alpha 通道。
## 语法
imread() 方法的语法如下：
```python
matplotlib.pyplot.imread(fname, format=None)
```
参数说明：
- fname：指定了要读取的图像文件的文件名或文件路径，可以是相对路径或绝对路径。
- format ：参数指定了图像文件的格式，如果不指定，则默认根据文件后缀名来自动识别格式。

**注意：**
整数颜色值在 0 到 255 之间，分别表示不同的颜色。
浮点数颜色值在0到1之间，代表的值实际上是乘以255后的值。