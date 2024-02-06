import json
import seldom
from common.loginApi import Common

class testgetCollectionDetailsMonths(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_getCollectionDetailsMonths(self):
        """
            回款明细-开票登记，查询开票账期月份
        """
        self.payload = json.dumps({
            "dataWay": 1,
            "projectId": "1310"
        })
        self.post("/api/report/invoicingRecord/getCollectionDetailsMonths", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)