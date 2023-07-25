import json
import datetime
import time

import seldom
from common.loginApi import Common
class testhandSaveOfInvoicing(seldom.TestCase):
    def start(self):
        #调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_handSaveOfInvoicing(self):
        """
                        新增开票
        """
        # 用时间戳作为发票号
        code = datetime.datetime.now()
        code = str(int(time.mktime(code.timetuple())))
        # print(code)
        self.payload = json.dumps({
            "invoicedAmount": "690",
            "invoicedDate": "2023-07-24",
            "code": code,
            "billVoucherUrl": "https://cz-filemino.dalezhuang.com/report-test/a241cae015f740398d218b8d6176a390.png",
            "remark": "123",
            "invoicingRecordDetailList": [
                {
                    "type": "1",
                    "accountPeriodDate": "2023-07-01",
                    "invoicedAmount": "690"
                }
            ],
            "projectId": "1063"
        })
        self.post("/api/report/invoicingRecord/handSaveOfInvoicing", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)

