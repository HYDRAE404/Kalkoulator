from unittest.mock import Mock, patch
from others import PowerNRoot, Conditionals


class TestPowerNRoot:
    @staticmethod
    def test_power():
        pnr = PowerNRoot(3, 2)
        assert pnr.power() == 9
        pnr = PowerNRoot(90, 3)
        assert pnr.power() == 729000
        pnr = PowerNRoot(6, -5)
        assert pnr.power() == "1/7776"

    @staticmethod
    def test_roots():
        pnr = PowerNRoot(729, 3)
        assert pnr.roots() == 9
        pnr = PowerNRoot(50, 2)
        assert pnr.roots() == "5 √2"
        pnr = PowerNRoot(256, 6)
        assert pnr.roots() == "2 \u2076√4"
        pnr = PowerNRoot(0, 2)
        assert pnr.roots() == 0


class TestConditionals:
    cond1 = Conditionals(69, 42)
    cond2 = Conditionals(80, 80)
    cond3 = Conditionals(24, 96)

    def test_greater(cls):
        assert cls.cond1.isGreater() == True
        assert cls.cond2.isGreater() == False
        assert cls.cond3.isGreater() == False

    def test_less(cls):
        assert cls.cond1.isLess() == False
        assert cls.cond2.isLess() == False
        assert cls.cond3.isLess() == True

    def test_greater_equal(cls):
        assert cls.cond1.isGreaterEqual() == True
        assert cls.cond2.isGreaterEqual() == True
        assert cls.cond3.isGreaterEqual() == False

    def test_less_equal(cls):
        assert cls.cond1.isLessEqual() == False
        assert cls.cond2.isLessEqual() == True
        assert cls.cond3.isLessEqual() == True

    def test_equal(cls):
        assert cls.cond1.isEqual() == False
        assert cls.cond2.isEqual() == True
        assert cls.cond3.isEqual() == False

    def test_not_equal(cls):
        assert cls.cond1.isNotEqual() == True
        assert cls.cond2.isNotEqual() == False
        assert cls.cond3.isNotEqual() == True
