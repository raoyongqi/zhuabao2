import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service  # 导入 Service
import time

# Set up logging
log_path = 'chrome_debug.log'

# Set up the logger for selenium
logger = logging.getLogger('selenium')
logger.setLevel(logging.DEBUG)  # Set the level to DEBUG to capture all log messages
file_handler = logging.FileHandler(log_path)  # Save logs to a file
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Set up Chrome options
chrome_options = Options()
chrome_options.headless = False  
chrome_options.add_argument(f'--log-path={log_path}')
chrome_options.add_argument('--user-data-dir=C:\\Users\\r\\AppData\\Local\\Chromium\\User Data\\Default')

# 如果弹出用户框就完蛋了


# chrome_options.add_argument('--profile-directory=C:\\Users\\r\\AppData\\Local\\Chromium\\User Data\\Profile 1')
chrome_options.add_argument("--ignore-certificate-errors")
chrome_path = r'C:\ungoogled-chromium-windows\build\ungoogled-chromium_131.0.6778.85-1.1_windows_x64\ungoogled-chromium_131.0.6778.85-1.1_windows_x64\chrome.exe'

chrome_options.binary_location = chrome_path

# Create a Service instance for ChromeDriver
service = Service(executable_path="chromedriver.exe")

# Initialize WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Log a message when the browser is started
logger.info('ChromeDriver started successfully.')

# Wait for a while
time.sleep(500)

# Log a message when the script ends
logger.info('Script completed.')

# Close the browser after the wait time
driver.quit()
