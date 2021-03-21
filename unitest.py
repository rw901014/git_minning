from timestamp import time_data1
from time_interval import time_interval
import unittest

list = [1,2,3]

class Test(unittest.TestCase):
    def test_timestampe(self):
        d = time_data1('2019-8-01 00:00:00')
        self.assertEqual(d, 1564614000)

    def test_time_interval(self):
        d = time_interval(list)
        self.assertEqual(d, 1)

if __name__ == '__main__':
    unittest.main()
