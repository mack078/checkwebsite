from selenium import webdriver
import time
import requests
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://XXX/")


driver.find_element_by_class_name('popup-close').click()
username = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div/form/div/div[1]/input").send_keys("rdtest1")
password = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div/form/div/div[2]/input").send_keys("123456")

driver.find_element_by_class_name("btn-top-login").submit()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div[3]/button").click()
time.sleep(1)
driver.find_element_by_link_text("体育").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]").click()
driver.switch_to.window(driver.window_handles[1])
url = driver.current_url
print(url)
r = requests.get(url)
print(r.status_code)
