import json
import datetime
import time

import seldom
from common.loginApi import Common
class testprocessPlan(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_put_processPlan(self):
        """
            工艺方案修改
        """
        self.payload = json.dumps({
            "id": "1684044611066003456",
            "productionRounds": "1",
            "schemeNumber": "1",
            "schemeSequence": "1",
            "schemeCarNumber": "1",
            "note": "备注123",
            "operation": "0"
        })
        self.put("/api/report/processPlan", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)