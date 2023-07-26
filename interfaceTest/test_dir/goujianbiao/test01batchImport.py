import json
import datetime
import time

import seldom
from common.loginApi import Common
class testbatchImport(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        # self.header = self.c.SetHeader()
        #在传递文件时，不能将Content-Type头部设置为application/json，因为application/json用于表示请求体是一个JSON格式的数据，而不是文件数据
        self.header = self.c.SetFileHeader()
        # self.url = "https://jf-api-test-x1ksp5.dalezhuang.com/api/report/file/upload"
    def test_post_batchImport(self):
        """
                   批量导入构件
        """
        files = [
            ('file', ('导入构件清单模块 (6).xlsx',
                      open('C:\\Users\\msi\\Desktop\\测试数据\\导入构件清单模块 (6).xlsx', 'rb'), 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'))
        ]
        print(self.header)
        self.post("/api/report/component/batchImport", headers=self.header, files=files)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)
