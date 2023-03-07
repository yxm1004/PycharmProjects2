import json
import unittest

import requests
from interfaceTest import readConfig

localReadConfig = readConfig.ReadConfig()

class Token():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/oauth/noToken/login"
        self.token=None

    #2、获取token
    def get_token(self):

        account=localReadConfig.get_OPTION("account")
        password=localReadConfig.get_OPTION("password")
        print(account+password)
        payload = json.dumps({
            "account": account,
            "avatar": "",
            "code": "",
            "grantType": "password",
            "key": "",
            "name": "",
            "openId": "",
            "password": password,
            "refreshToken": ""
        })
        print(payload)
        headers = {
            'Authorization': 'Basic Y2xvdWRmYWN0b3J5X3dlYjpjbG91ZGZhY3Rvcnlfd2ViX3NlY3JldA==',
            'tenant': 'ZGdnYw==',
            'token': 'Bearer test',
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", self.url, headers=headers, data=payload)
        if response.status_code==200:
            print(response.json()["data"]["token"])
            self.token= response.json()["data"]["token"]
            return self.token
        else:
            raise Exception("failed to get token")
        #4.写一个断言
        # self.assertEqual(response.status_code, 200)
#5.验证这个用例
if __name__ == '__main__':
    token=Token()
    access_token=token.get_token()
    print("ccccccccccccccc",access_token)
