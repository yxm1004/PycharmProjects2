import json
import seldom
from common.loginApi import Common
class test03material(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_001_checkMaterialDelete(self):
        """
            判断物料是否能被删除
        """
        self.payload = json.dumps([
            "1684495755609374720"
        ])
        self.post("/api/report/material/checkMaterialDelete", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])
    def test_002_material(self):
        """
            删除物料
        """
        self.payload = json.dumps([
            "1684495755609374720"
        ])
        self.delete("/api/report/material", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)




