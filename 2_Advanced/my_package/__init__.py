# 导出指定模块
from . import module1 # noqa
from .module2 import function2 # noqa
print("my_package 正在初始化！")

# 包全局变量（整个包都能用）
__version__ = "1.0.0"
__author__ = "张三"
