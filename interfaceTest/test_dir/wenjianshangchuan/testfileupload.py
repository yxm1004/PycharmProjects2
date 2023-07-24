import json
import datetime
import time
import requests
import seldom
from common.loginApi import Common


class testfileupload(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        # self.header = self.c.SetHeader()
        #在传递文件时，不能将Content-Type头部设置为application/json，因为application/json用于表示请求体是一个JSON格式的数据，而不是文件数据
        self.header = self.c.SetFileHeader()
        # self.url = "https://jf-api-test-x1ksp5.dalezhuang.com/api/report/file/upload"

    def test_post_fileupload(self):
        """
                   文件上传
        """
        self.payload = {}
        files = [
            ('file', ('1111.webp',
                      open('E:\\PycharmProjects2\\interfaceTest\\test_dir\\test_data\\1111.webp', 'rb'), 'image/webp'))
        ]

        print(self.header)
        self.post("/api/report/file/upload", headers=self.header,  files=files)
        self.assertStatusCode(200)
