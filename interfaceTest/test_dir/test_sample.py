# test_sample.py
import unittest

import seldom


class YouTest(seldom.TestCase):

    def test_case(self):
        """a simple test case """
        print('1111111111')
        self.assertEqual(1+1, 2)


if __name__ == '__main__':
    # 指定运行其他目录&文件
    print('222222222222')
    # 运行当前文件中的用例
    seldom.main(language="zh-CN")  # 默认运行当前文件中所有用例
