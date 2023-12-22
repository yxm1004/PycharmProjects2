import json
import seldom
from common.loginApi import Common
class testinvoicedetailpage(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_invoicedetailpage(self):
        """
           获取发货单-构件列表
        """
        self.payload = json.dumps({
            "current": 1,
            "extra": {},
            "model": {
                "id": 1631594528563527700,
                "projectId": 0,
                "tenantCode": ""
            },
            "order": "descending",
            "size": 999,
            "sort": "id"
        })
        self.post("/api/report/party/invoice/detail/page", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)
