# NumPy 广播(Broadcast)
## 简介
广播(Broadcast)是 numpy 对不同形状(shape)的数组进行数值计算的方式， 对数组的算术运算通常在相应的元素上进行。

如果两个数组 a 和 b 形状相同，即满足 a.shape == b.shape，那么 a*b 的结果就是 a 与 b 数组对应位相乘。这要求维数相同，且各维度的长度相同。

下面的图片展示了数组 b 如何通过广播来与数组 a 兼容。
![广播(Broadcast)](../../images/_numpy_/广播.png)
