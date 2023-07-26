import json
import seldom
from common.loginApi import Common

class testgetAccountStatementByFirst(seldom.TestCase):
    def start(self):
        # 调用登录公共方法创建报文
        self.c = Common
        self.headef = self.c.SetHeader()
    def test_get_getAccountStatementByFirst(self):
        """
            对账单-获取销售发货单明细
        """
        self.payload = {}
        self.get("/api/report/accountStatement/getAccountStatementByFirst/356", data=self.payload,
                 headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)

