import json
import datetime
import time

import seldom
from common.loginApi import Common

class testgetSettlementConfirmationColumnData(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_getSettlementConfirmationColumnData(self):
        """
                   web- 结算签确-获取列表筛选数据
        """
        self.payload = json.dumps({
            "directors": [],
            "overdueStatus": True,
            "projectIdList": [],
            "projectStatusList": [],
            "salePersonList": []
        })
        self.post("/api/report/accountStatement/getSettlementConfirmationColumnData", data=self.payload,headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])


if __name__ == '__main__':
    seldom.main(debug=True)

