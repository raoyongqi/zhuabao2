import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import sys
log_path = 'chrome_debug.log'
chrome_options = uc.ChromeOptions()
chrome_options.headless = False  # 设为 True 可无头运行
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--naro-sandbox')
## 某些add_argument可能会导致意想不到的错误


chrome_options.add_argument('--user-data-dir=C:\\Users\\r\\AppData\\Local\\Chromium\\User Data\\Default')
chrome_options.add_argument(f'--log-path={log_path}')
# chrome_options.add_argument('--profile-directory=C:\\Users\\r\\AppData\\Local\\Chromium\\User Data\\Profile 10')


chrome_path = r'C:\ungoogled-chromium-windows\build\ungoogled-chromium_131.0.6778.85-1.1_windows_x64\ungoogled-chromium_131.0.6778.85-1.1_windows_x64\chrome.exe'

chrome_options.binary_location = chrome_path

driver = uc.Chrome(driver_executable_path="chromedriver.exe",options=chrome_options, debug=True, browser_executable_path=chrome_path)


# 换一个url

# 还是会闪退 crash# 是什么bug
# 卸载插件后还是会crash 
time.sleep(1000)

url = "https://github.com"
driver.get(url)
time.sleep(10)

driver.quit()



time.sleep(50)




print(2222)
