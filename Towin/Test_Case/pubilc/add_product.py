from selenium import webdriver
import unittest
import time
import os

def add_product(self,pro_name,price1,price2):
    driver=self.driver
    driver.find_element_by_xpath('//*[@id="prom"]/a/span[1]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="grtclb"]/a').click()
    driver.find_element_by_class_name("add-btn").click()
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/form/table/tbody/tr[1]/td[2]/input').send_keys(pro_name)
    driver.find_element_by_name('payType').click()
    driver.find_element_by_id('market-price').send_keys(price1)
    driver.find_element_by_id('shop-price').send_keys(price2)
    driver.find_element_by_xpath('//*[@id="addProductForm"]/table/tbody/tr[4]/td[2]/span/input[1]').click()
    driver.find_element_by_xpath('//*[@id="addProductForm"]/table/tbody/tr[5]/td[2]/label[1]/input').click()
    driver.find_element_by_class_name('inputk1').click()
    driver.find_element_by_xpath('//*[@id="addProductForm"]/table/tbody/tr[6]/td[2]/div/p[1]').click()
    js="document.documentElement.scrollTop=500"
    driver.execute_script(js)
    # 上传图片
    driver.find_element_by_id('previewImg0').click()
    os.system("C:\\Users\\Administrator\\PycharmProjects\\untitled2\\Towin\\UpPicture.exe")
    js = "document.documentElement.scrollTop=200"
    driver.execute_script(js)
    driver.find_element_by_xpath('//*[@id="addProductForm"]/table/tbody/tr[8]/td[2]/label[2]/input').click()
    driver.find_element_by_xpath('//*[@id="addProductForm"]/table/tbody/tr[9]/td[2]/label[1]/input').click()
    driver.find_element_by_id('select_item_btn').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="select1"]').click()
    time.sleep(2)
    driver.find_element_by_class_name('newaddan1').click()
    js2='document.documentElement.scrollTop=500'
    driver.execute_script(js2)
    time.sleep(2)
    driver.find_element_by_id('addItems').click()
    time.sleep(2)
    driver.find_element_by_id('select_shop_btn').click()
    time.sleep(2)
    driver.find_element_by_id('ed1556').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="selectShop"]/div[2]/div/div[2]/div[2]/a[1]').click()
    time.sleep(2)
    js3='document.documentElement.scrollTop=500'
    driver.execute_script(js3)
    driver.find_element_by_id('addShop').click()
    time.sleep(2)
    js4='document.documentElement.scrollTop=10000'
    driver.execute_script(js4)
    driver.find_element_by_id('addProduct').click()





