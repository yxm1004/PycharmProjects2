import json
import datetime
import time

import seldom
from seldom import data
from seldom.testdata import *

from common.loginApi import Common
class testsaveMoldGroup(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_saveMoldGroup(self):
        """
           新增模具组
        """
        # 用时间戳作为模具组名称
        name = datetime.datetime.now()
        name = str(int(time.mktime(name.timetuple())))

        # 导入from seldom.testdata import * 生成单词
        groupNumber = get_word()

        self.payload = json.dumps({
            "componentType": "2",
            "name": name,
            "normalHours": "12",
            "person": "",
            "phone": "",
            "note": "",
            "personPhone": "1639110090675978240-15879654575",
            "groupNumber": groupNumber,
            "staticProject": "静态项目01",
            "fileDTOList": [],
            "managerPhone": "15879654575",
            "managerUserId": "1639110090675978240",
            "proofs": []
        })
        self.post("/api/report/moldGroup/saveMoldGroup", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)
