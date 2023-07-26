import json
import datetime
import time

import seldom
from common.loginApi import Common
class testgetProcessPlanPage(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_getProcessPlanPage(self):
        """
            新-分页查询工艺方案
        """
        self.payload = json.dumps({
            "model": {
                "list": [],
                "orderField": "production_rounds,scheme_number,scheme_sequence,scheme_car_number",
                "orderType": "ASC,ASC,ASC,ASC",
                "projectId": "1061",
                "building": "5"
            },
            "extra": {},
            "current": 1,
            "size": 50
        })
        self.post("/api/report/processPlan/getProcessPlanPage", data=self.payload,headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)
