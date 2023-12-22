import json
import seldom
from common.loginApi import Common
class testdeliveryPlan(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_delete_deliveryPlan(self):
        """
          发货计划-删除
        """
        self.payload = json.dumps([
            "1738042933649428480"
        ])
        self.delete("/api/report/deliveryPlan", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "发货计划不存在"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])


if __name__ == '__main__':
    seldom.main(debug=True)