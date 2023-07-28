import json
import seldom
from common.loginApi import Common
class testdeleteMold(seldom.TestCase):
    def start(self):
        #调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_delete_deleteMold(self):
        """
            删除模具
        """
        self.payload = {}
        self.delete("/api/report/mold/deleteMold?id=1684828939270225920", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "模具不存在或已被删除"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(False, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)
