'''
1. 什么是模块？
模块是一个包含Python定义和语句的文件，文件名即为模块名，后缀为.py。
例如，创建一个calculator.py文件，它就是一个名为calculator的模块。

2. 模块的作用
- 代码组织：将相关功能的代码放在一个文件中，提高代码可读性和可维护性
- 代码复用：避免重复编写相同的代码
- 命名空间隔离：不同模块中的同名变量不会冲突

'''

'''************3. 模块的导入方式*************'''
'''基本导入'''
print('基本导入')
import math  # 导入整个模块     # noqa
result = math.sqrt(4)  # 使用模块名.函数名调用
print(result)

'''导入特定内容'''
print('导入特定内容')
from math import sqrt  # 导入sqrt函数     # noqa
result = sqrt(4)  # 使用函数名调用
print(result)

'''导入多个内容'''
print('导入多个内容')
from math import sqrt, pi  # 导入sqrt函数和pi常量     # noqa
result = sqrt(4)  # 使用函数名调用
print(result)
print(pi)  # 使用常量名调用
print(result)

'''导入所有内容（不推荐）'''
print('导入所有内容（不推荐）')
from math import *  # 导入所有内容     # noqa
print(sin(0.5*pi))  # noqa
print(pi)  # 使用常量名调用

'''导入并别名'''
print('导入并别名')
import math as m  # 导入math模块并别名为m     # noqa
print(m.sqrt(4))    # 使用别名.函数名调用
print(m.pi)  # 使用别名.常量名调用

'''************4. 模块的搜索路径*************'''
'''
Python解释器会按以下顺序查找模块：
- 当前目录
- PYTHONPATH环境变量指定的目录
- 标准库目录
- 任何.pth文件中指定的目录
'''
'''可以通过sys.path查看当前搜索路径：'''
print('可以通过sys.path查看当前搜索路径：')
import sys  # noqa
print(sys.path)
'''
# 当前目录
['c:\\0\\learn\\3_soft\\1_python\\1_learn',     
# 标准库目录，用于存储Python的内置模块和标准库模块(不常用，因为会覆盖系统模块)
'...\\anaconda3\\envs\\python_syntax\\python311.zip',  
# 标准库目录，用于存储Python的DLL文件（动态链接库文件）
'...\\anaconda3\\envs\\python_syntax\\DLLs',  
# 标准库目录，用于存储Python的库文件（库模块）
 '...\\anaconda3\\envs\\python_syntax',  
# 标准库和第三方库目录，用于存储Python的第三方库模块
 '...\\anaconda3\\envs\\python_syntax\\Lib\\site-packages']  
'''
