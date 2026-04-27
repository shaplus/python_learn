'''
上下文管理器（Context Managers）

基本概念:
上下文管理器是Python中用于管理资源的重要工具，它确保资源在使用完毕后能够被正确释放，
无论代码执行过程中是否发生异常。

类实现:
方法	    调用时机	    作用
__init__	创建类实例时	接收参数（文件名、连接信息等）
__enter__	with 开始时	    申请资源、打开连接
__exit__	with 结束时	    释放资源、处理异常

规则：
- 只要实现 __enter__ 和 __exit__，就是上下文管理器
- with 代码块无论正常结束、报错、break跳出，__exit__ 一定执行
- __exit__ 返回 True = 压制异常，程序不崩溃
最适合：文件、数据库、网络、锁、线程、进程、临时目录

总结：
- 用类实现上下文管理器 = 实现 __enter__ + __exit__
- __enter__ 负责创建 / 打开
- __exit__ 负责关闭 / 清理 / 异常处理
最终效果：代码更简洁、资源永不泄露、更安全
'''

import traceback    # noqa

'''最常见的应用场景是文件操作：'''
print('文件操作示例：')
with open('example.txt', 'r') as f:
    content = f.read()
# 此处文件已自动关闭，无需手动调用f.close()
print(content)

'''**************使用类实现**************'''
print('使用类实现示例：')
'''基本实现'''
print('基本实现示例：')
# 通过实现__enter__和__exit__方法来创建上下文管理器：
class MyContextManager:
    def __enter__(self):
        print("进入上下文")
        return self  # 返回值将被赋给as后的变量
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("退出上下文")
        # 如果返回True，则异常会被抑制
        return False

# 使用方式
with MyContextManager() as cm:
    print("在上下文中执行操作")

print('---------------')
'''异常处理'''
print('异常处理示例：')
# exc_type, exc_val用法
print('exc_type, exc_val用法示例：')

class SafeExecutor:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"捕获到异常：{exc_val}")
            return True  # 返回 True = 压制异常，程序不崩溃

# 使用
with SafeExecutor():
    print(1 / 0)  # 除零错误

print("程序继续运行")

print('---------------')
# exc_tb用法,需要import traceback模块
print('exc_tb用法示例：')

class DemoCtx:
    def __enter__(self):
        print("进入上下文")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 无异常直接返回
        if not exc_type:
            print("正常退出，无异常")
            return False

        # ========== exc_tb 核心用法 ==========
        print("\n===== 异常堆栈信息 =====")
        # 1. 打印完整报错栈（和程序原生报错一模一样）
        traceback.print_tb(exc_tb)

        # 2. 获取报错所在 文件名、行号、函数名
        tb_frame = exc_tb.tb_frame
        file_name = tb_frame.f_code.co_filename
        line_no = exc_tb.tb_lineno   # 关键：报错代码行号
        func_name = tb_frame.f_code.co_name

        print(f"错误文件：{file_name}")
        print(f"错误行号：{line_no}")
        print(f"错误函数：{func_name}")
        print(f"错误信息：{exc_val}")

        # 返回True 吞噬异常
        return True

# 测试触发异常
def test_DemoCtx():
    with DemoCtx():
        1 / 0

test_DemoCtx()
print("程序继续运行")

print('------------------------------')
'''**************使用contextlib模块**************'''
'''对于简单的上下文管理器，可以使用contextlib.contextmanager装饰器：'''
from contextlib import contextmanager   # noqa

'''完整示例：模拟打开文件'''
print('完整示例：模拟打开文件')

@contextmanager
def my_open(filename, mode='r'):
    try:
        # 1. 进入 with 时执行
        print("打开文件")
        f = open(filename, mode, encoding='utf-8')

        # 2. 把文件对象返回给 as 接收
        yield f
    
    finally:
        # 3. 无论是否报错，一定会执行
        print("关闭文件")
        f.close()

with my_open("example.txt") as f:
    content = f.read()
    print(content)

print('---------------')
'''带异常处理的写法（捕获错误）'''
print('带异常处理的写法（捕获错误）')
@contextmanager
def safe_run():
    try:
        # 进入
        print("开始执行")
        yield  # 这里会执行 with 内的代码

    except Exception as e:
        # 捕获异常
        print(f"出错了：{e}")
        # 想压制异常就不抛，想让程序崩溃就 raise e

    finally:
        # 清理
        print("结束清理")


# 测试
with safe_run():
    1 / 0  # 报错