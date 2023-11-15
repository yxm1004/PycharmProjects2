import json
import seldom
from common.loginApi import Common

class testrankingRecordupdateRankingRecord(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_rankingRecordupdateRankingRecord(self):
        """
           修改回款目标金额
        """
        
