from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
driver.find_element(By.NAME,"q").send_keys("Lenovo Thinkpad")