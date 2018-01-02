from selenium import webdriver
import unittest
from pubilc import add_product
from pubilc import login
import xml.dom.minidom

dom=xml.dom.minidom.parse('C:\\Users\\Administrator\\PycharmProjects\\untitled2\\Towin\\Test_Date\\date.xml')
root=dom.documentElement

class ADD_product(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
        logins=root.getElementsByTagName('url')
        url=logins[0].firstChild.data
        self.driver.get(url)
    def test_add_product(self):
        driver=self.driver
        #登录
        name=root.getElementsByTagName('username')
        paword=root.getElementsByTagName('password')
        code=root.getElementsByTagName('code')
        username=name[0].firstChild.data
        password=paword[0].firstChild.data
        yzm=code[0].firstChild.data
        login.login(self,username,password,yzm)
        #新增套餐
        proname=root.getElementsByTagName('pro_name')
        pri1=root.getElementsByTagName('price1')
        pri2=root.getElementsByTagName('price2')
        pro_name=proname[0].firstChild.data
        price1=pri1[0].firstChild.data
        price2=pri2[0].firstChild.data
        add_product.add_product(self,pro_name,price1,price2)


    def tearDown(self):
        pass

if __name__=='__main__':
    suite=unittest.TestSuite()
    suite.addTest(ADD_product('test_add_product'))

    runner=unittest.TextTestRunner()
    runner.run(suite)













