import json
import datetime
import time

import seldom
from common.loginApi import Common
class testfileupload(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_fileupload(self):
        """
                   文件上传
        """
        self.payload={}
        file_path="C:/Users/msi/Pictures/ef6c7a0e2c6b4ebb9b60c38fb32dfa25.webp"
        with open(file_path,"rb") as file:
            files ={"file" :file}
            self.post("/api/report/file/upload", files=files,
                  headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])

if __name__ == '__main__':
    seldom.main(debug=True)