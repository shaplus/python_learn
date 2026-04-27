'''***************1. 自定义上下文管理器的高级实现***************'''
print('1. 自定义上下文管理器的高级实现')
class DatabaseConnection:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = None
    
    def __enter__(self):
        print("建立数据库连接")
        # 模拟建立连接
        self.connection = {"status": "connected"}
        return self
    
    def query(self, sql):
        print(f"执行SQL: {sql}")
        return {"result": "success"}
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("关闭数据库连接")
        self.connection = None
        # 处理异常
        if exc_type:
            print(f"发生异常: {exc_val}")
            # 返回False，让异常继续传播
            return False

# 使用方式
with DatabaseConnection("localhost:5432") as db:
    result = db.query("SELECT * FROM users")
    print(result)
print('------------------------------------')

'''***************2. 实现一个计时器上下文管理器***************'''
print('2. 实现一个计时器上下文管理器')
from contextlib import contextmanager   # noqa
import time  # noqa

@contextmanager
def timer(name):
    print(f"{name} 开始")
    start = time.time()
    yield
    end = time.time()
    print(f"{name} 结束，耗时: {end - start:.2f}秒")

# 使用方式
with timer("执行任务"):
    # 模拟耗时操作
    time.sleep(1)
    print("执行任务中...")
