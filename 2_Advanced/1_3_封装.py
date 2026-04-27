'''
封装：封装是指将对象的属性和方法封装起来，只暴露必要的接口给外部使用。
封装的作用：
- 隐藏实现细节，保护数据安全。
- 提供统一的接口，简化调用。
- 促进代码的重用和维护。
注意:
- 使用下划线开头表示私有属性和方法。
- 外部不能直接访问私有属性和方法，只能通过公共方法来操作。
'''

# 封装示例
class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance  # 使用下划线开头表示私有属性
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"存款成功，当前余额：{self._balance}")
        else:
            print("存款金额必须大于0")
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"取款成功，当前余额：{self._balance}")
        else:
            print("取款金额无效")
    
    def get_balance(self):
        return self._balance
    
# 实例化对象
account = BankAccount(1000)

# 调用方法
print('调用方法：')
account.deposit(500)
account.withdraw(200)
print(account.get_balance())