'''
边界	含义
\b	单词边界
\B	非单词边界
'''
import re

'''*************匹配单词边界****************'''
# 匹配单词边界
print('1.匹配单词边界')
text = "hellohellohello world"
res = re.findall(r"hello\b", text)  #相当于匹配'hello\W'
print('text:', text, 'res:', res)     # ['hello']
print('2.匹配非单词边界')
text = "hellohellohello world"
res = re.findall(r"hello\B", text)  #相当于匹配'hello\w'
print('text:', text, 'res:', res)     # ['hello', 'hello']
