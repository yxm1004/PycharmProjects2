import json
import datetime
import time

import seldom
from common.loginApi import Common

class testqueryAllStatistics(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_queryAllStatistics(self):
        """
                    结算回款-总统计
        """
        self.payload = json.dumps({
            "directors": [],
            "overdueStatus": True,
            "projectIdList": [],
            "projectStatusList": [],
            "salePersonList": []
        })
        self.post("/api/report/accountStatement/queryAllStatistics", data=self.payload,headers=self.header)
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(debug=True)