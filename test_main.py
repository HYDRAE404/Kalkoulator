from project import choose_calc, choose_conv, choose_oth
from calculator import Basic
from converters import Length, Area, Volume, Temperature
from others import PowerNRoot, Conditionals
from unittest.mock import Mock, patch


def test_choose_calc():
    with patch("calculator.Basic.getNums", new=Mock(return_value=(1, 2, 3))):
        with patch("builtins.input", new=Mock(return_value="1 2 3")):
            assert choose_calc("1") == Basic((1, 2, 3)).add()
            assert choose_calc("2") == Basic((1, 2, 3)).subtract()
            assert choose_calc("3") == Basic((1, 2, 3)).multiply()
            assert choose_calc("4") == Basic((1, 2, 3)).divide()
            assert choose_calc("5") == Basic((1, 2, 3)).modulo()


# SPECIAL CASE
def test_choose_calc_special():
    with patch("calculator.Basic.getNums", new=Mock(return_value=(1.7))):
        with patch("builtins.input", new=Mock(return_value="1.7")):
            assert choose_calc("1") == 1.7
            assert choose_calc("2") == 1.7
            assert choose_calc("3") == 1.7
            assert choose_calc("4") == 1.7
            assert choose_calc("5") == 1.7


def test_choose_calc_invalids():
    assert choose_calc("6") == "0x0"
    assert choose_calc("7") == "0x0"
    assert choose_calc("8") == "0x0"
    assert choose_calc("cat") == "0x0"
    assert choose_calc("dog") == "0x0"


def test_choose_conv():
    with patch("converters.Unit.getUnit", new=Mock(return_value=(1))):
        with patch("builtins.input", new=Mock(return_value="1")):
            assert choose_conv("1") == Length(1).engine()
            assert choose_conv("2") == Area(1).engine()
            assert choose_conv("3") == Volume(1).engine()
            assert choose_conv("4") == Temperature(1).engine()


def test_choose_conv_invalids():
    assert choose_conv("5") == "0x0"
    assert choose_conv("6") == "0x0"
    assert choose_conv("one") == "0x0"
    assert choose_conv("guan") == "0x0"
    assert choose_conv("1.0") == "0x0"


def test_choose_oth():
    with patch("others.PowerNRoot.getRational", new=Mock(return_value=(50, 2))):
        with patch("builtins.input", new=Mock(return_value="50")):
            with patch("builtins.input", new=Mock(return_value="2")):
                assert choose_oth("1") == PowerNRoot(50, 2).power()
                assert choose_oth("2") == PowerNRoot(50, 2).roots()

    with patch("others.Conditionals.getCondNums", new=Mock(return_value=(265, 879))):
        with patch("builtins.input", new=Mock(return_value="265")):
            with patch("builtins.input", new=Mock(return_value="879")):
                assert choose_oth("3") == Conditionals(265, 879).isGreater()
                assert choose_oth("4") == Conditionals(265, 879).isLess()
                assert choose_oth("5") == Conditionals(
                    265, 879).isGreaterEqual()
                assert choose_oth("6") == Conditionals(265, 879).isLessEqual()
                assert choose_oth("7") == Conditionals(265, 879).isEqual()
                assert choose_oth("8") == Conditionals(265, 879).isNotEqual()


def test_choose_oth_invalids():
    assert choose_oth("9") == "0x0"
    assert choose_oth("10") == "0x0"
    assert choose_oth("alksbadbjkbhvads") == "0x0"
    assert choose_oth("SHVSZALSKCNALSLCKAS") == "0x0"
    assert choose_oth("3/") == "0x0"
