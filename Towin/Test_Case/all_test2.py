from selenium import webdriver
import unittest
from pubilc import Add_product
from pubilc import Check_product
import HTMLTestRunner


suite=unittest.TestSuite()
suite.addTest(Add_product.ADD("test_add"))
suite.addTest((Check_product.Check("test_shenhe")))


if __name__=='__main__':
    runner=unittest.TextTestRunner()
    filename = ('C:\\Users\\Administrator\\PycharmProjects\\untitled2\\Towin\\Report\\result.html')
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=("测试报告"),
        description=("用例执行：")
    )
    runner.run(suite)
    fp.close()