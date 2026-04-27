import os
# 文件的打开与关闭

# 1. 正常打开与关闭
'''
文件打开模式：
- "r"：只读模式（默认）
- "r+"：读写模式（覆盖文件内容）
- "w"：写入模式（覆盖文件内容）
- "w+"：写入模式（覆盖文件内容）
- "a"：追加模式（不覆盖文件内容）
- "a+"：追加模式（不覆盖文件内容）
- "x"：创建模式（如果文件不存在则创建，如果存在则报错）
- "x+"：创建模式（如果文件不存在则创建，如果存在则报错）
- "t"：文本模式（默认）
- "b"：二进制模式（用于二进制文件）
'''

# 1. 文件的打开与关闭
# 基本打开模式
#在Python中，使用open()函数来打开文件，使用close()方法来关闭文件。
file = open("example.txt", "w")
file.write("Hello, World!\n")
file.close()

# 使用上下文管理器（with语句）
#with语句是一种更安全的打开文件的方式，它自动处理文件的关闭。
with open("example.txt", "a") as file:
    file.write("Hello, World!")
#with语句在文件操作完成后自动关闭文件，无需手动调用close()方法。

# 2. 文件的读取
#在Python中，使用read()方法来读取文件内容。
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# 逐行读取文件内容
with open("example.txt", "r") as file:
    for line in file:
        print(line)
        print(line.strip())  # 移除行末的换行符
        print("=" * 20)

# 读取指定数量的字符
with open("example.txt", "r") as file:
    content = file.read(10)
    print("读取的字符数:", len(content))
    print(content)

# 读取所有行到列表
with open("example.txt", "r") as file:
    lines = file.readlines()
    print("读取的行数:", len(lines))
    print(lines)

# 读取指定行
with open("example.txt", "r") as file:
    line = file.readline()
    print("第1行:", line.strip())
    line = file.readline()
    print("第2行:", line.strip())
    line = file.readline()
    print("第3行:", line.strip())  

# 3. 文件的写入
# 写入字符串
#在Python中，使用write()方法来写入文件内容。
with open("example.txt", "w") as file:
    file.write("Hello, World!")

# 写入列表
with open("example.txt", "w") as file:
    lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
    file.writelines(lines)

# 4. 文件的定位与操作
# 定位到文件开头
print("定位到文件开头")
with open("example.txt", "r") as file:
    file.seek(0)
    content = file.read()
    print(content)

# 定位到文件末尾
#seek()方法可以将文件指针移动到指定位置。
#参数：
#offset：要移动到的位置。
#whence：指定移动方向的常量，0表示从文件开头移动，1表示从当前位置移动，2表示从文件末尾移动。
#默认值为0，即从文件开头移动。
#seek()方法返回当前文件指针的位置。
#seek()方法可以用于定位到文件的开头、当前位置或末尾。
#在文本模式 'r' 下，whence=1 和 whence=2 只能配合 offset=0 使用，否则会报错。
print("定位到文件末尾")
with open("example.txt", "r") as file:
    file.seek(0, 2)
    content = file.read()
    print(content)

# 获取当前位置
print("获取当前位置")
with open("example.txt", "r") as file:
    print("当前位置:", file.tell())
    content = file.read(3)
    print('读取后的位置:', file.tell())

# 文件的复制
print("文件的复制")
with open("example.txt", "r") as source_file, open("copy.txt", "w") as dest_file:
    dest_file.write(source_file.read())

# 文件的移动
print("文件的移动")
os.rename("copy.txt", "new_copy.txt")
print("文件移动完成")

# 文件的删除
print("文件的删除")
os.remove("new_copy.txt")
print("文件删除完成")

# 统计文件行数和单词数
print("统计文件行数和单词数")
with open("example.txt", "r") as file:
    lines = file.readlines()
    print("行数:", len(lines))
    words = [word for line in lines for word in line.split()]
    print("单词数:", len(words))
