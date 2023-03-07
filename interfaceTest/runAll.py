# -*- coding: utf-8 -*-
import time
from datetime import datetime
import os

# import HtmlTestRunner

import readConfig

import unittest

from common import HTMLTestRunner
from common.EmailSend import EmailSender
from common.Logger import Logger

# 日志处理

logger = Logger()
resultPath = os.path.join(readConfig.proDir, "result")
resultPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))

resultPath = os.path.join(resultPath, "test_result.html")
rr = os.path.join(os.path.join(readConfig.proDir, "result"), "test_result1.html")


class runAll:

    def __init__(self, case_list_file):
        self.caseListFile = case_list_file
        self.caseList = []

    def set_case_list(self):
        fb = open(self.caseListFile)
        for value in fb.readlines():
            data = str(value)
            print(data)
            if data != '' and not data.startswith("#"):
                self.caseList.append(data.replace("\n", ""))
                print("打印list", self.caseList)
        fb.close()

    def set_case_suite(self):
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_model = []
        for case in self.caseList:
            case_file = os.path.join(readConfig.proDir, "testCase")
            case_name = case.split("/")[-1]
            print("测试文件名", case_name + ".py")
            discover = unittest.defaultTestLoader.discover(case_file, pattern=case_name + '.py', top_level_dir=None)
            suite_model.append(discover)
        if len(suite_model) > 0:
            for suite in suite_model:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None
        return test_suite

    def run(self):
        try:
            suit = self.set_case_suite()
            if suit is not None:
                logger.info("********TEST START********")
                fp = open(resultPath, 'wb')
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告', description="测试描述")
                runner.run(suit)
            else:
                logger.info("Have no case to test.")
        except Exception as ex:
            logger.error(str(ex))
        finally:
            logger.info("*********TEST END*********")
            # # send test report by email
            #
            # if int(on_off) == 0:
            # 等待测试报告文件生成,有缺陷，测试报告还未写入就发送了邮件，导致附件是空。后期再处理
            # while not os.path.exists(resultPath):
            #     time.sleep(1)
            # email = EmailSender()
            # email.send_email(rr)
            # # elif int(on_off) == 1:
            # #     logger.info("Doesn't send report email to developer.")
            # # else:
            # logger.info("Unknow state.")


if __name__ == "__main__":
    # this code will only be executed if this script is run directly
    myclass = runAll("caselist.txt")
    myclass.run()
