import json
import datetime
import time

import seldom
from common.loginApi import Common
class testgetColumnData(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_getColumnData(self):
        """
                       对账单--获取协同工厂筛选数据
        """
        self.payload = json.dumps({
            "queryType": 2,
            "columnKey": "abbreviation"
        })
        self.post("/api/report/accountStatement/getColumnData", data=self.payload, headers=self.header)
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(debug=True)