from bs4 import BeautifulSoup

# 打开本地 HTML 文件
with open("C:/Users/r/Desktop/zhuabao2/webofsci/ConvolutionalNeuralNetworks_1.html", "r", encoding="utf-8") as file:
    # 使用 BeautifulSoup 解析 HTML 内容
    soup = BeautifulSoup(file, "lxml")

# 提取所有的 a 标签并获取 href 属性
a_tags = soup.find_all("a")
hrefs = [a.get("href") for a in a_tags if a.get("href")]

# 输出所有 href 属性
for href in hrefs:
    print(href)
