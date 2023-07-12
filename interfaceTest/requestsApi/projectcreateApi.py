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
            "name": "验证",
            "orderType": "大乐装（惠州）建筑科技有限公司",
            "abbreviation": abbreviation,
            "contractNo": "ww-202307122",
            "province": 576,
            "city": 599,
            "region": 600,
            "address": [
                576,
                599,
                600
            ],
            "addressDetail": "铁西建筑局01",
            "note": "",
            "manufacturer": "大乐装 | 数字化交付平台",
            "contactPerson": "尹123",
            "contactPhone": "158 7965 4576",
            "salePerson": "尹晓梅",
            "salePhone": "153 1348 7958",
            "clientName": "铁西建筑局",
            "contractBelong": "大乐装01",
            "customers": [],
            "projectType": 1,
            "allocationType": None,
            "coordinationFactory": None,
            "allocationList": [],
            "logo": None,
            "orderSource": 2
        })
        response = requests.request("POST", self.url, headers=self.headers, data=self.payload)
        return response


if __name__ == '__main__':
    pc = projectcreatApi()
    rs = pc.projectcreat("你好07121050号")
    print(rs.json())
