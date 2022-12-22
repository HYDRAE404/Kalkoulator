import unittest
import pytest
from calculator import Basic

num_set1: tuple[int] = (1, 2, 3)
num_set2: tuple[int] = (9, 56, 14)
num_set3: tuple[float] = (6.8, 0.64, 7.1)

# SPECIAL CASES
spec_case1: tuple[float, int] = (51.9, 0, 14.54, 413.5)

nums_sum = {
    num_set1: 6,
    num_set2: 79,
    num_set3: 14.54
}

nums_diff = {
    num_set1: -4,
    num_set2: -61,
    num_set3: -0.9399999999999995
}

nums_prod = {
    num_set1: 6,
    num_set2: 7056,
    num_set3: 30.8992
}

nums_quo = {
    num_set1: 0.16666666666666666,
    num_set2: 0.011479591836734694,
    num_set3: 1.4964788732394367
}

nums_mod = {
    num_set1: 1,
    num_set2: 9,
    num_set3: 0.3999999999999997
}


def test_add():
    for test in nums_sum:
        basic = Basic(test)
        assert basic.add() == nums_sum[test]


def test_sub():
    for test in nums_diff:
        basic = Basic(test)
        assert basic.subtract() == nums_diff[test]


def test_mult():
    for test in nums_prod:
        basic = Basic(test)
        assert basic.multiply() == nums_prod[test]


def test_div():
    for test in nums_quo:
        basic = Basic(test)
        assert basic.divide() == nums_quo[test]


def test_mod():
    for test in nums_mod:
        basic = Basic(test)
        assert basic.modulo() == nums_mod[test]


class TestSpecial(unittest.TestCase):
    basic = Basic(spec_case1)

    @classmethod
    def test_special_div(cls):
        assert cls.basic.divide() == "Undefined or Indeterminate"

    @classmethod
    def test_special_mod(cls):
        cls.basic.modulo() == "Cannot determine remainder."
