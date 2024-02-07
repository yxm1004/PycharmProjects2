import json
import seldom
from common.loginApi import Common
class testgetProduceStatementInfo(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_get_getProduceStatementInfo(self):
        """
            获取劳务对账单详情
        """
        self.payload = {}
        self.get("/api/report/produceStatement/getProduceStatementInfo/1726807249439793152", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)