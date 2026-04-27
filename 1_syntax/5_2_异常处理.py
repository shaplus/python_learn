'''
异常的基本概念:
    异常是程序运行过程中出现的错误，如文件不存在、除零错误等。
Python使用异常处理机制来捕获和处理这些错误，避免程序崩溃。

except错误类型：
一、你写文件操作最常见的（必背）
    FileNotFoundError —— 文件找不到
    FileExistsError —— 文件已存在
    PermissionError —— 没权限读写
    IsADirectoryError —— 把文件夹当文件打开
    OSError —— 系统相关错误（上面这些的父类）   
二、数学 / 运算错误
    ZeroDivisionError —— 除以 0
    OverflowError —— 数值溢出
三、类型 / 值错误
    TypeError —— 类型不对（如字符串 + 数字）
    ValueError —— 值不对（如把abc转成 int）
四、列表 / 字典 / 索引错误
    IndexError —— 列表下标越界
    KeyError —— 字典里没有这个键
    StopIteration —— 迭代到头了
五、变量 / 属性错误
    NameError —— 变量没定义
    AttributeError —— 对象没有这个属性 / 方法
六、语法错误
    SyntaxError —— 语法写错
    IndentationError —— 缩进错
    TabError —— Tab键使用错误
    UnicodeError —— Unicode解码错误
七、万能捕获（最实用）
    Exception
    能抓住上面几乎所有常见错误
    你不知道报啥错时，用它最稳。
层级图：
BaseException
    ├── SystemExit       # exit() 退出
    ├── KeyboardInterrupt# Ctrl+C
    └── Exception        ✅ 你日常 99% 用这个
         ├── OSError          # 文件、系统相关
         │    ├── FileNotFoundError
         │    ├── FileExistsError
         │    ├── PermissionError
         │    └── ...
         ├── TypeError
         ├── ValueError
         ├── IndexError
         ├── KeyError
         ├── NameError
         ├── AttributeError
         ├── ZeroDivisionError
         └── ...
'''

# try-except-语句
print("try-except-语句")
try:
    # 可能会抛出异常的代码
    1 / 0
except Exception as e:
    print(type(e).__name__)  # 打印错误真实名字
    print("捕获到异常:", e)

# 捕获多个异常
print("捕获多个异常")
try:
    # 可能会抛出异常的代码
    1 / 0
except (ZeroDivisionError, FileNotFoundError):
    print("捕获到除零错误或文件不存在错误")
except Exception as e:
    print("捕获到其他异常:", e)

# else和finally子句
# else子句在没有异常抛出时执行
# finally子句无论是否有异常抛出都执行
print("else和finally子句")
print(1)
try:
    # 可能会抛出异常的代码
    1 / 0
except ZeroDivisionError:
    print("除零错误")
else:
    print("没有异常")
finally:
    print("finally子句")
print(2)
try:
    # 可能会抛出异常的代码
    1
except ZeroDivisionError:
    print("除零错误")
else:
    print("没有异常")
finally:
    print("finally子句")

# raise语句
# raise语句可以手动抛出异常
print("raise语句")
try:
    raise ZeroDivisionError("除零错误")
except ZeroDivisionError as e:
    print("捕获到除零错误:", e)

# 自定义异常
print("自定义异常")
class CustomError(Exception):
    pass


def check_age(age):
    if age < 0:
        raise CustomError("年龄不能为负数！")
    return age

try:
    check_age(-5)
except CustomError as e:
    print(f"错误：{e}")
except Exception as e:
    print(f"其他错误：{e}")
