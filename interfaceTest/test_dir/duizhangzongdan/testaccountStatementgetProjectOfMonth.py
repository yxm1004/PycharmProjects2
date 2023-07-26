import json
import datetime
import time

import seldom
from common.loginApi import Common
class testaccountStatementgetProjectOfMonth(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_get_accountStatementgetProjectOfMonth(self):
        """
            回款管理-项目筛选
        """
        self.payload = {}
        self.get("/api/report/accountStatement/getProjectOfMonth?startTime=2023-04&endTime=2023-07", data=self.payload,
                 headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)


