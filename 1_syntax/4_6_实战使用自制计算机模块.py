from caculator import add, sub, mul, div, pow, mod  # noqa: E402
print(f'1 + 2 = {add(1, 2)}')  # 输出：3
print(f'3 - 2 = {sub(3, 2)}')  # 输出：1
print(f'2 * 3 = {mul(2, 3)}')  # 输出：6
print(f'4 / 2 = {div(4, 2)}')  # 输出：2.0
print(f'2 ** 3 = {pow(2, 3)}')  # 输出：8
print(f'10 % 3 = {mod(10, 3)}')  # 输出：1

# 计算一个复杂的表达式
print('计算一个复杂的表达式')
result = add(sub(10, 3), mul(2, 5))
print(f'10 - 3 + 2 * 5 = {result}')  # 输出：13