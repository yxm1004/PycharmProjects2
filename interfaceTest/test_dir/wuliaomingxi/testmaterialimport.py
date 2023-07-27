import json
import seldom
from common.loginApi import Common
class testmaterialimport(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        # self.header = self.c.SetHeader()
        #在传递文件时，不能将Content-Type头部设置为application/json，因为application/json用于表示请求体是一个JSON格式的数据，而不是文件数据
        self.header = self.c.SetFileHeader()
        # self.url = "https://jf-api-test-x1ksp5.dalezhuang.com/api/report/file/upload"
    def test_001_materialimport(self):
        """
           导入物料主档
        """
        files = [
            ('file', ('物料下载模板.xlsx', open('C:\\Users\\msi\\Desktop\\测试数据\\物料下载模板.xlsx', 'rb'),
                      'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'))
        ]
        print(self.header)
        self.post("/api/report/material/import", headers=self.header, files=files)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])
    def test_002_materialconfirmImport(self):
        """
           确定导入物料主档
        """
        self.payload = {}
        self.get("/api/report/material/confirmImport", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)




