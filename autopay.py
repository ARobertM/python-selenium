import os
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

debugging = True
load_dotenv()

ACC_NUMBER = os.getenv('ACC_NUMBER')
LAST_NAME = os.getenv('LAST_NAME')
LOGIN_PAGE = os.getenv('LOGIN_PAGE')

script_directory = Path(__file__).resolve().parent
# Schimbă chrome.exe cu chromedriver.exe
driver_path = script_directory.joinpath('chrome-win64', 'chrome.exe')

service = Service(driver_path)

chrome_options = Options()
if debugging:
    chrome_options.add_experimental_option('detach', True)
    input('Press Enter')
else:
    chrome_options.add_argument('--headless')

driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get(LOGIN_PAGE)
except Exception as e:
    print(f"Error occurred: {e}")

if not debugging:
    driver.quit()

if not debugging:
    driver.quit()
