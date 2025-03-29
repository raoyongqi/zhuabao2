from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import undetected_chromedriver as uc
import os
import sys
title = "ConvolutionalNeuralNetworks"

with open("C:/Users/r/Desktop/zhuabao2/webofsci/ConvolutionalNeuralNetworks_1.html", "r", encoding="utf-8") as file:

    soup = BeautifulSoup(file, "lxml")

all_record_links = soup.find_all("app-summary-record-links")

hrefs = []
for record in all_record_links:
    a_tags = record.find_all("a")
    
    if len(a_tags) > 1:
        second_a_tag = a_tags[1]
        href = second_a_tag.get("href")
        hrefs.append(href)

chrome_options = uc.ChromeOptions()
chrome_options.headless = False  # 设为 True 可无头运行
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--user-data-dir=C:\\Users\\r\\AppData\\Local\\Chromium\\User Data\\Default')
chrome_path = r'C:\Users\r\Desktop\zhuabao\chrome-headless-shell-win64\chrome-headless-shell-win64\chrome-headless-shell.exe'
chrome_options.binary_location = chrome_path

single_file_path = r"C:\Users\r\Desktop\zhuabao2\single-file.exe"  # 指定 full path to single-file.exe

if not os.path.exists(title):
    os.makedirs(title)
    print(f"文件夹 '{title}' 已创建。")
else:
    print(f"文件夹 '{title}' 已存在。")


total_links = len(hrefs)  # 总共有多少链接

for index, current_url in enumerate(hrefs):

    start = current_url.find("KeyAID=") + len("KeyAID=")
    end = current_url.find("&", start)
    if end == -1:
        end = len(current_url)  # 如果是最后一个链接，end应该为字符串的结尾
    doi = current_url[start:end]
    
    standard_url = f"https://doi.org/{doi}"
    
    
    save_path = f"C:/Users/r/Desktop/zhuabao2/{title}/{title}_{doi}.html"

    print(f'{single_file_path} --browser-arg --user-data-dir="C:\\Users\\r\\AppData\\Local\\Chromium\\User Data\\Default" "{current_url}" {save_path}')


    exit_code = os.system(f'{single_file_path} --browser-arg --user-data-dir="C:\\Users\\r\\AppData\\Local\\Chromium\\User Data\\Default" "{current_url}" {save_path}')

    if exit_code != 0:
        print(f"Error: The command failed with exit code {exit_code}. Stopping the script.")
        sys.exit(1)
    else:
        print(f"Successfully processed: {current_url}")

    remaining = total_links - (index + 1)

    print(f"已完成 {index + 1}/{total_links}，还剩 {remaining} 个链接未处理。")
