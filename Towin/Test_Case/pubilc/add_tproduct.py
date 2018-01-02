from selenium import webdriver
import time

def Add_tproduct(self,pro_name,price):
    driver=self.driver
    driver.find_element_by_xpath('//*[@id="prom"]/a/span[1]').click()
    driver.find_element_by_xpath('//*[@id="tclb"]/a').click()
    js = "document.documentElement.scrollTop=10000"
    driver.execute_script(js)
    driver.find_element_by_class_name('add-btn').click()
    driver.find_element_by_name('tProduct.name').send_keys(pro_name)
    driver.find_element_by_name('tProduct.shopPrice').send_keys(price)
    driver.find_element_by_xpath('//*[@id="addProductForm"]/table/tbody/tr[3]/td[2]/span[1]/input').click()

    #添加单项
    driver.find_element_by_id('select_item_btn').click()
    '''A=driver.currents_window_handle
    driver.switch_to_window(A)'''
    driver.find_element_by_xpath('//*[@id="me1"]/td[1]/input').click()
    #driver.find_element_by_id('select1').click()
    driver.find_element_by_class_name('newaddan1').click()
    js="document.documentElement.scrollTop=10000"
    driver.execute_script(js)
    driver.find_element_by_id('addItems').click()
    time.sleep(2)

    #添加机构
    driver.find_element_by_id('select_shop_btn').click()
    time.sleep(1)
    B = driver.window_handles
    '''for handle in B:
        if handle !=A:
            driver.switch_to_window(handle)'''
    driver.find_element_by_xpath('//*[@id="select3"]').click()
    driver.find_element_by_xpath('//*[@id="selectShop"]/div[2]/div/div[2]/div[2]/a[1]').click()
    js = "document.documentElement.scrollTop=10000"
    driver.execute_script(js)
    driver.find_element_by_id('addShop').click()
    time.sleep(1)
    driver.find_element_by_id('submit-btn').click()
