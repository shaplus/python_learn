def safe_divide(a, b):
    """安全的除法函数，处理除零错误"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("错误：除数不能为零！")
        return None

# 测试函数
print("测试安全除法函数 safe_divide")
print(safe_divide(10, 2))  # 应该返回5.0
print(safe_divide(10, 0))  # 应该提示错误并返回None

# 练习3：文件操作与异常处理结合
print("测试安全文件复制函数 copy_file_safely")
def copy_file_safely(src, dst):
    """安全地复制文件，处理可能的异常"""
    try:
        with open(src, "rb") as source:
            content = source.read()
        with open(dst, "wb") as destination:
            destination.write(content)
        print(f"文件 {src} 已成功复制到 {dst}")
        return True
    except FileNotFoundError:
        print(f"错误：源文件 {src} 不存在！")
        return False
    except PermissionError:
        print(f"错误：没有权限访问源文件 {src}！")
        return False
    except Exception as e:
        print(f"错误：{e}")
        return False

# 测试函数
copy_file_safely("source.txt", "destination.txt")