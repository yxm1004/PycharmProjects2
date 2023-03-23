import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()
class processPlanApi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/processPlan"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def processplan(self):
        payload = json.dumps({
            "echoMap": {
                "projectId": "461"
            },
            "id": "1638869841743970304",
            "createTime": "2023-03-23 15:02:58",
            "createdBy": "1623846762252861440",
            "updateTime": "2023-03-23 15:02:58",
            "updatedBy": "1623846762252861440",
            "projectId": "461",
            "building": "6",
            "floor": "3",
            "type": "叠合板",
            "model": "DHB089",
            "floorCount": 3,
            "appearanceSizeLength": 2500,
            "appearanceSizeWidth": 2320,
            "appearanceSizeThickness": 60,
            "squareAmount": 636,
            "weight": 395,
            "moldNumber": None,
            "programmeArea": None,
            "productionRounds": "1",
            "schemeNumber": "1",
            "schemeSequence": "1",
            "schemeCarNumber": "1",
            "schemeModel": 10,
            "note": "测试",
            "concreteDosage": "0.636",
            "concreteLabel": "C30",
            "deleteStatus": 0
        })
        response = requests.request("put", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
    pc = processPlanApi()
    response = pc.processplan()
    print(response.json())