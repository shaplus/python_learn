import numpy as np 

'''**********************1. numpy.char.add()*************************'''
# numpy.char.add() 函数依次对两个数组的元素进行字符串连接。
print('1. numpy.char.add():')

print ('连接两个字符串：')
print (np.char.add(['hello'],[' xyz']))
print ('\n')
 
print ('连接示例：')
print (np.char.add(['hello', 'hi'],[' abc', ' xyz']))
print('-'*50)

'''**********************2. numpy.char.multiply()*************************'''
# numpy.char.multiply() 函数对字符串进行多重连接。
print('2. numpy.char.multiply():')

print (np.char.multiply('Runoob ',3))
print('-'*50)

'''**********************3. numpy.char.center()*************************'''
# numpy.char.center() 函数将字符串居中对齐。
print('3. numpy.char.center():')

# np.char.center(str , width,fillchar) ：
# str: 字符串，width: 长度，fillchar: 填充字符
print (np.char.center('Runoob', 20,fillchar = '*'))
print('-'*50)

'''**********************4. numpy.char.capitalize()*************************'''
# numpy.char.capitalize() 函数将字符串的第一个字符转换为大写，其他字符转换为小写。
print('4. numpy.char.capitalize():')

print (np.char.capitalize('runoob'))
print('-'*50)

'''**********************5. numpy.char.title()*************************'''
# numpy.char.title() 函数将字符串的每个单词的首字母转换为大写，其他字符转换为小写。
print('5. numpy.char.title():')

print (np.char.title('i like runoob'))
print('-'*50)

'''**********************6. numpy.char.lower()*************************'''
# numpy.char.lower() 函数将字符串中的所有字符转换为小写。
print('6. numpy.char.lower():')

print (np.char.lower('RUNOOB'))
print('-'*50)

'''**********************7. numpy.char.upper()*************************'''
# numpy.char.upper() 函数将字符串中的所有字符转换为大写。
print('7. numpy.char.upper():')

print (np.char.upper('runoob'))
print('-'*50)

'''**********************8. numpy.char.split()*************************'''
# numpy.char.split() 函数将字符串根据指定的分隔符进行分割。
print('8. numpy.char.split():')

# 分隔符默认为空格
print (np.char.split ('i like runoob?'))
# 分隔符为 .
print (np.char.split ('www.runoob.com', sep = '.'))
print('-'*50)

'''**********************9. numpy.char.splitlines()*************************'''
# numpy.char.splitlines() 函数将字符串根据换行符进行分割。
print('9. numpy.char.splitlines():')

# \n，\r，\r\n 都可用作换行符。
print (np.char.splitlines('i\nlike runoob?')) 
print (np.char.splitlines('i\rlike runoob?'))
print('-'*50)

'''**********************10. numpy.char.join()*************************'''
# numpy.char.join() 函数将字符串数组中的元素连接起来。
print('10. numpy.char.join():')

# 操作字符串
print (np.char.join(':','runoob'))
 
# 指定多个分隔符操作数组元素
print (np.char.join([':','-'],['runoob','google']))
print('-'*50)

'''**********************11. numpy.char.replace()*************************'''
# numpy.char.replace() 函数使用新字符串替换字符串中的所有子字符串。
print('11. numpy.char.replace():')

print (np.char.replace ('i like runoob', 'oo', 'cc'))
print('-'*50)

'''**********************12. numpy.char.encode()*************************'''
# numpy.char.encode() 函数对数组中的每个元素调用 str.encode 函数。 
# 默认编码是 utf-8，可以使用标准 Python 库中的编解码器。
print('12. numpy.char.encode():')

a = np.char.encode('runoob', 'cp500') 
print (a)
print('-'*50)

'''**********************13. numpy.char.decode()*************************'''
# numpy.char.decode() 函数对编码的元素进行 str.decode() 解码。
print('13. numpy.char.decode():')

a = np.char.encode('runoob', 'cp500') 
print (a)
print (np.char.decode(a, 'cp500'))
print('-'*50)
