import json
import seldom
from common.loginApi import Common
class testmoldGroupgetSpuList(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_moldGroupgetSpuList(self):
        """
           模具组关联的商品列表
        """
        self.payload = json.dumps({
            "moldGroupId": "1684740745325445120"
        })
        self.post("/api/report/moldGroup/getSpuList", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)
