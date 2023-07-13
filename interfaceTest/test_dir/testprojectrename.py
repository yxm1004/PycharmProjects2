import json
import seldom
from common.loginApi import Common

class testprojectrename(seldom.TestCase ):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()

    def test_post_projectcreat(self):
        """
                       更换图纸名称
        """
        self.payload = json.dumps({
            "fileId": 1679317923848044544,
            "name": "惠州千湾汇13",
            "phone": "",
            "reportUserId": 0
        })
        headers = {
            'Authorization': 'Basic Y2xvdWRmYWN0b3J5X3dlYjpjbG91ZGZhY3Rvcnlfd2ViX3NlY3JldA==',
            'tenant': 'ZGdnYw==',
            'token': self.token,
            'Content-Type': 'application/json'
        }

        self.post("/api/report/bom/projectFile/rename", data=self.payload, headers=self.header)
        self.assertStatusCode(200)


if __name__ == '__main__':
     seldom.main(debug=True)
