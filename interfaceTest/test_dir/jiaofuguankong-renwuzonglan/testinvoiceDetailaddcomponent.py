import json
import seldom
from common.loginApi import Common
class testinvoiceDetailaddcomponent(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_invoiceDetailaddcomponent(self):
        """
           执行者视角-滚动交付-发货单详情添加构件
        """
        self.payload = json.dumps({
            "componentIds": [
                "1696713183667945472",
                "1696713183743442945"
            ]
        })
        self.post("/api/report/invoiceDetail/add/component",data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)
