import unittest
import requests
import json

from interfaceTest.common.ApiConstants import ApiConstants
from interfaceTest.common.GetToken import Token
from interfaceTest import readConfig
from interfaceTest.testCase.mycase.testcomponentsave import testcomponentsave

localReadConfig = readConfig.ReadConfig()


class confirmComponentAndBom(unittest.TestCase):
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
        payload = json.dumps({
            "bomDetailList": [],
            "rebarWeight": "30.475",
            "projectId": "434",
            "building": "6",
            "floorSegment": "3",
            "type": "叠合板",
            "model": "DHB014",
            "floorCount": "1",
            "appearanceSizeLength": "2500",
            "appearanceSizeWidth": "2320",
            "appearanceSizeThickness": "60",
            "squareAmount": "0.636",
            "weight": "0.255",
            "concreteLabel": "C30",
            "concreteDosage": "0.636"
        })
        #保存构件信息
        response = requests.request("POST", self.constants.COMPONENTSAVE_URL, headers=self.headers, data=payload)
        data = json.loads(response.text)
        #提取strKey
        self.strKey = data["data"]["strKey"]
        print(self.strKey)


    # 测试用例get类型测试用例
    def test_get_confirmComponentAndBom(self):
        print("queren", self.strKey)
        #初始化get参数
        params={"key":self.strKey}
        response = requests.request("GET", self.constants.CONFIRMCOMPONENTANDBOM_URL, params=params,
                                    headers=self.headers)
        data = json.loads(response.text)
        print(data)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
