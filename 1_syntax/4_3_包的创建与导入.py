# 导入包中的模块
print('导入包中的模块')
import my_package.module1   # noqa: E402
print(my_package.module1.function1())  # 输出：Function 1 from module1

# 导入包中的特定模块
print('导入包中的特定模块')
from my_package import module2  # noqa: E402
print(module2.function2())  # 输出：Function 2 from module2

# 导入包中的模块并起别名
print('导入包中的模块并起别名')
from my_package import module1 as m1     # noqa: E402
print(m1.function1())  # 输出：Function 1 from module1

# 导入子包中的模块
print('导入子包中的模块')
from my_package.sub_package import module3  # noqa: E402 F401
print(module3.function3())  # 输出：Function 3 from module3
# 从子包导入所有模块
# 注意：__init__.py文件中必须包含__all__列表，且__all__列表中必须包含所有要导入的模块，否则会报错。
print('从子包导入所有模块')
from my_package.sub_package import *  # noqa: E402 F403
print(module3.function3())  # 输出：Function 3 from module3  # noqa: E402 F405
print(module4.function4())  # 输出：Function 4 from module4  # noqa: E402 F405
