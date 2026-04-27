import re

# 匹配邮箱的正则表达式
# 注意：尾部的.会在匹配时因$而被选择,[a-zA-Z0-9.-]+中最后一个.会回退
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
test_emails = [
    'user@example.com',
    ' user@example.com',
    'user.name@example.com',
    'user_name@example.com',
    'user@sub.example.com',
    'user@.com',  # 无效
    '@example.com'  # 无效
]

for email in test_emails:
    if re.match(email_pattern, email):
        print(f'{email} 是有效的邮箱')
    else:
        print(f'{email} 是无效的邮箱')