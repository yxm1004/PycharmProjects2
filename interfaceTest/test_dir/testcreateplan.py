import json
import datetime
import time

import seldom
from common.loginApi import Common

class testcreatplan(seldom.TestCase):
    def start(self):
        #调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_createplan(self):
        """
                       创建主计划
        """
        self.payload = json.dumps({
            "considerMaintenanceTime": "3",
            "excludeHolidays": [
                "1"
            ],
            "expectedProductCycle": "2",
            "planTime": "3",
            "roundStatus": False
        })
        self.post("/api/report/masterPlan/createPlan", data=self.payload, headers=self.header)
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(debug=True)




