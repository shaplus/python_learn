
'''条件语句（if语句）用于根据条件的真假来执行不同的代码块。Python中的if语句的基本语法如下：

if 条件:
    语句块
elif 条件:
    语句块
else:
    语句块
在这个语法结构中：
- if：用于检查一个条件，如果条件为真，则执行对应的语句块。
- elif：是“else if”的缩写，用于检查另一个条件，如果前面的条件不满足且这个条件满足，则执行对应的语句块。可以有多个elif。
- else：当所有前面的条件都不满足时，执行对应的语句块。else是可选的。
'''

# 1. 基本的if语句
age = 18
if age >= 18:
    print("成年人")
# 输出：成年人

# 2. if-else语句
age = 16
if age >= 18:
    print("成年人")
else:
    print("未成年人")
# 输出：未成年人

# 3. if-elif-else语句
score = 85
if score >= 90:
    print("优秀")
elif score >= 75:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")
# 输出：良好

# 4. 嵌套的if语句
num = 10
if num > 0:
    print("正数")
    if num % 2 == 0:
        print("偶数")
    else:
        print("奇数")
else:
    print("非正数")