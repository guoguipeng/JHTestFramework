'''
Created on 2017年10月24日

@author: Administrator
'''


from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
from Base import Base
from Menu import Menu

import unittest
import time

class TestUserManageSuite(unittest.TestCase):
    
    def setUp(self):
        #self.driver = webdriver.Chrome()
        #self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.99.100:18180/jhCountyCloud"
        
    def usermanage_testcase_2336(self):

        driver = Base.Login(self.base_url, "admin", "888888")   
        driver = Base.Menu(driver,'//*[@id="bs-example-navbar-collapse-1"]/ul[1]/li[5]/a')
        
        print("点击权限管理")
        driver = Base.Menu(driver,'//*[@id="bbbNav"]/h1[4]/a')
        time.sleep(3)
        print("点击用户管理")
        driver = Base.Menu(driver,'//*[@id="bbbNav"]/ul[4]/li[4]')
        time.sleep(3)

        driver.find_element_by_id('ser_username').send_keys('001')
        driver.find_element_by_xpath('//*[@id="searchForm"]/button').click()
        
        
        time.sleep(3)
        strNum = driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[3]/div[1]/div[1]/span/span').text
        print(strNum)
        
        self.assertEqual('4', strNum)
        
    def usermanage_testcase_2337(self):
        driver = Base.Login(self.base_url, "admin", "888888")   
        driver = Base.Menu(driver,'//*[@id="bs-example-navbar-collapse-1"]/ul[1]/li[5]/a')
        
        print("点击权限管理")
        driver = Base.Menu(driver,'//*[@id="bbbNav"]/h1[4]/a')
        time.sleep(3)
        print("点击用户管理")
        driver = Base.Menu(driver,'//*[@id="bbbNav"]/ul[4]/li[4]')
        time.sleep(3)

        driver.find_element_by_id('ser_username').send_keys('001')
        driver.find_element_by_xpath('//*[@id="searchForm"]/button').click()
        
        
        time.sleep(3)
        strNum = driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[3]/div[1]/div[1]/span/span').text
        print(strNum)
        
        self.assertEqual('4', strNum)
         
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    #构造测试套件
    testsuit = unittest.TestSuite()
    testsuit.addTest(TestUserManageSuite("usermanage_testcase_2336"))
    testsuit.addTest(TestUserManageSuite("usermanage_testcase_2337"))
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