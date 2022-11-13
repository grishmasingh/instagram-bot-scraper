from dotenv import load_dotenv
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


load_dotenv()

USERNAME ='' #put in insta account
PASSWORD=''

# USERNAME = os.environ['USERNAME']
# PASSWORD = os.environ['PASSWORD']


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()

insta_url = "https://www.instagram.com/"
driver.get(insta_url)

sleep(2)

username_field  = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.NAME, 'username')))
username_field[0].send_keys(USERNAME)

sleep(1)

password_field  = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.NAME, 'password')))
password_field[0].send_keys(PASSWORD)

sleep(1)

login_button = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/button')))
login_button[0].click()

driver.get(insta_url + 'neymarjr')
sleep(5)

ul =  WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'ul')))

items = ul.find_elements_by_tag_name('li')

for li in items:
    print(li.text)
