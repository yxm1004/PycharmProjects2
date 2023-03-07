import unittest
import requests
import json

from interfaceTest.common.GetToken import Token
from interfaceTest import readConfig

localReadConfig = readConfig.ReadConfig()

class testcomponentsave(unittest.TestCase):
    def setUp(self):
        # 引入常量类，直接使用常量类中的url地址
        self.constants = ApiConstants()
        self.account = localReadConfig.get_OPTION("account")
        self.password = localReadConfig.get_OPTION("password")
        payload = json.dumps({
        "bomDetailList": [],
        "rebarWeight": "30.475",
        "projectId": "434",
        "building": "6",
        "floorSegment": "3",
        "type": "叠合板",
        "model": "DHB003",
        "floorCount": "1",
        "appearanceSizeLength": "2500",
        "appearanceSizeWidth": "2320",
        "appearanceSizeThickness": "60",
        "squareAmount": "0.636",
        "weight": "0.255",
        "concreteLabel": "C30",
        "concreteDosage": "0.636"
    })
    headers = {
        'Authorization': 'Basic Y2xvdWRmYWN0b3J5X3dlYjpjbG91ZGZhY3Rvcnlfd2ViX3NlY3JldA==',
        'tenant': 'ZGdnYw==',
        'token': self.token ,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST",self.constants.componentsave_url, headers=headers, data=payload)
    self.assertEqual(response.status_code, 200)
if __name__ == '__main__':
    main()

