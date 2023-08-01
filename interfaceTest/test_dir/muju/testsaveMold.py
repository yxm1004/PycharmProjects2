import json
import datetime
import time

import seldom
from common.loginApi import Common
class testsaveMold(seldom.TestCase):
    def start(self):
        #调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_saveMold(self):
        """
             新增模具
        """
        # 用时间戳作为模具编号
        moldNumber = datetime.datetime.now()
        moldNumber = str(int(time.mktime(moldNumber.timetuple())))
        # print(moldNumber)
        self.payload = json.dumps({
            "moldGroupIds": [
                "1684804358186729472"
            ],
            "currentLife": 0,
            "proofs": [
                "https://cz-filemino.dalezhuang.com/report-test/652d2d592c664b40b94e008fef851127.webp"
            ],
            "fileDTOList": [],
            "dummy": 0,
            "moldNumber": moldNumber,
            "defUsefulLife": "200",
            "orgId": "1514430640907354112",
            "cover": "https://cz-filemino.dalezhuang.com/report-test/652d2d592c664b40b94e008fef851127.webp"
        })
        self.post("/api/report/mold/saveMold", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)
