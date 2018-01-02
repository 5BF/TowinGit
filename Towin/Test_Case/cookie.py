from selenium import webdriver
import time


driver=webdriver.Chrome()
driver.maximize_window()

driver.get("http://www.51towin.com/0755")
time.sleep(2)
driver.find_element_by_id('login').click()
time.sleep(2)
driver.find_element_by_id('account').send_keys("13726245005")
driver.find_element_by_id('password').send_keys("123456")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div/div/button').click()

cookie=driver.get_cookies()
print(cookie)