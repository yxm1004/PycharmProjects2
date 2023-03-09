import json
import requests
from interfaceTest.common.ApiConstants import ApiConstants
from interfaceTest import readConfig

localReadConfig = readConfig.ReadConfig()


# 登录接口
class loginApi:
    def __init__(self):
        self.account = localReadConfig.get_OPTION("account")
        self.password = localReadConfig.get_OPTION("password")

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
            "account": self.account,
            "avatar": "",
            "code": "",
            "grantType": "password",
            "key": "",
            "name": "",
            "openId": "",
            "password": self.password,
            "refreshToken": ""
        })

        response = requests.request("POST", constants.LOGIN_URL, headers=headers, data=payload)
        # 返回结果
        return response

    # 获取登录用户token
    def getToken(self):
        response = self.login()
        if response.status_code == 200:
            print(response.json()["data"]["token"])
            token = response.json()["data"]["token"]
            return token
        else:
            print("failed to get token")


# 验证这个用例
if __name__ == '__main__':
    lg=loginApi()
    rs=lg.login()
    print("login",rs.json())
    tk=lg.getToken()
    print(tk)
