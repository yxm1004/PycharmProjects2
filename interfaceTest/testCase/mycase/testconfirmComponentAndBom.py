import unittest
import requests
import json

from interfaceTest.common.ApiConstants import ApiConstants
from interfaceTest.common.GetToken import Token
from interfaceTest import readConfig
from interfaceTest.testCase.mycase.testcomponentsave import testcomponentsave

localReadConfig = readConfig.ReadConfig()


class confirmComponentAndBom(unittest.TestCase):
    global strKey
    def setUp(self):

        # 引入常量类，直接使用常量类中的url地址
        self.constants = ApiConstants()
        tk = Token()
        self.token = 'Bearer ' + tk.get_token()
        print("self.token-------", self.token)

        # 公告头部
        self.headers = {
            'Authorization': 'Basic Y2xvdWRmYWN0b3J5X3dlYjpjbG91ZGZhY3Rvcnlfd2ViX3NlY3JldA==',
            'tenant': 'ZGdnYw==',
            'token': self.token,
            'Content-Type': 'application/json'
        }

    def test_post_componentsave(self):

        payload = json.dumps({
            "bomDetailList": [],
            "rebarWeight": "30.475",
            "projectId": "434",
            "building": "6",
            "floorSegment": "3",
            "type": "叠合板",
            "model": "DHB010",
            "floorCount": "1",
            "appearanceSizeLength": "2500",
            "appearanceSizeWidth": "2320",
            "appearanceSizeThickness": "60",
            "squareAmount": "0.636",
            "weight": "0.255",
            "concreteLabel": "C30",
            "concreteDosage": "0.636"
        })
        response = requests.request("POST", self.constants.COMPONENTSAVE_URL, headers=self.headers, data=payload)
        # 取出响应结果字段
        print("------------------", response.text)
        data = json.loads(response.text)
        # 多级字段取值
        strKey = data["data"]["strKey"]
        print("打印strKey", strKey)

    # 测试用例get类型测试用例
    def test_get_confirmComponentAndBom(self):
        # key=None
        print("queren",strKey)
        response = requests.request("GET", self.constants.CONFIRMCOMPONENTANDBOM_URL, params=strKey,
                                    headers=self.headers)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(confirmComponentAndBom("test_post_componentsave"))
    suite.addTest(confirmComponentAndBom("test_get_confirmComponentAndBom"))
    unittest.TextTestRunner().run(suite)
