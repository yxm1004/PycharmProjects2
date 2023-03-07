import unittest
import requests
import json

from interfaceTest.common.ApiConstants import ApiConstants
from interfaceTest.common.GetToken import Token
from interfaceTest import readConfig

localReadConfig = readConfig.ReadConfig()


class confirmComponentAndBom(unittest.TestCase):
    def setUp(self):
        # 引入常量类，直接使用常量类中的url地址
        self.constants = ApiConstants()
        tk = Token()
        self.token = 'Bearer ' + tk.get_token()
        print("self.token-------", self.token)

        #公告头部
        self.headers = {
        'Authorization': 'Basic Y2xvdWRmYWN0b3J5X3dlYjpjbG91ZGZhY3Rvcnlfd2ViX3NlY3JldA==',
        'tenant': 'ZGdnYw==',
        'token': self.token,
        'Content-Type': 'application/json'
    }
    #测试用例get类型测试用例
    def test_get_confirmComponentAndBom(self):
        # key=None
        params={"key":"40dad150ce59444f99a17c78d50d1b2c"}
        response = requests.request("GET", self.constants.CONFIRMCOMPONENTANDBOM_URL, params=params,headers=self.headers)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()#单元测试