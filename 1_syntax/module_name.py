# module_name.py
def my_function():
    print("Hello from my_function")

if __name__ == "__main__":
    # 当模块被直接运行时执行
    print('__name__:', __name__)
    print("Module is being run directly")
    my_function()
else:
    # 当模块被导入时执行
    print("Module is being imported")