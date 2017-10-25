'''
Created on 2017年10月24日

@author: Administrator
'''
from selenium import webdriver
from Base import Base
from HTMLTestRunner import HTMLTestRunner

import unittest

class TestMenuSuite(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.99.100:18180/jhCountyCloud"
        
    def menu_testcase_1100(self):
        driver = Base.Login(self.base_url, "admin", "888888")   
        
        driver = Base.Menu(driver,'//*[@id="bs-example-navbar-collapse-1"]/ul[1]/li[5]/a')
        
        self.assertEqual(u"工作平台的首页", driver.title)
        
    def menu_testcase_1101(self):
        driver = Base.Login(self.base_url, "admin", "888888")   
        
        driver = Base.Menu(driver,'//*[@id="bs-example-navbar-collapse-1"]/ul[1]/li[4]/a')
        driver = Base.Menu(driver,'//*[@id="bs-example-navbar-collapse-1"]/ul[1]/li[4]/ul/li[1]/a')
        
        self.assertEqual(u"病虫图谱", driver.title)
         
    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    #构造测试套件
    testsuit = unittest.TestSuite()
    testsuit.addTest(TestMenuSuite("menu_testcase_1100"))
    testsuit.addTest(TestMenuSuite("menu_testcase_1101"))
    #定义测试报告存放路径
    filename = 'E:\\result.html'
    fp = open(filename,'wb')
    #定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title='自动化测试报告',
                            description='用例执行情况：')
    runner.run(testsuit)
    #关闭测试报告
    fp.close()