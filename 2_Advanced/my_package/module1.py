__all__ = [
    "function1"
]

def function1():
    print("Hello, module1!")

if __name__ == "__main__":
    print("module1被直接运行")
else:
    print("module1被导入")