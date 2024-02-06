import json
import seldom
from common.loginApi import Common
class testqueryInvoicingEntryDetail(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_get_queryInvoicingEntryDetail(self):
        """
            回款明细-开票登记，获取开票入账详情
        """
        self.payload = {}
        self.get("/api/report/invoicingRecord/queryInvoicingEntryDetail?id=1743149283184295936", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)
