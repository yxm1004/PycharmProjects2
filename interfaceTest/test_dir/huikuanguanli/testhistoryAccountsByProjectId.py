import json
import seldom
from common.loginApi import Common
class testhistoryAccountsByProjectId(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_get_historyAccountsByProjectId(self):
        """
                回款管理-查询项目历史对账日志详情
        """
        self.payload = {}
        self.get("/api/report/historyAccounts/historyAccountsByProjectId?projectId=1443", data=self.payload,
                 headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)

