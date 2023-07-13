import json
import datetime
import time

import seldom
from common.loginApi import Common

class testgetMonitoring(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_getMonitoring(self):
        """
                实时质量监测
        """
        self.payload = json.dumps({
            "screen": 0,
            "endTime": "2023-05-31",
            "startTime": "2023-05-01"
        })
        self.post("/api/report/billboards/getMonitoring", data=self.payload, headers=self.header)
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(debug=True)