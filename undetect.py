from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import undetected_chromedriver as uc
import os
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import psutil
import re
title = "ConvolutionalNeuralNetworks"

with open("C:/Users/r/Desktop/zhuabao2/webofsci/ConvolutionalNeuralNetworks_1.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "lxml")

# 获取所有记录链接
all_record_links = soup.find_all("app-summary-record-links")

hrefs = []
for record in all_record_links:
    a_tags = record.find_all("a")
    if len(a_tags) > 1:
        second_a_tag = a_tags[1]
        href = second_a_tag.get("href")
        hrefs.append(href)


if not os.path.exists(title):
    os.makedirs(title)
    print(f"文件夹 '{title}' 已创建。")
else:
    print(f"文件夹 '{title}' 已存在。")

total_links = len(hrefs)



def init_driver():
    chrome_options = uc.ChromeOptions()
    chrome_options.headless = False
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--user-data-dir=C:\\Users\\r\\AppData\\Local\\Chromium\\User Data\\Default')
    chrome_path = r'C:\Program Files\Chromium\Application\chrome.exe'
    chrome_options.binary_location = chrome_path

    driver = uc.Chrome(driver_executable_path="chromedriver.exe", options=chrome_options, browser_executable_path=chrome_path)
    return driver


def kill_process_by_port(port):
    """
    Finds and kills processes listening on the given port.
    """
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        try:
            # Check if the process has any open connections
            if hasattr(proc, 'connections'):
                for conn in proc.connections(kind='inet'):  # 'inet' for network connections
                    if conn.laddr.port == port:
                        print(f"Killing process {proc.info['name']} with PID {proc.info['pid']} on port {port}")
                        proc.kill()
                        print(f"Process {proc.info['name']} with PID {proc.info['pid']} terminated successfully.")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # These exceptions can occur if a process ends before we access its info
            pass

driver = init_driver()

for index, current_url in enumerate(hrefs):
    
    
    
    start = current_url.find("KeyAID=") + len("KeyAID=")

    end = current_url.find("&", start)
    
    if end == -1:
        end = len(current_url)
    
    
    doi = current_url[start:end]

    standard_url = f"https://doi.org/{doi}"

    save_path = f"C:/Users/r/Desktop/zhuabao2/{title}/{title}_{doi}.html"

    if os.path.exists(save_path):
        print(f"文件 {save_path} 已存在，跳过保存。")

        continue

    MAX_RETRIES = 20
    
    retry_count = 0

    success = False

    while retry_count < MAX_RETRIES and not success:
        try:
            print(current_url)
            driver.get(current_url)
            
            # 等待页面加载完成
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            
            try:
                user_agent_element = driver.find_element(By.ID, "userAgent")
                if user_agent_element:
                    print("检测到 'userAgent' 页面内容，请手动处理后按回车继续...")
                    input("按回车键继续")
            except:
                print("没有检测到 'userAgent' 元素，继续执行...")

                
            last_height = driver.execute_script("return document.body.scrollHeight")
            scroll_steps = 30
            scroll_increment = last_height / scroll_steps  # 每次滚动的高度

            for i in range(scroll_steps):
                driver.execute_script(f"window.scrollTo(0, {scroll_increment * (i + 1)});")
                time.sleep(0.1)
            
            page_source = driver.page_source
            with open(save_path, "w", encoding="utf-8") as file:
                file.write(page_source)

            print(f"成功保存页面: {save_path}")
            success = True  

        except Exception as e:
            print(f"加载页面出错: {e}")

            match = re.search(r"(\d+)", str(e))  # Extracts the number (port) from the exception message
            if match:
                port = int(match.group(1))  # Convert the matched port to an integer
            kill_process_by_port(port)  # Call the function to kill the process on that port

            retry_count += 1  # 增加重试次数
            print(f"正在尝试重新启动浏览器并重试 ({retry_count}/{MAX_RETRIES})...")

            # 如果重试次数超过最大限制，退出
            if retry_count >= MAX_RETRIES:
                print(f"重试次数达到最大值 ({MAX_RETRIES})，跳过当前链接。")
                break

            # 关闭当前浏览器实例
            driver.quit()

            driver = init_driver()

   

driver.quit()
