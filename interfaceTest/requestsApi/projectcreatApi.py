import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()


class projectcreatApi:
    def __init__(self, abbreviation):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/project/create"
        lg = loginApi()
        self.token = lg.getToken()
        self.headers = {
            'Authorization': 'Basic Y2xvdWRmYWN0b3J5X3dlYjpjbG91ZGZhY3Rvcnlfd2ViX3NlY3JldA==',
            'tenant': 'ZGdnYw==',
            'token': "Bearer "+self.token,
            'Content-Type': 'application/json'
        }
        self.payload = json.dumps({
            "name": "",
            "orderType": "大乐装（东莞）建筑科技有限公司",
            "abbreviation": abbreviation,
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

    def projectcreat(self):
        response = requests.request("POST", self.url, headers=self.headers, data=self.payload)
        return response


if __name__ == '__main__':
    pc = projectcreatApi("2023030999")
    rs = pc.projectcreat()
    print(rs.json())
