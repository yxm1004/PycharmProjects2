import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()

class componentlistByPageApi():
    baseurl = localReadConfig.get_http("baseurl")
    self.url = baseurl + "/api/report/accountStatement/queryCollectionExecutePageOfWeb"
    # 初始化头部
    lg = loginApi()
    # 从登陆类里获取头部
    self.headers = lg.getheaders()
