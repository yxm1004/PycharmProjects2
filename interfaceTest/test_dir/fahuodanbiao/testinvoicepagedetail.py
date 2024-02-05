import json
import seldom
from common.loginApi import Common
class testinvoicepagedetail(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_invoicepagedetail(self):
        """
            发货单详情-分页查询构件列表
        """
        self.payload = json.dumps({
            "model": {
                "id": "1738135552480071680",
                "list": []
            },
            "extra": {},
            "current": 1,
            "size": 9999
        })
        self.post("/api/report/invoice/page/detail", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)
