'''
1. 普通字符
普通字符包括大小写字母、数字、标点符号等，它们在正则表达式中表示自身。

示例：
abc 匹配包含"abc"的字符串
123 匹配包含"123"的字符串

2. 特殊字符（元字符）
元字符在正则表达式中有特殊含义，需要转义（使用\）才能表示其字面意义。
元字符	含义	                        示例
.	    匹配任意单个字符（除换行符）	a.c 匹配 "abc"、"adc" 等
*	    匹配前面的字符0次或多次	    ab* 匹配 "a"、"ab"、"abb" 等
+	    匹配前面的字符1次或多次	    ab+ 匹配 "ab"、"abb" 等，不匹配 "a"
?	    匹配前面的字符0次或1次	    ab? 匹配 "a"、"ab"，不匹配 "abb"
^	    匹配字符串开头	    ^abc 匹配以"abc"开头的字符串
$	    匹配字符串结尾	    abc$ 匹配以"abc"结尾的字符串
[]	    字符类，匹配其中任意一个字符	[abc] 匹配 "a"、"b" 或 "c"
[0-9]	数字字符类，匹配0-9之间的数字	[0-9] 匹配 "0"、"1"、"2" 等
[a-zA-Z0-9_]	字母、数字、下划线字符类，匹配字母、数字、下划线	[a-zA-Z0-9_] 匹配 "a"、"b"、"c" 等
[^]	    否定字符类，匹配除其中字符外的任意字符	[^abc] 匹配除"a"、"b"、"c"外的任意字符
|	    或操作，匹配左右任意一个表达式	ab|cd 匹配 "ab" 或 "cd"
()	    分组，将多个字符作为一个整体	    (ab)+ 匹配 "ab"、"abab" 等
\	    转义字符，将特殊字符转义为普通字符	    \. 匹配 "."

'''
import re
'''*****************1. 普通字符*****************'''
# 匹配包含"abc"的字符串
print('1.匹配包含"abc"的字符串')
text = "csaabcdeabc"
res = re.findall(r"abc", text)
print(res)  
# ['abc', 'abc']

'''*****************1. 特殊字符（元字符）*****************'''
''' . 匹配任意单个字符（除换行符）'''
# 匹配一个字符
print('2.匹配一个字符')
text = "abc123"
res = re.findall(r".", text)
print(res)  
# ['a', 'b', 'c', 'd', 'e']

''' * 匹配前面的字符0次或多次 '''
# 匹配一个或多个"b"
print('3.匹配0个或多个"b"')
text = "abbba"
res = re.findall(r"ab*", text)
print('text:', text, 'res:', res)     # ['ab', 'abbb']

''' + 匹配前面的字符1次或多次 '''
# 匹配一个或多个"b"
print('4.匹配一个或多个"b"')
text = "abbba"
res = re.findall(r"ab+", text)
print('text:', text, 'res:', res)     # ['ab', 'abbb']

''' ? 匹配前面的字符0次或1次 '''
# 匹配一个或0个"b"
print('5.匹配一个或0个"b"')
text = "abbba"
res = re.findall(r"ab?", text)
print('text:', text, 'res:', res)     # ['ab', 'abbb']

''' ^ 匹配字符串开头 '''
# 匹配以"abc"开头的字符串
print('6.匹配以"abc"开头的字符串')
text1 = "abcde"
text2 = "defabc"
res1 = re.findall(r"^abc", text1)
res2 = re.findall(r"^abc", text2)
print('text1:', text1, 'res1:', res1)     # ['abc']
print('text2:', text2, 'res2:', res2)     # []

''' $ 匹配字符串结尾 '''
# 匹配以"abc"结尾的字符串
print('7.匹配以"abc"结尾的字符串')
text1 = "abcde"
text2 = "defabc"
res1 = re.findall(r"abc$", text1)
res2 = re.findall(r"abc$", text2)
print('text1:', text1, 'res1:', res1)     # []
print('text2:', text2, 'res2:', res2)     # ['abc']

''' [] 字符类，匹配其中任意一个字符 '''
# 匹配"a"、"b"或"c"
print('8.匹配"a"、"b"或"c"')
text = "abc123"
res = re.findall(r"[abc]", text)
print('text:', text, 'res:', res)     # ['a', 'b', 'c']

# 匹配指定范围的数字
print('9.匹配指定范围的数字')
text = "123456"
res = re.findall(r"[2-5]", text)
print('text:', text, 'res:', res)     # ['2', '3', '4', '5']

''' `	`	或操作，匹配左右任意一个表达式 '''
# 匹配"ab"或"cd"
print('10.匹配"ab"或"cd"')
text = "ab123cd"
res = re.findall(r"ab|cd", text)
print('text:', text, 'res:', res)     # ['ab', 'cd']

''' () 分组，将多个字符作为一个整体 '''
# 匹配"ab"或"cd"
print('11.匹配"ab"或"cd"')
text = "abcbbac"
res = re.findall(r"(bc)", text)
print('text:', text, 'res:', res)     # ['bc', 'bc']

''' \ 转义字符，将特殊字符转义为普通字符 '''
# 匹配"."
print('12.匹配"."')
text = "123.456.789"
res = re.findall(r"\.", text)
print('text:', text, 'res:', res)     # ['.', '.']

# 匹配"\"
print('13.匹配"\\"')
text = "123\\456\\789"
res = re.findall(r"\\", text)
print('text:', text, 'res:', res)     # ['\\', '\\', '\\']


