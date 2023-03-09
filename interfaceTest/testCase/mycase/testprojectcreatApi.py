import time
import unittest
from interfaceTest.requestsApi.projectcreatApi import projectcreatApi
from interfaceTest import readConfig


class testprojectcreat(unittest.TestCase ):
    def setUp(self) :
        #初始化创建项目对象
        self.pc= projectcreatApi()
    #编写创建项目用例
    def test_post_projectcreat(self):
        #创建对象方法创建项目简称,使用时间戳作为项目简称创建项目
        abbreviation=time.strftime("%Y%m%d%H%M%S", time.localtime())
        rs=self.pc.projectcreat(abbreviation)
        self.assertEqual(rs.status_code, 200)
        print("创建项目响应结果：",rs.json())


if __name__ == '__main__':

    unittest .main()
