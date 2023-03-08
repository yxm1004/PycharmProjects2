import json
import requests
from interfaceTest.common.ApiConstants import ApiConstants
from interfaceTest import readConfig

localReadConfig = readConfig.ReadConfig()


# 登录接口
class loginApi:
    def __init__(self):
        pass

    def login(self, account, password):
        # 引入常量类，直接使用常量类中的url地址
        constants = ApiConstants()
        headers = {
            'Authorization': 'Basic Y2xvdWRmYWN0b3J5X3dlYjpjbG91ZGZhY3Rvcnlfd2ViX3NlY3JldA==',
            'tenant': 'ZGdnYw==',
            'token': 'Bearer test',
            'Content-Type': 'application/json'
        }
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

        response = requests.request("POST", constants.LOGIN_URL, headers=headers, data=payload)
        # 返回结果
        return response

    # 获取登录用户token
    def getToken(self, account, password):
        response = self.login(account, password)
        if response.status_code == 200:
            print(response.json()["data"]["token"])
            token = response.json()["data"]["token"]
            return token
        else:
            print("failed to get token")


# 验证这个用例
if __name__ == '__main__':
    lg=loginApi()
    rs=lg.login("15313487958","900520")
    print("login",rs.json())
    tk=lg.getToken("15313487958","900520")
    print(tk)
