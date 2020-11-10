import unittest
import HTMLTestRunner
import os
import logging
import re
import time
import string
class runItAll(unittest.TestCase):
    def getTestCase(self):
        self.proDir=os.path.dirname(os.path.dirname(__file__))
        case_file = os.path.join(self.proDir,'interface_1',"testCase").replace('\\','/')
        fb = os.listdir(case_file)
        # 创建测试套件。。0



        suite = unittest.TestSuite()

        # 指定识别测试用例的规则
        tests = unittest.defaultTestLoader.discover(case_file, pattern = 'test*.py')
        # 识别所有test开头的py文件为测试用例
        # 按模块名顺序执行

        suite.addTest(tests)
        return suite




    def run(self):
        try:
            suit = self.getTestCase()
            if suit is not None:
                logging.getLogger().info("********TEST START********")
                now = time.strftime("%Y-%m-%d_%H_%M_%S")
                path=os.path.join(os.path.dirname(os.path.dirname(__file__)),'interface_1','result','').replace('\\','/')
                fp = open(path + now + "result.html", 'wb')
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
                runner.run(suit)
            else:
                logging.info("Have no case to test.")
        except Exception as ex:
            logging.error(str(ex))
        finally:
            logging.info("*********TEST END*********")



print(runItAll().run())