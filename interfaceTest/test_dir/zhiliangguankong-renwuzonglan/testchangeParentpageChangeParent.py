import json
import seldom
from common.loginApi import Common
class testchangeParentpageChangeParent(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_changeParentpageChangeParent(self):
        """
           管理者视角-质量管控-设计变更，查看处理中变更
        """
        self.payload = json.dumps({
            "model": {
                "list": [
                    {
                        "columnFileValue": "0,3",
                        "columnFileKey": "status",
                        "calSymbol": 4,
                        "dataType": 3
                    }
                ],
                "status": "0,3",
                "locations": []
            },
            "extra": {},
            "current": 1,
            "size": 50
        })
        self.post("/api/report/changeParent/pageChangeParent", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)
