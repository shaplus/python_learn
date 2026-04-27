import re

text = '访问 https://www.example.com 和 http://test.org 获取更多信息'
url_pattern1 = r'https?://[^\s]+'
url_pattern2 = r'\bhttp[^\s]+\b'

urls = re.findall(url_pattern1, text)
print('url_pattern1', '提取的URL:', urls)
urls = re.findall(url_pattern2, text)
print('url_pattern2', '提取的URL:', urls)
