import json
import datetime
import time

import seldom
from common.loginApi import Common
class testaccountStatementgetMonitoring(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_accountStatementgetMonitoring(self):
        """
                对账回款监测
        """
        self.payload = json.dumps({
            "screen": 0,
            "endTime": "2023-06-31",
            "startTime": "2023-06-01"
        })
        self.post("/api/report/accountStatement/getMonitoring", data=self.payload, headers=self.header)
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(debug=True)

