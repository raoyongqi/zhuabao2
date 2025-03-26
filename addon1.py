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
chrome_options.add_argument('--user-data-dir=C:\\Users\\r\\AppData\\Local\\Chromium\\User Data\\Default')
# chrome_options.add_argument('--profile-directory=C:\\Users\\r\\AppData\\Local\\Chromium\\User Data\\Profile 10')
# ✅ 指定 Chromium 浏览器路径
chrome_path = r'C:\Program Files\Chromium\Application\chrome.exe'
chrome_options.binary_location = chrome_path



# ✅ 启动 undetected_chromedriver
driver = uc.Chrome(driver_executable_path="chromedriver.exe",options=chrome_options, browser_executable_path=chrome_path)

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

search_box = driver.find_element(By.ID, "search-option")


keys = "Convolutional Neural Networks"

search_box.clear() 

search_box.send_keys(keys)  # 然后输入新的内容

search_box.send_keys(Keys.RETURN)  # 模拟按下回车键

from selenium.webdriver.support.ui import WebDriverWait

WebDriverWait(driver, 30).until(
    lambda driver: driver.execute_script("return document.readyState") == "complete"
)

time.sleep(5)

page = 1

keys_no_spaces = keys.replace(" ", "")

save_path = f"C:\\Users\\r\\Desktop\\zhuabao2\\webofsci\\{keys_no_spaces}_{page}.html"

single_file_path = r"C:\Users\r\Desktop\zhuabao2\single-file.exe"  # 指定 full path to single-file.exe

current_url = driver.execute_script("return window.location.href;")

folder_path = 'webofsci'

if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"文件夹 '{folder_path}' 已创建。")
else:
    print(f"文件夹 '{folder_path}' 已存在。")

print(f'{single_file_path} {current_url} {save_path}')

#  务必配置chrome路径在C:\\Program Files\\Chromium\\Application\\chrome.exe

# 搞一下数据文件


# C:\Users\r\AppData\Local\Chromium\User Data
# 关闭浏览器


driver.quit()
# 如果不关闭浏览器，注定报错


os.system(f'{single_file_path} --browser-arg --user-data-dir="C:\\Users\\r\\AppData\\Local\\Chromium\\User Data\\Default" {current_url} {save_path}')


