import json
import seldom
from common.loginApi import Common
class testexportmaterialDetail(seldom.TestCase):
    def start(self):
        #调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_exportmaterialDetail(self):
        """
            物料明细导出
        """
        self.payload = json.dumps({
            "materialCode": "PR20230705090322"
        })
        self.post("/api/report/tmpBomDetail/export/materialDetail", data=self.payload, headers=self.header)
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(debug=True)
