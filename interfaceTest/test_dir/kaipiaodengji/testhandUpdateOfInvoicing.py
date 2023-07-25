import json
import datetime
import time

import seldom
from common.loginApi import Common
class testhandUpdateOfInvoicing(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_put_handUpdateOfInvoicing(self):
        """
                修改开票
        """
        self.payload = json.dumps({
            "id": "1682230365915185152",
            "invoicedAmount": "1500.00",
            "invoicedDate": "2023-07-21 00:00:00",
            "code": "101",
            "billVoucherUrl": "https://cz-filemino.dalezhuang.com/report-test/928800165c9e4c2c835c024c0af799fd.jpg",
            "remark": "修改备注2",
            "invoicingRecordDetailList": [
                {
                    "echoMap": {},
                    "id": "1682230365931962368",
                    "invoicingRecordId": "1682230365915185152",
                    "type": "1",
                    "invoicedAmount": "1500.00",
                    "accountPeriodDate": "2023-07-01"
                }
            ],
            "projectId": "1063"
        })
        self.put("/api/report/invoicingRecord/handUpdateOfInvoicing", data=self.payload,
                 headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])

if __name__ == '__main__':
    seldom.main(debug=True)