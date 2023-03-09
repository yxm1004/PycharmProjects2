import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()
class productionTaskApi:
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/productionTask"
        # 初始化头部
        lg = loginApi()
        #从登陆类里获取头部
        self.headers = lg.getheaders()
    def productionTask(self):
        """
        排产任务表-新增
        """
        payload = json.dumps({
            "echoMap": {},
            "weightTotal": "3.829",
            "squareAmountTotal": "7.488",
            "nums": 12,
            "plannedProductDate": "2023-03-09",
            "plannedCompleteDate": "2023-03-09",
            "coordinationFactory": "大乐装(东莞)",
            "assemblyLineId": "1570679828548419584",
            "leaderId": "1574240702374608896",
            "componentIds": [
                "1633116571146649601",
                "1633115949890535424",
                "1633106785785085953",
                "1633090870842490880",
                "1633090799224750081",
                "1633088938799267841",
                "1633085898402824193",
                "1633084949722562560",
                "1633083125066104833",
                "1633079637879816193",
                "1633075829296594945",
                "1633000259334438912"
            ]
        })
        response = requests.request("POST", self.url, headers=self.headers, data=payload)
        return response
    def delete_productionTaskbyid(self,id):
        """
        根据id删除排产任务表
        """
        # id=self.get_productionTask_id()
        payload = json.dumps([
            id
        ])
        response = requests.request("DELETE", self.url, headers=self.headers, data=payload)
        return response
    def get_productionTask_id(self):
        """
        获取新增方法中的结果id
        """
        response=self.productionTask()
        data=response.json()
        print(data)
        id=data["data"]["id"]
        return id

if __name__ == '__main__':
    pt=productionTaskApi()
    #调用获取id方法就会调用新增方法返回id
    id=pt.get_productionTask_id()
    #再调用删除方法根据id删除
    response=pt.delete_productionTaskbyid(id)
    print("打印删除相应结果",response.json())