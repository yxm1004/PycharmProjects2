import json
import seldom
from common.loginApi import Common

class testgetAccountStatementComponent(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_get_getAccountStatementComponent(self):
        """
            对账单-获取销售发货单明细
        """
        self.payload = {}
        self.get("/api/report/accountStatement/getAccountStatementComponent?id=1675715347614793728", data=self.payload, headerstest=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"   # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)

