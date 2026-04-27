# caculator.py
def add(a, b):
    """加法"""
    return a + b

def sub(a, b):
    """减法"""
    return a - b

def mul(a, b):
    """乘法"""
    return a * b

def div(a, b):
    """除法"""
    return a / b

def pow(a, b):
    """指数"""
    return a ** b

def mod(a, b):
    """取余"""
    return a % b

if __name__ == "__main__":
    print("Calculator Module Test")
    print(f"1 + 2 = {add(1, 2)}")  # 输出：3
    print(f"3 - 2 = {sub(3, 2)}")  # 输出：1
    print(f"2 * 3 = {mul(2, 3)}")  # 输出：6
    print(f"4 / 2 = {div(4, 2)}")  # 输出：2.0
    print(f"2 ** 3 = {pow(2, 3)}")  # 输出：8
    print(f"10 % 3 = {mod(10, 3)}")  # 输出：1