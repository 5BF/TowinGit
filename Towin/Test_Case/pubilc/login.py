from selenium import webdriver

def login(self,username,password,code):
    driver=self.driver
    driver.find_element_by_id("account").clear()
    driver.find_element_by_id("account").send_keys(username)
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("yzm").send_keys(code)
    driver.find_element_by_class_name("btn").click()


def twlogin(self,twusername,twpassword,twcode):
    driver=self.driver
    driver.find_element_by_id("account").clear()
    driver.find_element_by_id("account").send_keys(twusername)
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys(twpassword)
    driver.find_element_by_id("yzm").send_keys(twcode)
    driver.find_element_by_class_name("btn").click()
