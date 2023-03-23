import requests
import json
from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()


class confirmComponentAndBomApi:
    """新增构建清单componentsave()
    确认新增构建清单confirmComponentAndBom()"""

    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.componentsave_url = baseurl + "/api/report/component/saveComponentAndBom"
        self.confirmComponentAndBom_url = baseurl + "/api/report/component/confirmComponentAndBom"
        # 初始化头部
        lg = loginApi()
        self.headers = lg.getheaders()

    def confirmComponentAndBom(self):
        """
        确认新增-构件清单
        """
        params = {"key": self.getstrKey()}
        response = requests.request("GET", self.confirmComponentAndBom_url, params=params,
                                    headers=self.headers)
        print("确认新增-构建清单", response.json())
        return response

    def getstrKey(self):
        """
        获取新增构建接口中返回的key
        """
        response = self.componentsave()
        data = json.loads(response.text)
        # 提取key
        strKey = data["data"]["strKey"]
        return strKey

    def componentsave(self):
        """
        新增-构建清单
        """
        payload = json.dumps({
            "bomDetailList": [],
            "rebarWeight": "30.475",
            "projectId": "450",
            "building": "6",
            "floorSegment": "3",
            "type": "叠合板",
            "model": "DHB088",
            "floorCount": "1",
            "appearanceSizeLength": "2500",
            "appearanceSizeWidth": "2320",
            "appearanceSizeThickness": "60",
            "squareAmount": "0.636",
            "weight": "0.255",
            "concreteLabel": "C30",
            "concreteDosage": "0.636"
        })
        response = requests.request("POST", self.componentsave_url, headers=self.headers, data=payload)
        print("新增-构建清单", response.json())
        return response


if __name__ == '__main__':
    sv = confirmComponentAndBomApi()
    print(sv.confirmComponentAndBom())
