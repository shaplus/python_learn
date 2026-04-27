import random
# 创建一个列表，包含10个随机整数
numbers = [random.randint(1, 100) for _ in range(10)]
print(numbers)

# 1. 排序并打印
numbers.sort()
print(numbers)

# 2. 反转并打印
numbers.reverse()
print(numbers)

# 3. 计算列表的和、平均值
total = sum(numbers)
print(f"列表的和: {total}")
average = total / len(numbers)
print(f"列表的平均值: {average:.2f}")

# 4. 找出最大值和最小值
max_value = max(numbers)
print(f"列表的最大值: {max_value}")
min_value = min(numbers)
print(f"列表的最小值: {min_value}")
