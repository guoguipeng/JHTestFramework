'''
Created on 2017年10月24日

@author: Administrator
'''

from selenium import webdriver
import time

def Login(url,username,pd):

    driver = webdriver.Chrome()
    driver.get(url)

    inputuserName = driver.find_element_by_id('username')
    inputuserName.send_keys(username)

    inputPassword = driver.find_element_by_id("password")
    inputPassword.send_keys(pd)

    btLogin = driver.find_element_by_xpath('//*[@id="loginForm"]/table/tbody/tr[3]/td/button')
    btLogin.click()

    time.sleep(5)

    return driver

def Menu(driver,strxpath):
    imageMenu = driver.find_element_by_xpath(strxpath)
    
    imageMenu.click()
    
    return driver
    
    