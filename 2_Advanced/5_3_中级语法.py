'''
量词,分组与捕获,反向引用

1. 量词
量词用于指定前面的字符或分组的匹配次数。
量词	含义	示例
{n}	    匹配恰好n次	a{3} 匹配 "aaa"
{n,}	匹配至少n次	a{2,} 匹配 "aa"、"aaa" 等
{n,m}	匹配n到m次	a{1,3} 匹配 "a"、"aa"、"aaa"

2. 分组与捕获
分组：使用()将多个字符组合成一个单元
捕获：分组会捕获匹配的内容，可通过反向引用或后续处理获取
注意：
    - 捕获分组 (ab)：会把匹配到的内容存入「分组 1、分组 2...」，
    后续可以用 group(1) 或 \1 引用
    - findall里面有捕获分组，返回的是一个元组，每个元素对应一个分组
    - 非捕获分组 (?:ab)：匹配结果不会被单独保存，没有分组编号，无法用 group() 引用
示例：
(ab)+ 匹配一个或多个"ab"
(\d{4})-(\d{2})-(\d{2}) 匹配日期格式，捕获年、月、日

命名捕获分组（自定义名字）
Python 固定语法：(?P<自定义名字>正则内容)
- ?P<name> 是固定写法
- <> 里面是你自己起的分组名（英文）

3. 反向引用
使用\n（n为分组编号）引用前面捕获的分组内容。
注意：
    - 反向引用只能引用前面捕获的分组，不能引用后面捕获的分组
    - 引用的分组内容必须和对应分组存的内容完全一样
示例：
(\w)\1 匹配连续重复的字符，如 "aa"、"bb"
(\d{2})-(\d{2})-\2-\1 匹配如 "12-34-34-12" 这样的模式
'''
import re

'''***************量词****************'''
# 匹配恰好n次
print('1.匹配恰好n次')
text = "a1bc234d56e"
res = re.findall(r"\d{3}", text)
print('text:', text, 'res:', res)     # ['234']

# 匹配至少n次
print('2.匹配至少n次')
text = "a1bc234d56e"
res = re.findall(r"\d{2,}", text)
print('text:', text, 'res:', res)     # ['234', '56']

# 匹配n到m次
print('3.匹配n到m次')
text = "a1bc234d56e"
res = re.findall(r"\d{1,2}", text)
print('text:', text, 'res:', res)     # ['1', '23']

'''***************分组与捕获****************'''
# 匹配一个或多个"ab"
print('4.匹配一个或多个"ab"')
text = "ababcab"
res = re.findall(r"(ab)+", text)    #['ab', 'ab']
print('text:', text, 'res:', res)

# 匹配日期格式
print('5.匹配日期格式')
text = "2023-03-15-10:10:33"
res = re.findall(r"(\d{4})-(\d{2})-(\d{2})", text)
print('text:', text, 'res:', res)   #res: [('2023', '03', '15')]

# 命名捕获分组（自定义名字）
print('6.命名捕获分组（自定义名字）')
text = "ab12cc"
res = re.search(r"(?P<number>\d+)", text)
print('text:', text, 'res:', res.group('number'))     # 12

# 非捕获分组
print('7.非捕获分组')
text = "ababcab"
res = re.findall(r"(?:ab)+", text)
print('text:', text, 'res:', res)   #['abab', 'ab']

'''***************反向引用****************'''
# 匹配连续重复的字符
print('8.匹配连续重复的字符')
text = "aaabcd"
res = re.findall(r"(\w)\1", text)   #捕获前两个a
print('text:', text, 'res:', res)   #['a']

# 匹配如 "12-34-34-12" 这样的模式
print('9.匹配如 "12-34-34-12" 这样的模式')
text = "12-34-34-12"
res = re.findall(r"(\d{2})-(\d{2})-\2-\1", text)
print('text:', text, 'res:', res)   #[('12', '34')]
