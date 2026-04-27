'''
- 贪婪与非贪婪
- 零宽断言
- 标志（Flags）

1. 贪婪与非贪婪
贪婪模式：所以量词默认情况下贪婪，量词会尽可能多地匹配字符
非贪婪模式：在量词后添加?，使其尽可能少地匹配字符

示例：
贪婪：a.*b 匹配 "a任意字符b"，如 "acccb" 会匹配整个字符串
非贪婪：a.*?b 匹配 "a到第一个b"，如 "acccb" 会匹配 "acccb" 中的 "acb"（如果有的话）

2. 零宽断言
零宽断言用于指定匹配位置的条件，不消耗字符，参与判断的字符还能被后续的匹配操作使用。

断言	    含义	    示例
(?=pattern)	正向先行断言，匹配后面跟着pattern的位置	a(?=b) 匹配后面跟着"b"的"a"
(?!pattern)	负向先行断言，匹配后面不跟着pattern的位置	a(?!b) 匹配后面不跟着"b"的"a"
(?<=pattern)	正向后行断言，匹配前面是pattern的位置	(?<=a)b 匹配前面是"a"的"b"
(?<!pattern)	负向后行断言，匹配前面不是pattern的位置	(?<!a)b 匹配前面不是"a"的"b"

3. 标志（Flags）
标志（Flags）用于修改匹配行为，改变默认的匹配规则。

- re.I / re.IGNORECASE
作用:忽略大小写匹配
示例：
re.search(r'abc', 'ABC', re.I) 匹配 "abc"

- re.M / re.MULTILINE 【高频重点】
作用:多行匹配，改造两个边界符规则:
    ^ 原本：只匹配整个文本最开头，开 re.M 后：每一行的开头
    $ 原本：只匹配整个文本最结尾，开 re.M 后：每一行的结尾
示例：
re.search(r'^abc', 'line1\nabc', re.M) 匹配 "abc"

- re.S / re.DOTALL 【超级常用】
作用：让.点号 匹配换行符 \n
默认规则：
. 匹配除了换行 \n 以外所有字符
开启 re.S：
. = 真・任意字符，包含换行符
示例：
re.search(r'a.b', 'a\nb', re.S) 匹配 "a\nb"

4. re.A / re.ASCII
作用：让 \w \d \s 只匹配 ASCII 字符
默认：
\w 会匹配中文、日文、韩文等万国字符
开 re.A：
\w 只匹配：a-z A-Z 0-9 _
中文不再被当成单词字符
示例：
re.search(r'\w+', 'a1你好b2c3', re.A) 匹配 "a1"，"b2c3"

- re.X / re.VERBOSE
作用：正则允许写空格、写注释
用来写超长、复杂正则，美化可读性
示例：
reg = r"""
\d+   # 匹配数字
-     # 连接符
\w+   # 匹配字母
"""
re.findall(reg, "123-abc", re.X) 匹配 ["123-abc"]
'''
import re

'''***************贪婪与非贪婪****************'''
'''贪婪模式'''
print('贪婪模式：')
# 用a.*匹配
print('1.用a.*匹配')
text = "acccb"
res = re.findall(r"a.*", text)
print('text:', text, 'res:', res)     # ['acccb']

# 用a.+匹配
print('2.用a.+匹配')
text = "acccb"
res = re.findall(r"a.+", text)
print('text:', text, 'res:', res)     # ['acccb']

# 用a.?匹配
print('3.用a.?匹配')
text = "acccb"
res = re.findall(r"a.?", text)
print('text:', text, 'res:', res)     # ['acccb']
print('-----------------')
'''非贪婪模式'''
print('非贪婪模式：')
# 用a.*?匹配
print('4.用a.*?匹配')
text = "acccb"
res = re.findall(r"a.*?", text)
print('text:', text, 'res:', res)     # ['acb']

# 用a.+?匹配
print('5.用a.+?匹配')
text = "acccb"
res = re.findall(r"a.+?", text)
print('text:', text, 'res:', res)     # ['acb']

# 用a.??匹配
print('6.用a.??匹配')
text = "acccb"
res = re.findall(r"a.??", text)
print('text:', text, 'res:', res)     # ['acb']

print('----------------------------------------')
'''***************零宽断言****************'''
print('零宽断言：')
# 正向先行断言
print('7.正向先行断言')
text = "acccb"
res = re.findall(r"a(?=b)", text)
print('text:', text, 'res:', res)     # ['a']
print('-----------------')
# 负向先行断言
print('8.负向先行断言')
text = "acccb"
res = re.findall(r"a(?!b)", text)
print('text:', text, 'res:', res)     # ['a']
print('-----------------')
# 正向后行断言
print('9.正向后行断言')
text = "acccb"
res = re.findall(r"(?<=a)b", text)
print('text:', text, 'res:', res)     # ['b']
print('-----------------')
# 负向后行断言
print('10.负向后行断言')
text = "acccb"
res = re.findall(r"(?<!a)b", text)
print('text:', text, 'res:', res)     # ['b']
print('-----------------')

print('----------------------------------------')
'''***************标志（Flags）****************'''
print('标志（Flags）：')
'''re.I / re.IGNORECASE'''
print('11. re.I / re.IGNORECASE')
text = "a1bc234d56eA"
res = re.findall(r"A", text, re.I)
print('text:', text, 'res:', res)    #['a', 'A']
print('-----------------')

'''re.M / re.MULTILINE'''
print('12. re.M / re.MULTILINE')
text = "a1bc234d56eA\na1bc234d56eA"
res = re.findall(r"a1", text, re.M)
print('text:', text, 'res:', res)     # ['a1', 'a1']
print('-----------------')

'''re.S / re.DOTALL'''
print('13. re.S / re.DOTALL')
text = "a\nb"
res = re.findall(r"a.b", text, re.S)
print('text:', text, 'res:', res)     # ['a\nb']
print('-----------------')

'''re.A / re.ASCII'''
print('14. re.A / re.ASCII')
text = "a1你好b2c3"
res = re.findall(r"\w+", text, re.A)
print('text:', text, 'res:', res)     # ['a1', 'b2c3']
print('-----------------')

'''re.X / re.VERBOSE'''
print('15. re.X / re.VERBOSE')
reg = r"""
\d+   # 匹配数字
-     # 连接符
\w+   # 匹配字母
"""
text = "123-abc"
res = re.findall(reg, text, re.X)
print('text:', text, 'res:', res)     # ['123-abc']
print('-----------------')
