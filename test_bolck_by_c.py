import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import sys

chrome_options = uc.ChromeOptions()
chrome_options.headless = False  # 设为 True 可无头运行
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--user-data-dir=C:\\Users\\r\\AppData\\Local\\Chromium\\User Data\\Default')

# chrome_options.add_argument('--profile-directory=C:\\Users\\r\\AppData\\Local\\Chromium\\User Data\\Profile 10')

### 如果还是不行，就尝试关闭vpn

chrome_path = r'C:\Program Files\Chromium\Application\chrome.exe'
chrome_options.binary_location = chrome_path

driver = uc.Chrome(driver_executable_path="chromedriver.exe",options=chrome_options, debug=True, port=54805, browser_executable_path=chrome_path)


# 换一个url

# 还是会闪退 crash


# 是什么bug


# 卸载插件后还是会crash 


url = "https://github.com"


# driver.get(url)

time.sleep(200)


driver.close()

driver.quit()


print(2222)
