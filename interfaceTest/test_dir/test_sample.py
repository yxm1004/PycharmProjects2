# test_sample.py
import unittest

import seldom


class YouTest(seldom.TestCase):

    def test_case(self):
        """a simple test case """
        self.assertEqual(1+1, 2)


