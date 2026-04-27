'''
1. 什么是包？
包是一个包含多个模块的目录，必须包含一个特殊的__init__.py文件
（Python 3.3+中可以为空，但建议保留）。

2. 包的结构示例
my_package/
├── __init__.py
├── module1.py
├── module2.py
└── sub_package/
    ├── __init__.py
    └── module3.py

'''

'''**************3. 包的导入方式******************'''
'''导入包中的模块'''
print("导入包中的模块")
import my_package.module1   # noqa
my_package.module1.function1()

'''从包中导入模块和函数'''
print("从包中导入模块和函数")
from my_package import module1, module2 # noqa
module1.function1()
module2.function2()

'''从包的模块中导入函数'''
print("从包的模块中导入函数")
from my_package.module1 import function1 # noqa
function1()

'''**************4. __init__.py的作用******************'''
'''
- 标识目录为包
- 可以在其中定义包级别的变量和函数
- 控制包的导入行为
'''
print("导入包")
# 需要在__init__.py中导出指定模块
from my_package import function2   # noqa
print(my_package.__version__)
print(my_package.__author__)
function2()