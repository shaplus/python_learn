'''
简写	含义	等价于
\d	匹配数字	[0-9]
\D	匹配非数字	[^0-9]
\w	匹配字母、  数字、下划线	[a-zA-Z0-9_]
\W	匹配非字母、数字、下划线	[^a-zA-Z0-9_]
\s	匹配空白字符（空格、制表符、换行符等）	[ \t\n\r\f\v]
\S	匹配非空白字符	[^ \t\n\r\f\v]
'''
import re

'''*************匹配数字****************'''
# 匹配数字
print('1.匹配数字')
text = "a1bc234d56e"
res = re.findall(r"\d", text)
print('text:', text, 'res:', res)     # ['1', '2', '3', '4', '5', '6']

# 匹配非数字
print('2.匹配非数字')
text = "a1bc234d56e"
res = re.findall(r"\D", text)
print('text:', text, 'res:', res)     # ['a', 'b', 'c', 'd', 'e']

'''*************匹配字母、数字、下划线****************'''
# 匹配字母、数字、下划线
print('3.匹配字母、数字、下划线')
text = "a1bc23*\\4d56e"
res = re.findall(r"\w", text)
print('text:', text, 'res:', res)     # ['a', '1', 'b', 'c', '2', '3', '4', 'd', '5', '6']
print('4.匹配非字母、数字、下划线')
text = "a1bc23*\\4d56e"
res = re.findall(r"\W", text)
print('text:', text, 'res:', res)     # ['_', '']

'''*************匹配空白字符****************'''
# 匹配空白字符
print('5.匹配空白字符')
text = "a1b c23*\\4d56e\r\n\t"
res = re.findall(r"\s", text)
print('text:', text, 'res:', res)     # [' ', '\\n', '\\t', '\\r', '\\f', '\\v']
print('6.匹配非空白字符')
text = "a1b c23*\\4d56e\r\n\t"
res = re.findall(r"\S", text)
print('text:', text, 'res:', res)     # ['a', '1', 'b', 'c', '2', '3', '4', 'd', '5', '6']

