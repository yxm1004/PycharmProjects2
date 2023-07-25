import json
import datetime
import time

import seldom
from common.loginApi import Common

class testgetBuildByProjectId(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_get_getBuildByProjectId(self):
        """
            根据项目id获取楼栋信息
        """
        self.payload = {}
        self.get("/api/report/component/getBuildByProjectId?projectId=1061", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)
