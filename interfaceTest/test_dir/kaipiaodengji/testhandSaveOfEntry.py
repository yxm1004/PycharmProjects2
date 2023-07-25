import json
import datetime
import time

import seldom
from common.loginApi import Common

class testhandSaveOfEntry(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_handSaveOfEntry(self):
        """
               保存入账
        """
        self.payload = json.dumps({
            "totalReturnedMoney": "1700",
            "entryDate": "2023-07-24",
            "imageUrl": "https://cz-filemino.dalezhuang.com/report-test/efd3ed0e95004fc38967857bb6869887.png",
            "remark": "",
            "entryRecordDetailList": [
                {
                    "type": "1",
                    "accountPeriodDate": "2023-07-01",
                    "unInvoicingMoney": "1700.00",
                    "returnedMoney": "1700.00",
                    "company": "丰台建筑局",
                    "returnedMoneyType": "1",
                    "contractBelong": "大乐装01"
                }
            ],
            "projectId": "1063"
        })
        self.post("/api/report/invoicingRecord/handSaveOfEntry",data=self.payload,headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)