from selenium import webdriver
import unittest
import Add_tproduct
import Check_product
import Add_product
import HTMLTestRunner
import time


suite=unittest.TestSuite()
suite.addTest(Add_tproduct.ADD("test_add"))
suite.addTest((Check_product.Check("test_shenhe")))
suite.addTest(Add_product.ADD_product("test_add_product"))


if __name__=='__main__':
    runner=unittest.TextTestRunner()
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    filename = ('C:\\Users\\Administrator\\PycharmProjects\\untitled2\\Towin\\Report\\'+now+'result.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=("测试报告"),
        description=("用例执行：")
    )
    runner.run(suite)
    fp.close()