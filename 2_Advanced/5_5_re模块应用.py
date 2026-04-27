'''
1. 常用函数
函数	        功能	            返回值
re.match()	    从字符串开头匹配	 匹配对象或None
re.search()	    在整个字符串中搜索	 匹配对象或None
re.findall()	查找所有匹配项	    列表
re.finditer()	查找所有匹配项	    迭代器
re.sub()	    替换匹配项	        替换后的字符串
re.split()	    根据匹配项分割字符串 列表
re.compile()	编译正则表达式	    正则表达式对象

2. 匹配对象
最常用 核心方法
- group()	    返回匹配的整个字符串
m.group(0)   # 完整匹配内容（全局）
m.group(1)   # 第1个捕获分组
m.group(2)   # 第2个捕获分组
m.group()    # 不写默认 = group(0)
非捕获分组 (?:...) 没有编号，拿不到
量词重复分组，只返回最后一次覆盖的值

- groupdict()   
只针对命名分组，返回字典，键为分组名，值为匹配获获
# 比如 (?P<num>\d+)
m.groupdict()
# {'num': '123'}

- .start() 匹配开始下标
- .end() 匹配结束下标
- .span() 匹配起止下标元组
示例：
s = "aa123bb"
m = re.search(r"\d+", s)
print(m.start())   # 2
print(m.end())     # 5
print(m.span())    # (2, 5)

- .string 返回匹配的原始字符串
- .re 当前使用的正则编译对象
- .pos / .endpos 本次匹配的起始搜索范围（切片范围）

- .expand() 配合反向引用 \1 \2 做格式化替换
示例：  m.expand(r"key:\1") 
'''
import re

'''***************常用函数****************'''
'''re.match()'''
# 从字符串开头匹配
print('1. re.match()')
text = "a1bc234d56e"
res = re.match(r"\d", text)
print('text:', text, 'res:', res)     # None
res = re.match(r"\w", text)
print('text:', text, 'res:', res)     # <re.Match object; span=(0, 1), match='a'>
print('-----------------')

'''re.search()'''
# 在整个字符串中搜索
print('2. re.search()')
text = "a1bc234d56e"
res = re.search(r"\d{3}", text)
print('text:', text, 'res:', res)     # <re.Match object; span=(4, 7), match='234'>
print('-----------------')

'''re.findall()'''
# 查找所有匹配项
print('3. re.findall()')
text = "a1bc234d56e"
res = re.findall(r"\d{2}", text)
print('text:', text, 'res:', res)     # ['23', '56']
print('-----------------')

'''re.finditer()'''
# 查找所有匹配项
print('4. re.finditer()')
text = "a1bc234d56e"
res = re.finditer(r"\d{2}", text)
print('text:', text, 'res:', res)     # <re.SRE_Match object at 0x104200000>
for i in res:
    print(i.group())
print('-----------------')

'''re.sub()'''
# 替换匹配项
print('5. re.sub()')
text = "a1bc234d56e"
res = re.sub(r"\d{2}", "XX", text)
print('text:', text, 'res:', res)     # aXXbcXXdXXe
print('-----------------')

'''re.split()'''
# 根据匹配项分割字符串
print('6. re.split()')
text = "a1bc234d56e"
res = re.split(r"\d{2}", text)
print('text:', text, 'res:', res)     # ['a', 'bc', 'd', 'e']
print('-----------------')

'''re.compile()'''
# 编译正则表达式
print('7. re.compile()')
text = "a1bc234d56e"
pat = re.compile(r"\d{2}")
print('text:', text, 'pat:', pat)     # <re.Pattern object; re.SRE_Pattern object at 0x104200000>
res = pat.findall(text)
print('text:', text, 'res:', res)     # ['23', '56']
res = pat.finditer(text)
for i in res:
    print(i.group())
print('-----------------')

print('----------------------------------')
'''***************匹配对象****************'''
# 匹配对象的常用方法
print('匹配对象的常用方法')
text = "aabbcc666xyz"
res1 = re.search(r"bbcc\d+", text)
res2 = re.search(r"(?P<bb>bb)(?P<cc>cc)(?P<number>\d+)", text)
print('-----------------')

'''group()方法'''
print('group()方法')
print('res1.group(0):', res1.group(0))     # bbcc666
#res1没有捕获分组，所以没有group(1)、group(2)、group(3)方法
print('res2.group(0):', res2.group(0))     # bbcc666
print('res2.group(1):', res2.group(1))     # bb
print('res2.group(2):', res2.group(2))     # cc
print('res2.group(3):', res2.group(3))     # 666
print('res2.group(bb):', res2.group('bb'))     # bb
print('res2.group(cc):', res2.group('cc'))     # cc
print('res2.group(number):', res2.group('number'))     # 666
print('-----------------')

'''groupdict()方法'''
print('groupdict()方法')
print('res2.groupdict():', res2.groupdict())     # {'bb': 'bb', 'cc': 'cc', 'number': '666'}
print('-----------------')

'''start()方法'''
print('start()方法')
print('res1.start():', res1.start())     # 2
print('res2.start():', res2.start())     # 2
print('-----------------')

'''end()方法'''
print('end()方法')
print('res1.end():', res1.end())     # 9
print('res2.end():', res2.end())     # 9
print('-----------------')

'''span()方法'''
print('span()方法')
print('res1.span():', res1.span())     # (2, 9)
print('res2.span():', res2.span())     # (2, 9)
print('-----------------')

'''string属性'''
print('string属性')
print('res1.string:', res1.string)     # aabbcc666xyz
print('res2.string:', res2.string)     # aabbcc666xyz
print('-----------------')

'''re属性'''
print('re属性')
print('res1.re:', res1.re)     # <re.Pattern object; re.SRE_Pattern object at 0x104200000>
print('res2.re:', res2.re)     # <re.Pattern object; re.SRE_Pattern object at 0x104200000>
print('-----------------')

'''pos属性'''
print('pos属性')
print('res1.pos:', res1.pos)     # 0
print('res1.endpos:', res1.endpos)     # 12
print('res2.pos:', res2.pos)     # 0
print('res2.endpos:', res2.endpos)     # 12
print('-----------------')

'''expand()方法'''
print('expand()方法')
print('res2.expand(r"key:\3\2\1"):', res2.expand(r"key:\3\2\1"))     # key:bb666cc
print('-----------------')
