import json
import seldom
from common.loginApi import Common
class testchangeParentgetDrawList(seldom.TestCase):
    def start(self):
        #调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_changeParentgetDrawList(self):
        """
            设计变更-根据项目id获取有关联图纸的编号(去重)
        """
        self.payload = json.dumps([
            {
                "building": "2",
                "model": "6~8F-DB5",
                "projectId": "1063"
            }
        ])
        self.post("/api/report/changeParent/getDrawList", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)
