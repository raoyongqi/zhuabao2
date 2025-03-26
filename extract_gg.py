from bs4 import BeautifulSoup

# 假设你已经有一个 HTML 内容（可以从本地文件或者网页获取）
# 本地 HTML 文件路径
file_path = 'exts.ggplot2.tidyverse.org.htm'

# 打开并读取本地 HTML 文件
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

    # 解析网页内容
    soup = BeautifulSoup(html_content, 'html.parser')
    

# 查找所有符合条件的 div 标签
divs = soup.find_all('div', class_='card-content widget-content')
from urllib.parse import urlparse
# 创建一个文本文件来保存链接
hosts = set()

# 创建一个文本文件来保存链接
with open('output_links.txt', 'w', encoding='utf-8') as file:
    for div in divs:
        # 获取每个 div 标签中的第一个 <a> 标签
        first_a_tag = div.find('a')
        
        # 如果找到了 <a> 标签，提取 href 属性
        if first_a_tag:
            href = first_a_tag.get('href')
            # 提取链接的 host（域名）
            parsed_url = urlparse(href)
            host = parsed_url.netloc  # netloc 提取的是域名部分

            hosts.add(host)
            


import json
js_content_new = f"""
const allowedUrls = {json.dumps(list(hosts), ensure_ascii=False, indent=4)};

"""

# 将生成的新内容写入到文件中
with open('newbackground.js', 'w', encoding='utf-8') as js_file:
    js_file.write(js_content_new)

print("Combined and de-duplicated hosts saved to newbackground.js")
