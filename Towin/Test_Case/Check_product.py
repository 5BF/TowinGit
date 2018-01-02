from selenium import webdriver
import unittest
import xml.dom.minidom
from pubilc import login
from pubilc import shenhe

dom=xml.dom.minidom.parse('C:\\Users\\Administrator\\PycharmProjects\\untitled2\\Towin\\Test_Date\\date.xml')
root=dom.documentElement

class Check(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(2)
        logins=root.getElementsByTagName('twurl')
        self.twbase_url=logins[0].firstChild.data


    def test_shenhe(self):
        driver = self.driver
        driver.get(self.twbase_url)
        name2 = root.getElementsByTagName('twusername2')
        twusername = name2[0].firstChild.data
        paword2 = root.getElementsByTagName('twpassword2')
        twpassword = paword2[0].firstChild.data
        code = root.getElementsByTagName('twcode2')
        twcode = code[0].firstChild.data
        login.twlogin(self, twusername, twpassword, twcode)
        shenhe.shenhea(self)
        driver.implicitly_wait(2)

    def tearDown(self):
        pass
if __name__=='__main__':
    suite=unittest.TestSuite()
    suite.addTest(Check("test_shenhe"))

    runner=unittest.TextTestRunner
    runner.run(suite)