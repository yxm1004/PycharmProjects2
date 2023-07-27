import json
import seldom
from common.loginApi import Common
class testdictionarytemplate(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_get_dictionarytemplate(self):
        """
           物料主档-下载模版
        """
        self.payload = {}
        self.get("/api/report/dictionary/template/09", data=self.payload, headers=self.header)
        self.assertStatusCode(200)



if __name__ == '__main__':
    seldom.main(debug=True)