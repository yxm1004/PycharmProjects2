import json
import unittest
import requests
from ApiConstants import ApiConstants
from interfaceTest import readConfig

localReadConfig = readConfig.ReadConfig()
#1、写一个类继承unitest会自动引入的
class testlogin(unittest.TestCase):
    #2、定义一个测试方法test_开头

    def setUp(self):
        c=ApiConstants()
        self.url=
        self.account = localReadConfig.get_OPTION("account")
        self.password = localReadConfig.get_OPTION("password")
        self.headers = {
            'Authorization': 'Basic Y2xvdWRmYWN0b3J5X3dlYjpjbG91ZGZhY3Rvcnlfd2ViX3NlY3JldA==',
            'tenant': 'ZGdnYw==',
            'token': 'Bearer test',
            'Content-Type': 'application/json'
        }
    def test_post_login(self):
        #3、拷贝postman中code
        #获取baseurl
        # baseurl = localReadConfig.get_http("baseurl")
        # url = baseurl+"/api/oauth/noToken/login"
        #获取登录账号
        # account = localReadConfig.get_OPTION("account")
        # password = localReadConfig.get_OPTION("password")
        payload = json.dumps({
            "account": self.account,
            "avatar": "",
            "code": "",
            "grantType": "password",
            "key": "",
            "name": "",
            "openId": "",
            "password": self.password,
            "refreshToken": ""
        })


        response = requests.request("POST", url, headers=self.headers, data=payload)
        if response.status_code==200:
            print(response.json()["data"]["token"])
            return response.json()["data"]["token"]
        else:
            print("failed to get token")
        #4.写一个断言
        self.assertEqual(response.status_code, 200)
#5.验证这个用例
if __name__ == '__main__':
    unittest.main()
