import json

from seldom.request import check_response
from seldom.request import HttpRequest


class Common(HttpRequest):
    """
    封住登陆公共方法组装header
    """

    @check_response(
        describe="获取登录用户名",
        status_code=200,
        ret="data.token",
        check={"msg": "成功"},
        debug=True
    )
    def get_login_user(self):
        """
        调用接口获得用户名
        """
        headers = {
            'Authorization': 'Basic Y2xvdWRmYWN0b3J5X3dlYjpjbG91ZGZhY3Rvcnlfd2ViX3NlY3JldA==',
            'tenant': 'ZGdnYw==',
            'token': 'Bearer test',
            'Content-Type': 'application/json'
        }
        payload = json.dumps({
            "account": "13170978240",
            "avatar": "",
            "code": "",
            "grantType": "password",
            "key": "",
            "name": "",
            "openId": "",
            "password": "yxm900520",
            "refreshToken": ""
        })
        r = self.post("https://jf-api-test-x1ksp5.dalezhuang.com/api/oauth/noToken/login", headers=headers,data=payload)
        return r

    def SetHeader (self):
        token=self.get_login_user()
        headers = {
            'Authorization': 'Basic Y2xvdWRmYWN0b3J5X3dlYjpjbG91ZGZhY3Rvcnlfd2ViX3NlY3JldA==',
            'tenant': 'ZGdnYw==',
            'token': "Bearer " + token,
            'Content-Type': 'application/json'
        }
        return headers

if __name__ == '__main__':
    c = Common()
    print(c.SetHeader())
