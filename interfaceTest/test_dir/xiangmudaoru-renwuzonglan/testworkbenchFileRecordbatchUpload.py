import json
import seldom
from common.loginApi import Common

class testworkbenchFileRecordbatchUpload(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_workbenchFileRecordbatchUpload(self):
        """
           任务附件记录表—批量上传
        """
        self.payload = json.dumps({
            "fileList": [
                {
                    "fileName": "微信图片_20230830102826.png",
                    "filePath": "https://cz-filemino.dalezhuang.com/report-test/b51482a6a8254235b0ee10930698125a.png",
                    "fileSize": 732259
                }
            ],
            "taskId": "1696770564032561152",
            "remark": "交底书备注123"
        })
        self.post("/api/report/workbenchFileRecord/batchUpload", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)
