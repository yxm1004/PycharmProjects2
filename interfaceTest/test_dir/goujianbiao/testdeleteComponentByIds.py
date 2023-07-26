import json
import datetime
import time

import seldom
from common.loginApi import Common
class testdeleteComponentByIds(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_001_deleteComponentByIds(self):
        """
            删除构件
        """
        self.payload = json.dumps({
            "componentParentIds": [],
            "componentIds": [
                "1680818087357579264"
            ]
        })
        self.post("/api/report/component/deleteComponentByIds", data=self.payload,headers=self.header)
        self.assertStatusCode(200)
        self.assertJSON(True, self.response["isSuccess"])

    def test_002_confirmDeleteComponent(self):
        """
            确认删除构件
        """
        self.payload = json.dumps({
            "componentParentIds": [],
            "componentIds": [
                "1680818087357579264"
            ]
        })
        self.post("/api/report/component/confirmDeleteComponent", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)