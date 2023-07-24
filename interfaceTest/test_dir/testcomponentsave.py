import json

import requests
import seldom
from seldom import depend

from common.loginApi import Common


class testcomponentsave(seldom.TestCase):
    global strKey

    @classmethod
    def start_class(self):
        # 调用登录公共方法构建报文头
        print("执行次数")
        self.c = Common()
        self.header = self.c.SetHeader()

    def test_002_confirmComponentAndBom(self):
        """确认提交"""
        print("---------------" + self.response['data']['strKey'])
        params = {"key": self.response['data']['strKey']}
        r=self.get("/api/report/component/confirmComponentAndBom", params=params, headers=self.header)
        print(r.url)
        self.assertStatusCode(200)

    # 测试用例
    def test_001_componentsave(self):
        """添加构件"""
        self.payload = json.dumps({
            "bomDetailList": [],
            "rebarWeight": "20.475",
            "projectId": "1039",
            "building": "6",
            "floorSegment": "3",
            "id": 1679690953943678976,
            "type": "叠合板",
            "model": "DHB001",
            "floorCount": "1",
            "appearanceSizeLength": "2500",
            "appearanceSizeWidth": "2320",
            "appearanceSizeThickness": "60",
            "squareAmount": "0.636",
            "weight": "0.255",
            "concreteLabel": "C30",
            "concreteDosage": "0.636"
        })
        self.post("/api/report/component/saveComponentAndBom", data=self.payload, headers=self.header)
        self.assertStatusCode(200)



# if __name__ == '__main__':
#     unittest.main()#单元测试
