import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

# ✅ 设置 Chrome 配置
chrome_options = uc.ChromeOptions()
chrome_options.headless = False  # 设为 True 可无头运行
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')

# ✅ 指定 Chromium 浏览器路径
chrome_path = r'C:\ungoogled-chromium-windows\build\ungoogled-chromium_131.0.6778.85-1.1_windows_x64\ungoogled-chromium_131.0.6778.85-1.1_windows_x64\chrome.exe'
chrome_options.binary_location = chrome_path


# ✅ 启动 undetected_chromedriver
driver = uc.Chrome(driver_executable_path="chromedriver.exe",options=chrome_options, browser_executable_path=chrome_path)

# ✅ 打开 Web of Science
url = "https://webofscience.clarivate.cn/wos/alldb/basic-search"
driver.get(url)
time.sleep(5)

try:
    # ✅ 查找并点击同意按钮
    consent_button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    consent_button.click()
    print("✅ 同意隐私政策按钮已点击。")
except Exception as e:
    print("⚠️ 未找到同意按钮，跳过。")

# ✅ 查找并输入搜索框
search_box = driver.find_element(By.ID, "search-option")
search_box.send_keys("Convolutional Neural Networks")
search_box.send_keys(Keys.RETURN)  # 模拟按下回车键
from selenium.webdriver.support.ui import WebDriverWait
# 等待页面加载完成
WebDriverWait(driver, 30).until(
    lambda driver: driver.execute_script("return document.readyState") == "complete"
)

# 模拟滚动到底部，直到页面不再加载
last_height = driver.execute_script("return document.body.scrollHeight")

# 设置每次滚动的次数
scroll_steps = 30
scroll_increment = last_height / scroll_steps  # 每次滚动的高度

for i in range(scroll_steps):
    driver.execute_script(f"window.scrollTo(0, {scroll_increment * (i + 1)});")
    time.sleep(2)  # 设置每次滚动后的等待时间



time.sleep(2)  # 确保所有内容都加载完


# ✅ 获取所有符合条件的链接
links = driver.find_elements(By.XPATH, "//a")

import re

# 打开文件以写入链接
with open("links.txt", "w", encoding="utf-8") as file:
    # 提取并保存所有 href
    for link in links:
        outer_html = link.get_attribute("outerHTML")  # 获取完整的 HTML 代码
        if outer_html:
            # 使用正则表达式提取所有 href
            hrefs = re.findall(r'href=["\'](https?://[^"\']+)["\']', outer_html)
            for href in hrefs:
                file.write(href + "\n")  # 写入到文件，并换行
                print(href)  # 如果你还想在控制台看到输出，可以保留这行

print("所有链接已保存到 links.txt 文件中。")



time.sleep(5000)  # 让浏览器保持打开
