from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By
import time

print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
driver = webdriver.Chrome('./chromedrived')
driver.get("https://visagrader.com/trackers/us-drop-box-visa-appointments")

print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

print('Going to sleep')
time.sleep(5)


for i in range(1 , 10):
    link = driver.find_element(By.LINK_TEXT,f"{i}")
    link.click()
    time.sleep(5)
    data = driver.find_element(By.ID, "dataTable")

    sample = data.text.splitlines()
    for line in sample:
        if "H1B Chennai, India" in line:
            print(line)



print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))





driver.quit()