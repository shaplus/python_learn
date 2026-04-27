# 1. 创建一个文件，写入5行内容
print("创建文件 test.txt")
with open('test.txt', 'w', encoding='utf-8') as file:
    for i in range(5):
        file.write(f"Line {i+1}\n")
        print(f"已入第 {i+1} 行内容")

# 2. 读取并打印文件内容
print("读取文件 test.txt 内容")
with open('test.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print("文件内容：")
    print(content)

# 3. 追加3行内容
print("追加3行内容到文件 test.txt")
with open('test.txt', 'a', encoding='utf-8') as file:
    for i in range(3):
        file.write(f"Line {i+6}\n")
        print(f"已追加第 {i+6} 行内容")

# 4. 再次读取并打印文件内容
print("再次读取文件 test.txt 内容")
with open('test.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print("文件内容：")
    print(content)


