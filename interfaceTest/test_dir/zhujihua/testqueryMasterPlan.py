import json
import datetime
import time

import seldom
from common.loginApi import Common
class testqueryMasterPlan(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_queryMasterPlanApi(self):
        """
                   查询主计划
        """
        self.payload = json.dumps({
            "createTime": "2023-06",
            "orgIds": [],
            "projectIds": [],
            "version": 0
        })
        self.post("/api/report/masterPlan/queryMasterPlan", data=self.payload, headers=self.header)
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(debug=True)
