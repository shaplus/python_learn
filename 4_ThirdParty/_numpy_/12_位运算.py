import numpy as np

arr1 = np.array([True, False, True], dtype=bool)
arr2 = np.array([False, True, False], dtype=bool)

result_and = np.bitwise_and(arr1, arr2)
result_and2 = arr1 & arr2
result_or = np.bitwise_or(arr1, arr2)
result_or2 = arr1 | arr2
result_xor = np.bitwise_xor(arr1, arr2)
result_xor2 = arr1 ^ arr2
result_not = np.bitwise_not(arr1)
result_not2 = ~arr1

print("AND:", result_and)  # [False, False, False]
print("AND2:", result_and2)  # [False, False, False]
print("OR:", result_or)    # [True, True, True]
print("OR2:", result_or2)  # [True, True, True]
print("XOR:", result_xor)  # [True, True, True]
print("XOR2:", result_xor2)  # [True, True, True]
print("NOT:", result_not)  # [False, True, False]

# 按位取反

arr_invert1 = np.invert(np.array([1, 2], dtype=np.int8))
arr_invert2 = ~np.array([1, 2], dtype=np.int8)
print("Invert1:", arr_invert1)
print("Invert2:", arr_invert2)

# 左移位运算
arr_left_shift1 = np.left_shift(5, 2)
arr_left_shift2 = 5 << 2
print("Left Shift1:", arr_left_shift1)
print("Left Shift2:", arr_left_shift2)  # 20

# 右移位运算
arr_right_shift1 = np.right_shift(10, 1)
arr_right_shift2 = 10 >> 1
print("Right Shift1:", arr_right_shift1)
print("Right Shift2:", arr_right_shift2)  # 5

print('----------------------------------')

'''**********************1. bitwise_and*************************'''
print('1. bitwise_and:')

print ('5 和 6 的二进制形式：')
a,b = 5,6
print (bin(a), bin(b))
print ('\n')
 
print ('5 和 6 的位与：')
print (bin(np.bitwise_and(5, 6)))

print('----------------------------------')

'''**********************2. bitwise_or*************************'''
print('2. bitwise_or:')

a,b = 5,6 
print ('5 和 6 的二进制形式：')
print (bin(a), bin(b))
 
print ('5 和 6 的位或：')
print (bin(np.bitwise_or(5, 6)))
print('----------------------------------')

'''**********************3. bitwise_xor*************************'''
print('3. bitwise_xor:')

a,b = 5,6 
print ('5 和 6 的二进制形式：')
print (bin(a), bin(b))
 
print ('5 和 6 的位异或：')
print (bin(np.bitwise_xor(5, 6)))
print('----------------------------------')

'''**********************4. bitwise_invert*************************'''
print('4. bitwise_invert:')

print ('13 的位反转，其中 ndarray 的 dtype 是 uint8：')
print (np.invert(np.array([13], dtype = np.uint8)))
print ('\n')
# 比较 13 和 242 的二进制表示，我们发现了位的反转
 
print ('13 的二进制表示：')
print (np.binary_repr(13, width = 8))
print ('\n')
 
print ('242 的二进制表示：')
print (np.binary_repr(242, width = 8))
print('----------------------------------')

'''**********************5. left_shift*************************'''
# left_shift() 函数将数组元素的二进制形式向左移动到指定位置，右侧附加相等数量的 0。
print('5. left_shift:')

print ('将 10 左移两位：')
print (np.left_shift(10,2))
print ('\n')
 
print ('10 的二进制表示：')
print (np.binary_repr(10, width = 8))
print ('\n')
 
print ('40 的二进制表示：')
print (np.binary_repr(40, width = 8))
#  '00001010' 中的两位移动到了左边，并在右边添加了两个 0。
print('----------------------------------')

'''**********************6. right_shift*************************'''
# right_shift() 函数将数组元素的二进制形式向右移动到指定位置，左侧附加相等数量的 0。
print('6. right_shift:')

print ('将 40 右移两位：')
print (np.right_shift(40,2))
print ('\n')
 
print ('40 的二进制表示：')
print (np.binary_repr(40, width = 8))
print ('\n')
 
print ('10 的二进制表示：')
print (np.binary_repr(10, width = 8))
#  '00001010' 中的两位移动到了右边，并在左边添加了两个 0。
print('----------------------------------')
