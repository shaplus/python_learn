import re

text = '2023-12-25 是圣诞节，2024-01-01 是元旦'
date_pattern = r'(\d{4})-(\d{2})-(\d{2})'

# 替换为中文日期格式
print('替换前的文本:', text)
result = re.sub(date_pattern, r'\1年\2月\3日', text)
print('替换后的文本:', result)