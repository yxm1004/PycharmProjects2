import json
import datetime
import time

import seldom
from common.loginApi import Common

class testcomponentlistByPage(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_componentlistByPage(self):
        """
                   构件表-分页查询构件列表
        """
        self.payload = json.dumps({
            "model": {
                "list": [],
                "projectId": "434",
                "isNoProductionTask": True
            },
            "extra": {},
            "current": 1,
            "size": 50,
            "order": "ascend",
            "sort": "floor"
        })
        self.post("/api/report/component/listByPage", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)

