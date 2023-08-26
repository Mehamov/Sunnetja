from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import tkinter as tk
import names
import secrets
import random
import string
import os
from selenium.webdriver.common.by import By


chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

r1 = ''.join(random.choices(string.ascii_lowercase +string.ascii_uppercase, k=random.randint(3,4)))

r2=''.join(random.choices(string.digits, k=random.randint(3,5)))

pas=r1+r2





N = 7
# using random.choices()
# generating random strings
res = ''.join(random.choices(string.ascii_lowercase +string.ascii_uppercase, k=28))

res1=''.join(random.choices(string.digits, k=4))

res0=''.join(random.choices(string.ascii_uppercase, k=1))

nl = ( str(res1) + str(res))
fbl = random.sample(nl,k=32)
def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1
tr=(listToString(fbl))
trx=('T'+str(res0)+tr)









driver.get('https://minetrx.pro/?ref=340605')
time.sleep(10)




driver.find_element(By.XPATH, value="//input[@id='wallet']"
 ).send_keys(trx)
time.sleep(3)
driver.find_element(By.XPATH, value= "//button[@id='continue-button']").click()

driver.find_element(By.XPATH, value= "//div[@id='password-section']//input[1]").send_keys(pas)
time.sleep(4)
driver.find_element(By.XPATH, value= "//button[@id='submit-button']").click()
time.sleep(25)



