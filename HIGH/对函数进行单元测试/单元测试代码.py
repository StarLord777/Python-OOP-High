import unittest
from 单元测试 import add,cheng

class Mytest(unittest.TestCase):
    def setUp(self):
        print('开始测试时会调用')
    def tearDown(self):
        print('结束测试时会调用')

    def test_add(self):
        self.assertEqual(add(2,7),9,'加法有误')
    def test_cheng(self):
        self.assertEqual(cheng(5,7),35,'乘法有误')


if __name__ == '__main__':
    unittest.main()