import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()


class projectcreatApi:
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/project/create"
        lg = loginApi()
        self.token = lg.getToken()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def projectcreat(self,abbreviation):
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
        response = requests.request("POST", self.url, headers=self.headers, data=self.payload)
        return response


if __name__ == '__main__':
    pc = projectcreatApi()
    rs = pc.projectcreat("项目0406")
    print(rs.json())
