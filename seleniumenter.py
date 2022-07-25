from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\\Users\\admin\\Downloads\\chromedriver_win32 (1)\\chromedriver")
driver=webdriver.Chrome(service=serv_obj)   #declaringdriverandaccessitfromdevicelocation
driver.get("https://opensource-demo.orangehrmlive.com/")    #link of the website
print(driver.title)   #title of the page
print(driver.current_url)    #FetchesURL
driver.find_element(By.NAME,"txtUsername").send_keys("Admin")
driver.find_element(By.ID,"txtPassword").send_keys("admin123")
driver.find_element(By.ID,"btnLogin").click()   #click login on the page

act_title=driver.title   #getactualsitetitleascharvariable
exp_title="OrangeHRM"      #declareexpectedtitleascharvariable
if act_title==exp_title:
    print("LOGIN TEST PASS")      #verify thatactualtitleissameas expectedtitle
else:
    print("LOGIN TEST FAIL")
driver.close()