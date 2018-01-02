from selenium import webdriver
import time

def shenhea(self):
    '''这是注释'''
    driver=self.driver
    driver.find_element_by_xpath("/html/body/div[2]/div[1]/ul/li[3]/a/span[1]").click()
    time.sleep(2)
    driver.find_element_by_id('tjtcsh').click()
    checkboxs=driver.find_elements_by_css_selector('input[type=checkbox]')
    for checkbox in checkboxs:
        checkbox.click()
    time.sleep(2)
    driver.find_elements_by_css_selector('input[type=checkbox]').pop(1).click()
    time.sleep(2)
    driver.find_element_by_class_name('btn1').click()
    A=driver.current_window_handle
    driver.switch_to_window(A)
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/a[1]').click()
