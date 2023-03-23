import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()
class projectupdateApi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/project/update"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def projectupdate(self):
        """
        编辑项目信息-确认投产/取消投产
        """


        payload = json.dumps({
            "echoMap": {
                "province": "北京市",
                "city": "北京市",
                "region": "丰台区"
            },
            "id": "461",
            "bomProjectId": "1638840413895172096",
            "contractNo": "",
            "contractBelong": "",
            "name": "交付0323",
            "projectType": 1,
            "abbreviation": "交付0323",
            "province": 1,
            "city": 2,
            "region": 6,
            "addressDetail": "",
            "note": "",
            "contactPerson": "",
            "contactPhone": "",
            "salePerson": "尹卡卡",
            "salePhone": "153 1348 7958",
            "clientName": "",
            "customers": [],
            "manufacturer": "大乐装 | 数字化交付平台",
            "projectAmounts": None,
            "allocationType": 1,
            "coordinationFactory": "",
            "orgId": "",
            "logo": None,
            "allocationList": [
                {
                    "coordinationFactory": "",
                    "orgId": "",
                    "details": [
                        {}
                    ]
                }
            ],
            "createMark": True,
            "orderType": "大乐装（东莞）建筑科技有限公司",
            "status": 1,
            "address": [
                1,
                2,
                6
            ],
            "amounts": []
        })
        response = requests.request("POST", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
    pc = projectupdateApi()
    response = pc.projectupdate()
    print(response.json())