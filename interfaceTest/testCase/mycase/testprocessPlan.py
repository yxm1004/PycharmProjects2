import unittest
import requests
import json

from interfaceTest.common.ApiConstants import ApiConstants
from interfaceTest.common.GetToken import Token
from interfaceTest import readConfig
from interfaceTest.testCase.mycase.testcomponentsave import testcomponentsave

localReadConfig = readConfig.ReadConfig()


class processPlan(unittest.TestCase):
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

        def test_put_processPlan(slef):
            payload = json.dumps({
                "echoMap": {
                    "projectId": "434"
                },
                "id": "1633075829296594944",
                "createTime": "2023-03-07 15:02:58",
                "createdBy": "1623846762252861440",
                "updateTime": "2023-03-07 15:02:58",
                "updatedBy": "1623846762252861440",
                "projectId": "434",
                "building": "6",
                "floor": "3",
                "type": "叠合板",
                "model": "DHB-005",
                "floorCount": 1,
                "appearanceSizeLength": 3170,
                "appearanceSizeWidth": 3520,
                "appearanceSizeThickness": 60,
                "squareAmount": 734,
                "weight": 293,
                "moldNumber": None,
                "programmeArea": None,
                "productionRounds": "3",
                "schemeNumber": "3",
                "schemeSequence": "3",
                "schemeCarNumber": "3",
                "schemeModel": 10,
                "note": "测试",
                "concreteDosage": "0.293",
                "concreteLabel": "C30",
                "deleteStatus": 0
            })

        response = requests.request("PUT", self.constants.PROCESSPLAN_URL, headers=self.headers, data=payload)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
