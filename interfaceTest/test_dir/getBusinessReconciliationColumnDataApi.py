import json
import datetime
import time

import seldom
from common.loginApi import Common
class testgetBusinessReconciliationColumnData(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_getBusinessReconciliationColumnData(self):
        """
                    web-商务对账-获取列表筛选数据
        """
        self.payload = json.dumps({
            "directors": [],
            "overdueStatus": True,
            "projectIdList": [],
            "projectStatusList": [],
            "salePersonList": []
        })
        self.post("/api/report/accountStatement/getBusinessReconciliationColumnData", data=self.payload,
                  headers=self.header)
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(debug=True)