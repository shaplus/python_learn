'''
1. 相对导入
    - 相对导入：在模块内部导入其他模块时，使用点号表示当前目录
    - 例如：from . import module1
    - 例如：from .module2 import function2
'''

'''*********2. 模块的__name__属性*********'''
'''
- 当模块被直接运行时，__name__值为"__main__"
- 当模块被导入时，__name__值为模块名
'''
print('模块的__name属性')
from my_package import module1   # noqa
print(module1.__name__)

'''*********2. 模块的__all__属性*********'''
'''在模块中定义__all__列表，控制from module import *时导入的内容：'''
print('模块的__all__属性')
from my_package.module2 import *   # noqa
function2() # noqa
fuction2_2() # noqa
