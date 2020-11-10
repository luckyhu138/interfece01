import logging
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
from selenium import webdriver
from time import sleep
import os
from UI_dev.config_path.path_file import read_file
from UI_dev.model.TimeConversion import return_y_d_m
class TestAdd(unittest.TestCase):



    '''加法测试'''

    def setUp(self):

        print('test add start')



    def test_add3(self):

        driver=webdriver.Firefox()
        driver.get("http://192.168.43.228/phpwind/phpwind/index.php")
        driver.implicitly_wait(30)
        driver.maximize_window()


        driver.find_element_by_link_text("登录").click()
        sleep(3)
        driver.find_element_by_name("pwuser").clear()
        driver.find_element_by_name("pwpwd").clear()

        driver.find_element_by_name("pwuser").send_keys("df3")
        driver.find_element_by_name("pwpwd").send_keys("12356")
        driver.find_element_by_name("submit").click()
        info=driver.find_element_by_id("td_userinfo_more").text
        print(info)
        if "df3" in info:
            print("test_login_001 pass")
        else:
            print("test_login_001 fail")

        driver.quit()

    def test_add4(self):
        driver = webdriver.Firefox()
        driver.get("http://192.168.43.228/phpwind/phpwind/index.php")
        driver.implicitly_wait(30)
        driver.maximize_window()

        driver.find_element_by_link_text("登录").click()
        sleep(3)
        driver.find_element_by_name("pwuser").clear()
        driver.find_element_by_name("pwpwd").clear()

        driver.find_element_by_name("pwuser").send_keys("df3")
        driver.find_element_by_name("pwpwd").send_keys("12345678")
        driver.find_element_by_name("submit").click()
        info = driver.find_element_by_class_name("f_one").text
        print(info)
        if "密码错误或安全问题错误" in info:
            print("test_login_002 pass")
        else:
            print("test_login_002 fail")

        driver.quit()



    def tearDown(self):

        print('add end')



class TestSub(unittest.TestCase):

    def setUp(self):

        print('test sub start')



    def test_sub3(self):
        driver = webdriver.Firefox()
        driver.get("http://192.168.43.228/phpwind/phpwind/index.php")
        driver.implicitly_wait(30)
        driver.maximize_window()

        driver.find_element_by_link_text("登录").click()
        sleep(3)
        driver.find_element_by_name("pwuser").clear()
        driver.find_element_by_name("pwpwd").clear()

        driver.find_element_by_name("pwuser").send_keys("")
        driver.find_element_by_name("pwpwd").send_keys("")
        driver.find_element_by_name("submit").click()
        info = driver.find_element_by_class_name("f_one").text
        print(info)
        if "用户名或密码为空" in info:
            print("test_login_003 pass")
        else:
            print("test_login_003 fail")
        driver.quit()



    def test_sub4(self):
        print("asas")



    def tearDown(self):

        print('test sub end')





