import json
import datetime
import time

import seldom
from common.loginApi import Common

class testcomponentstatus(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_componentstatus(self):
        """
           批量更改构件状态
        """
        self.payload = json.dumps({
            "componentIds": [
                "1681223883232903168",
                "1681223554919563264",
                "1679674165143011330",
                "1679674165063319554",
                "1679674165105262592",
                "1679674165021376514",
                "1681188139621679105"
            ],
            "inspectionStatus": 0,
            "status": 4
        })
        self.post("/api/report/component/status", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)
