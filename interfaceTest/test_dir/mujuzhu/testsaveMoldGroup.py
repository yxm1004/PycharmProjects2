import json
import datetime
import time

import seldom
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
        # print(name)

        self.payload = json.dumps({
            "componentType": "2",
            "name": name,
            "normalHours": "12",
            "person": "",
            "phone": "",
            "note": "",
            "personPhone": "1639110090675978240-15879654575",
            "groupNumber": "MUXH-0002",
            "staticProject": "静态项目01",
            "fileDTOList": [],
            "managerPhone": "15879654575",
            "managerUserId": "1639110090675978240",
            "proofs": []
        })
