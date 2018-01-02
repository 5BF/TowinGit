from selenium import webdriver
import unittest
import time
import xml.dom.minidom
from pubilc import login
from pubilc import add_tproduct


dom=xml.dom.minidom.parse('C:\\Users\\Administrator\\PycharmProjects\\untitled2\\Towin\\Test_Date\\date.xml')
root=dom.documentElement

class ADD(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(2)
        #self.driver.maximize_window()
        logins=root.getElementsByTagName('url')
        self.base_url=logins[0].firstChild.data



    def test_add(self):
        driver=self.driver
        driver.get(self.base_url)
        name=root.getElementsByTagName('username')
        pword=root.getElementsByTagName('password')
        YZM=root.getElementsByTagName('code')
        username=name[0].firstChild.data
        password=pword[0].firstChild.data
        code=YZM[0].firstChild.data
        login.login(self,username,password,code)
        driver.implicitly_wait(2)
        #self.driver.switch_to_alert().accept()
        proname=root.getElementsByTagName('pro_name')
        prices=root.getElementsByTagName('price')
        pro_name=proname[0].firstChild.data
        price=prices[0].firstChild.data
        add_tproduct.Add_tproduct(self,pro_name,price)


    def tearDown(self):
        pass


if __name__=='__main__':
    suite=unittest.TestSuite()
    suite.addTest(ADD('test_add'))


    runner=unittest.TextTestRunner()
    runner.run(suite)










