import json
import seldom
from common.loginApi import Common
class testqueryPaymentCollectionTaskDetail(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_get_queryPaymentCollectionTaskDetail(self):
        """
                回款管理-根据项目查询最新回款跟进任务
        """
        self.payload = {}
        self.get("/api/report/workbenchTaskRecord/queryPaymentCollectionTaskDetail/1443", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)