import unittest
import requests
import json

from interfaceTest.common.GetToken import Token
from interfaceTest import readConfig

localReadConfig = readConfig.ReadConfig()

class testprojectcreat(unittest.TestCase ):
    @classmethod
    def setUpClass(self) :
        #获取token
        tk=Token()
        self.token='Bearer '+tk.get_token()
        print("self.token-------",self.token)


    def test_post_projectcreat(self):
        # 获取baseurl
        baseurl = localReadConfig.get_http("baseurl")
        url = baseurl + "/api/report/project/create"

        payload = json.dumps({
            "name": "",
            "orderType": "大乐装（东莞）建筑科技有限公司",
            "abbreviation": "2023030914",
            "contractNo": "",
            "province": 1,
            "city": 2,
            "region": 6,
            "address": [
                1,
                2,
                6
            ],
            "addressDetail": "",
            "note": "",
            "manufacturer": "大乐装 | 数字化交付平台",
            "contactPerson": "",
            "contactPhone": "",
            "salePerson": "尹卡卡",
            "salePhone": "153 1348 7958",
            "clientName": "",
            "contractBelong": "",
            "customers": [],
            "projectType": 1,
            "allocationType": None,
            "coordinationFactory": None,
            "allocationList": [],
            "logo": None
        })
        headers = {
            'Authorization': 'Basic Y2xvdWRmYWN0b3J5X3dlYjpjbG91ZGZhY3Rvcnlfd2ViX3NlY3JldA==',
            'tenant': 'ZGdnYw==',
            'token': self.token,
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
if __name__ == '__main__':
     unittest .main()
