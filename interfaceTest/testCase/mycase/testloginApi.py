import json
import unittest
import requests
from interfaceTest.common.ApiConstants import ApiConstants
from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()


# 1、写一个类继承unitest会自动引入的
class testlogin(unittest.TestCase):
    # 2、setUp初始话数据引入API接口

    def setUp(self):
        self.account = localReadConfig.get_OPTION("account")
        self.password = localReadConfig.get_OPTION("password")
        self.loginApi = loginApi()
    #编写测试用力和断言
    def test_post_login(self):
        response = self.loginApi.login(self.account, self.password)
        #打印token
        if response.status_code == 200:
            print("login接口",response.json()["data"]["token"])
            return response.json()["data"]["token"]
        else:
            print("failed to get token")
        self.assertEqual(response.status_code, 200)
    # def test_post_getToken(self):
    #     tk = self.loginApi.getToken(self.account, self.password)
    #     #打印token
    #     print("获取token",tk)
    #     self.assertIsNotNone(tk)

# 5.验证这个用例
if __name__ == '__main__':
    unittest.main()
