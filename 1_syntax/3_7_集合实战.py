# 创建两个集合
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
print("set1:", set1)
print("set2:", set2)

# 1. 打印两个集合的并集
print("并集:", set1 | set2)

# 2. 打印两个集合的交集
print("交集:", set1 & set2)

# 3. 打印两个集合的差集
print("差集:", set1 - set2)

# 4. 打印两个集合的对称差集
print("对称差集:", set1 ^ set2)

# 5. 向set1添加元素9
set1.add(9)
print("添加元素9后:")
print("set1:", set1)

# 6. 从set2中移除元素6
set2.remove(6)
print("移除元素6后:")
print("set2:", set2)
