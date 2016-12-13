#!/bin/bash
from po.baidu_po import BaiduPO
import unittest


class ClickNomi(unittest.TestCase):
    baidu = BaiduPO()

    def setUp(self):
        pass

    def test_click_nuomi(self):
        self.baidu.clickNomi()

    def tearDown(self):
        pass
        # self.baidu.quit()

if __name__ == "__main__":
    unittest.main