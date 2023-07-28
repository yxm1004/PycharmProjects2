import json
import seldom
from common.loginApi import Common
class testupdateMoldGroup(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_updateMoldGroup(self):
        """
           修改模具组
        """
        self.payload = json.dumps({
            "groupNumber": "MJXH-001",
            "staticProject": "55555555",
            "componentType": "6",
            "fileDTOList": [],
            "managerPhone": "15879654575",
            "managerUserId": "1639110090675978240",
            "name": "ALC",
            "normalHours": 12,
            "proofs": [
                "https://cz-filemino.dalezhuang.com/report-test/c474a1532a5c4693804c2e58dcbe6fbd.webp"
            ],
            "cover": "https://cz-filemino.dalezhuang.com/report-test/c474a1532a5c4693804c2e58dcbe6fbd.webp",
            "id": "1658739780411719680"
        })
        self.post("/api/report/moldGroup/updateMoldGroup", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)