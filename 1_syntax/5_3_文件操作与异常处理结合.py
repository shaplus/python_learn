def read_file(filename):
    """读取文件内容，处理可能的异常"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"错误：文件 {filename} 不存在！")
        return None
    except PermissionError:
        print(f"错误：没有权限访问文件 {filename}！")
        return None
    except UnicodeDecodeError:
        print(f"错误：文件 {filename} 编码错误！")
        return None
    except Exception as e:
        print(f"错误：{e}")
        return None

# 使用函数
content = read_file("example.txt")
if content:
    print("文件内容：")
    print(content)
else:
    print("读取文件失败！")