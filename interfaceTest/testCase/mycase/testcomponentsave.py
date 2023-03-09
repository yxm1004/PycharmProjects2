import unittest
import requests
import json

from interfaceTest.common.ApiConstants import ApiConstants
from interfaceTest.common.GetToken import Token
from interfaceTest import readConfig

localReadConfig = readConfig.ReadConfig()


class testcomponentsave(unittest.TestCase):
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
    #测试用例
    def test_post_componentsave(self):

        payload = json.dumps({
            "bomDetailList": [],
            "rebarWeight": "30.475",
            "projectId": "434",
            "building": "6",
            "floorSegment": "3",
            "type": "叠合板",
            "model": "DHB009",
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
        self.assertEqual(response.status_code, 200)
        # 取出响应结果字段
        print("------------------",response.text)
        data = json.loads(response.text)
        # 多级字段取值
        strKey = data["data"]["strKey"]
        print("打印结果",data)


# if __name__ == '__main__':
#     unittest.main()#单元测试