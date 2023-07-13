import json
import requests
from common.ApiConstants import ApiConstants
from interfaceTest import readConfig

localReadConfig = readConfig.ReadConfig()


# 登录接口
class loginApi:
    """
    读取配置项config.ini内OPTION账号信息登录
    getToken()返回该用户的token信息
    getheaders()返回头部信息供其他方法使用
    """
    def __init__(self):
        self.account = localReadConfig.get_OPTION("account")
        self.password = localReadConfig.get_OPTION("password")

    def login(self):
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

    def getheaders(self):
        """
        登录后获取token返回一个headers
        """
        tk = self.getToken()
        headers = {
            'Authorization': 'Basic Y2xvdWRmYWN0b3J5X3dlYjpjbG91ZGZhY3Rvcnlfd2ViX3NlY3JldA==',
            'tenant': 'ZGdnYw==',
            'token': "Bearer " + tk,
            'Content-Type': 'application/json'
        }
        return headers
# 验证这个用例
if __name__ == '__main__':
    lg=loginApi()
    rs=lg.login()
    print("login",rs.json())
    tk=lg.getToken()
    print(tk)
