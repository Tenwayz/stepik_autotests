import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="C:/Users/dgalkin/Documents/Chromedriver/chromedriver.exe")
browser = webdriver.Chrome(service=service)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

url = "https://suninjuly.github.io/alert_accept.html"
browser.get(url)
button = browser.find_element(By.TAG_NAME, "button").click()
confirm = browser.switch_to.alert
confirm.accept()

x = browser.find_element(By.ID, "input_value")
n = x.text
y = calc(n)

otvet = browser.find_element(By.ID, "answer").send_keys(y)
send = browser.find_element(By.TAG_NAME, "button").click()

time.sleep(5)