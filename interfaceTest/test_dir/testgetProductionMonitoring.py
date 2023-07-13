import json
import datetime
import time

import seldom
from common.loginApi import Common

class testgetProductionMonitoring(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_getProductionMonitoring(self):
        """
                实时生产监测
        """
        self.payload = json.dumps({
            "screen": 0,
            "endTime": "2023-05-31",
            "startTime": "2023-05-01"
        })
        self.post("/api/report/productionTask/getProductionMonitoring", data=self.payload, headers=self.header)
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(debug=True)

