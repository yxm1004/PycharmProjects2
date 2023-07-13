import json
import seldom

from common.loginApi import Common
from interfaceTest import readConfig

localReadConfig = readConfig.ReadConfig()


class testcomponentsave(seldom.TestCase):
    def start(self):
        #调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()

    #测试用例
    def test_post_componentsave(self):

        payload = json.dumps({
            "bomDetailList": [],
            "rebarWeight": "30.475",
            "projectId": "434",
            "building": "6",
            "floorSegment": "3",
            "type": "叠合板",
            "model": "DHB009",
            "floorCount": "1",
            "appearanceSizeLength": "2500",
            "appearanceSizeWidth": "2320",
            "appearanceSizeThickness": "60",
            "squareAmount": "0.636",
            "weight": "0.255",
            "concreteLabel": "C30",
            "concreteDosage": "0.636"
        })
        self.post("POST", "/api/report/component/saveComponentAndBom", headers=self.headers, data=payload)
        self.assertStatusCode(200)



# if __name__ == '__main__':
#     unittest.main()#单元测试