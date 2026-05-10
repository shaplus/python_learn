import numpy as np 
import matplotlib
from matplotlib import pyplot as plt 

x = np.arange(1,11) 
y =  2  * x +  5 
# plt.title("Matplotlib demo") 
# plt.xlabel("x axis caption") 
# plt.ylabel("y axis caption") 
# plt.plot(x,y) 
# plt.show()
print('-'*50)

'''**************图形中文显示***************'''
print('中文显示')
# fname 为 你下载的字体库路径，注意 SourceHanSansSC-Bold.otf 字体的路径
zhfont1 = matplotlib.font_manager.FontProperties(fname="4_ThirdParty/_numpy_/SourceHanSansSC-Bold.otf") 

# plt.title("文件字体", fontproperties=zhfont1, fontsize=16) 
 
# # fontproperties 设置中文显示，fontsize 设置字体大小
# plt.xlabel("x 轴", fontproperties=zhfont1)
# plt.ylabel("y 轴", fontproperties=zhfont1)
# plt.plot(x,y) 
# plt.show()
print('-'*25)

print('使用系统字体:')
a=sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])

# for i in a:
#     print(i)

# 打印出你的 font_manager 的 ttflist 中所有注册的名字，
# 找一个看中文字体例如：SimHei(黑体）,然后添加以下代码即可：
# plt.title("系统字体", fontproperties="SimHei", fontsize=16) 
# plt.xlabel("x 轴", fontproperties="SimHei") 
# plt.ylabel("y 轴", fontproperties="SimHei") 
# plt.plot(x,y) 
# plt.show()
print('-'*50)

'''**************格式化字符***************'''
print('格式化字符')

print('圆标记')
# plt.title("Matplotlib demo") 
# plt.xlabel("x axis caption") 
# plt.ylabel("y axis caption") 
# plt.plot(x,y,"ob") 
# plt.show()

print('绘制正弦波')
# 计算正弦曲线上点的 x 和 y 坐标
x = np.arange(0,  3  * np.pi,  0.1) 
y = np.sin(x)
# plt.title("sine wave form")  
# # 使用 matplotlib 来绘制点
# plt.plot(x, y) 
# plt.show()

'''**************subplot()***************'''
print('subplot()')

# # 绘制正弦和余弦曲线
# # 计算正弦和余弦曲线上的点的 x 和 y 坐标 
# x = np.arange(0,  3  * np.pi,  0.1) 
# y_sin = np.sin(x) 
# y_cos = np.cos(x)  
# # 建立 subplot 网格，高为 2，宽为 1  
# # 激活第一个 subplot
# plt.subplot(2,  1,  1)  
# # 绘制第一个图像 
# plt.plot(x, y_sin) 
# plt.title('Sine')  
# # 将第二个 subplot 激活，并绘制第二个图像
# plt.subplot(2,  1,  2) 
# plt.plot(x, y_cos) 
# plt.title('Cosine')  
# # 展示图像
# plt.show()

'''**************bar()***************'''
print('bar()')

# # 以下实例生成两组 x 和 y 数组的条形图。
# x =  [5,8,10] 
# y =  [12,16,6] 
# x2 =  [6,9,11] 
# y2 =  [6,15,7] 
# plt.bar(x, y, align =  'center') 
# plt.bar(x2, y2, color =  'g', align =  'center') 
# plt.title('Bar graph') 
# plt.ylabel('Y axis') 
# plt.xlabel('X axis') 
# plt.show()

'''**************numpy.histogram()***************'''
print('numpy.histogram()')

a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
np.histogram(a,bins =  [0,20,40,60,80,100]) 
hist,bins = np.histogram(a,bins =  [0,20,40,60,80,100])  
print (hist) 
print (bins)

'''**************plt()***************'''
print('plt()')

# # 直方图
# a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27]) 
# plt.hist(a, bins =  [0,20,40,60,80,100]) 
# plt.title("histogram") 
# plt.show()
