import json
import seldom
from common.loginApi import Common
class testexportMaterial(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_get_exportMaterial(self):
        """
           导出所有物料
        """
        self.payload = {}
        self.get("/api/report/material/exportMaterial", data=self.payload, headers=self.header)
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(debug=True)
