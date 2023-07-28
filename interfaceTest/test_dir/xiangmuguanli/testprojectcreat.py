import json
import datetime
import time

import seldom
from common.loginApi import Common


class testprojectcreat(seldom.TestCase):
    def start(self):
        #调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_projectcreat(self):
        """
             创建项目
        """
        #用时间戳作为项目简称
        abbreviation = datetime.datetime.now()
        abbreviation = str(int(time.mktime(abbreviation.timetuple())))
        # print(abbreviation)

        #构建报文
        self.payload = json.dumps({
            "name": "验证",
            "orderType": "大乐装（惠州）建筑科技有限公司",
            "abbreviation": abbreviation,
            "contractNo": "ww-202307122",
            "province": 576,
            "city": 599,
            "region": 600,
            "address": [
                576,
                599,
                600
            ],
            "addressDetail": "铁西建筑局01",
            "note": "",
            "manufacturer": "大乐装 | 数字化交付平台",
            "contactPerson": "尹123",
            "contactPhone": "158 7965 4576",
            "salePerson": "尹晓梅",
            "salePhone": "153 1348 7958",
            "clientName": "铁西建筑局",
            "contractBelong": "大乐装01",
            "customers": [],
            "projectType": 1,
            "allocationType": None,
            "coordinationFactory": None,
            "allocationList": [],
            "logo": None,
            "orderSource": 2
        })
        self.post("/api/report/project/create", data=self.payload, headers=self.header)
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(debug=True)
