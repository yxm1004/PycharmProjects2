import json
import seldom
from common.loginApi import Common
class testworkbenchFileRecordquery02(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_workbenchFileRecordquery02(self):
        """
           上传甲方验收文件-附件查询
        """
        self.payload = json.dumps({
            "taskId": "1699605880934236160",
            "businessType": 8,
            "businessNode": 3
        })
        self.post("/api/report/workbenchFileRecord/query", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)
