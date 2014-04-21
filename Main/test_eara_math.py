import unittest
import math
from eara_math import DescStat
from eara_math import Integral


class Test(unittest.TestCase):

    def setUp(self):
        self.list1 = [1, 2, 3]

    def test_summation(self):
        actual = DescStat.summation(self.list1)
        expected = 6.0
        self.assertEqual(actual, expected)

    def test_summation_func_item(self):
        actual = DescStat.summation(self.list1,
                                    lambda x: 2 * x)
        expected = 12.0
        self.assertEqual(actual, expected)

    def test_summation_func_item_func_total(self):
        actual = DescStat.summation(self.list1,
                                    lambda x: 2 * x,
                                    lambda x: 2 * x)
        expected = 24.0
        self.assertEqual(actual, expected)

    def test_summation_func_total(self):
        actual = DescStat.summation(self.list1,
                                    func_total=lambda x: 2 * x)
        expected = 12.0
        self.assertEqual(actual, expected)

    def test_trapeziod_rule_sinx_n10(self):
        integral1 = Integral(0, math.pi, 10,
                             lambda x: float(math.sin(x)), 'sin(x) dx')
        actual = DescStat.trapeziod_rule(integral1)
        expected = '[l=0,u=3.14159265359, n=10] sin(x) dx = 1.98352353751'
        self.assertEqual(actual, expected)

    def test_trapeziod_rule_sinx_n100(self):
        integral1 = Integral(0, math.pi, 100,
                             lambda x: float(math.sin(x)), 'sin(x) dx')
        actual = DescStat.trapeziod_rule(integral1)
        expected = '[l=0,u=3.14159265359, n=100] sin(x) dx = 1.99983550389'
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()