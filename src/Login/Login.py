'''
Created on 2017年10月23日

@author: Administrator
'''

from selenium import webdriver
from Base import Base
from HTMLTestRunner import HTMLTestRunner

import time
import unittest

class TestLoginSuite(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.99.100:18180/jhCountyCloud"
        
    def login_testcase_1099(self):
        driver = Base.Login(self.base_url, "admin", "888888")   
    
        self.assertEqual(u"物联网", driver.title)
    
    def login_testcase_1100(self):
        driver = Base.Login(self.base_url, "admin", "admin")   
        
        element = driver.find_element_by_xpath('/html/body/div/div/div/div/div/table/tbody/tr/td[2]/div')
        time.sleep(10)
        
        self.assertEqual(u"用户名或密码错误！", element.text)
     
    def login_testcase_1101(self):
        driver = Base.Login(self.base_url, "", "admin")   
        
        element = driver.find_element_by_xpath('/html/body/div/div/div/div/div/table/tbody/tr/td[2]/div')
        time.sleep(10)
        
        self.assertEqual(u"请填写登录名", element.text)
        
    def login_testcase_1102(self):
        driver = Base.Login(self.base_url, "admin", "")   
        
        element = driver.find_element_by_xpath('/html/body/div/div/div/div/div/table/tbody/tr/td[2]/div')
        time.sleep(10)
        
        self.assertEqual(u"请填写登录密码", element.text)
        
    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    #构造测试套件
    testsuit = unittest.TestSuite()
    testsuit.addTest(TestLoginSuite("login_testcase_1099"))
    testsuit.addTest(TestLoginSuite("login_testcase_1100"))
    testsuit.addTest(TestLoginSuite("login_testcase_1101"))
    testsuit.addTest(TestLoginSuite("login_testcase_1102"))
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
