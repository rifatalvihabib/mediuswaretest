from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from  selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="D:\drivers\chromedriver")
driver.get("https://lms.celt.vip/login")
print(driver.title)
driver.implicitly_wait(5)
username = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[3]/div[1]/input[1]")
#print(username.is_enabled())




username.send_keys("elgunulu@gmail.com")
password = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/input[1]")

password.send_keys("12345678")
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[5]/button[1]").click()



print(driver.title)
driver.implicitly_wait(5)
button = driver.find_element_by_xpath("//body/div[@id='app']/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[13]/a[1]/span[1]")


driver.implicitly_wait(10)
ActionChains(driver).move_to_element(button).click(button).perform()
driver.implicitly_wait(5)
search = driver.find_element_by_xpath("//body/div[@id='app']/div[1]/div[1]/div[3]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]")
search.send_keys("SQA Demo Exam")
driver.implicitly_wait(5)
button1 = driver.find_element_by_xpath("//i[contains(text(),'search')]")
driver.implicitly_wait(5)

ActionChains(driver).move_to_element(button1).click(button1).perform()