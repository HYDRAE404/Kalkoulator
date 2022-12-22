import unittest
from unittest.mock import Mock, patch
from converters import Length, Area, Volume, Temperature

length = Length(1)
area = Area(1)
vol = Volume(1)
temp = Temperature(1)


class TestLength:
    @staticmethod
    def test_km():
        with patch("converters.Length.conv_to", new=Mock(return_value=1)):
            with patch("builtins.input", new=Mock(return_value="1")):
                assert length.km_conv() == "1000 m"

    @staticmethod
    def test_m():
        with patch("converters.Length.conv_to", new=Mock(return_value=2)):
            with patch("builtins.input", new=Mock(return_value="2")):
                assert length.m_conv() == "100 cm"

    @staticmethod
    def test_cm():
        with patch("converters.Length.conv_to", new=Mock(return_value=3)):
            with patch("builtins.input", new=Mock(return_value="3")):
                assert length.cm_conv() == "10 mm"

    @staticmethod
    def test_mm():
        with patch("converters.Length.conv_to", new=Mock(return_value=4)):
            with patch("builtins.input", new=Mock(return_value="4")):
                assert length.mm_conv() == f"{1/1_609_000} mi"

    @staticmethod
    def test_mi():
        with patch("converters.Length.conv_to", new=Mock(return_value=5)):
            with patch("builtins.input", new=Mock(return_value="5")):
                assert length.mi_conv() == "1760 yd"

    @staticmethod
    def test_yd():
        with patch("converters.Length.conv_to", new=Mock(return_value=6)):
            with patch("builtins.input", new=Mock(return_value="6")):
                assert length.yd_conv() == "3 ft"

    @staticmethod
    def test_ft():
        with patch("converters.Length.conv_to", new=Mock(return_value=7)):
            with patch("builtins.input", new=Mock(return_value="7")):
                assert length.ft_conv() == "12 in"

    @staticmethod
    def test_in():
        with patch("converters.Length.conv_to", new=Mock(return_value=3)):
            with patch("builtins.input", new=Mock(return_value="3")):
                assert length.in_conv() == "2.54 cm"


class TestArea:
    @staticmethod
    def test_km2():
        with patch("converters.Area.conv_to", new=Mock(return_value=1)):
            with patch("builtins.input", new=Mock(return_value="1")):
                assert area.km2_conv() == "1000000 m\u00b2"

    @staticmethod
    def test_m2():
        with patch("converters.Area.conv_to", new=Mock(return_value=2)):
            with patch("builtins.input", new=Mock(return_value="2")):
                assert area.m2_conv() == f"{1/2.59e+6} mi\u00b2"

    @staticmethod
    def test_mi2():
        with patch("converters.Area.conv_to", new=Mock(return_value=3)):
            with patch("builtins.input", new=Mock(return_value="3")):
                assert area.mi2_conv() == f"{1*3.098e+6} yd\u00b2"

    @staticmethod
    def test_yd2():
        with patch("converters.Area.conv_to", new=Mock(return_value=4)):
            with patch("builtins.input", new=Mock(return_value="4")):
                assert area.yd2_conv() == "9 ft\u00b2"

    @staticmethod
    def test_ft2():
        with patch("converters.Area.conv_to", new=Mock(return_value=5)):
            with patch("builtins.input", new=Mock(return_value="5")):
                assert area.ft2_conv() == "144 in\u00b2"

    @staticmethod
    def test_in2():
        with patch("converters.Area.conv_to", new=Mock(return_value=6)):
            with patch("builtins.input", new=Mock(return_value="6")):
                assert area.in2_conv() == f"{1/1.55e+7} ha"

    @staticmethod
    def test_ha():
        with patch("converters.Area.conv_to", new=Mock(return_value=7)):
            with patch("builtins.input", new=Mock(return_value="7")):
                assert area.ha_conv() == "2.471 acre"

    @staticmethod
    def test_acre():
        with patch("converters.Area.conv_to", new=Mock(return_value=3)):
            with patch("builtins.input", new=Mock(return_value="3")):
                assert area.acre_conv() == "0.0015625 mi\u00b2"


class TestVolume:
    @staticmethod
    def test_L():
        with patch("converters.Volume.conv_to", new=Mock(return_value=1)):
            with patch("builtins.input", new=Mock(return_value="1")):
                assert vol.L_conv() == f"{1/3.785} US gal"

    @staticmethod
    def test_usgal():
        with patch("converters.Volume.conv_to", new=Mock(return_value=2)):
            with patch("builtins.input", new=Mock(return_value="2")):
                assert vol.usgal_conv() == "3785 mL"

    @staticmethod
    def test_mL():
        with patch("converters.Volume.conv_to", new=Mock(return_value=3)):
            with patch("builtins.input", new=Mock(return_value="3")):
                assert vol.mL_conv() == f"{1/1e+6} m\u00b3"

    @staticmethod
    def test_m3():
        with patch("converters.Volume.conv_to", new=Mock(return_value=4)):
            with patch("builtins.input", new=Mock(return_value="4")):
                assert vol.m3_conv() == "2113 US pt"

    @staticmethod
    def test_uspt():
        with patch("converters.Volume.conv_to", new=Mock(return_value=5)):
            with patch("builtins.input", new=Mock(return_value="5")):
                assert vol.uspt_conv() == "16 fl oz"

    @staticmethod
    def test_floz():
        with patch("converters.Volume.conv_to", new=Mock(return_value=6)):
            with patch("builtins.input", new=Mock(return_value="6")):
                assert vol.floz_conv() == f"{1/957.5} ft\u00b3"

    @staticmethod
    def test_ft3():
        with patch("converters.Volume.conv_to", new=Mock(return_value=7)):
            with patch("builtins.input", new=Mock(return_value="7")):
                assert vol.ft3_conv() == "1728 in\u00b3"

    @staticmethod
    def test_in3():
        with patch("converters.Volume.conv_to", new=Mock(return_value=3)):
            with patch("builtins.input", new=Mock(return_value="3")):
                assert vol.in3_conv() == "16.387 mL"


class TestTemperature:
    @staticmethod
    def test_C():
        with patch("converters.Temperature.conv_to", new=Mock(return_value=1)):
            with patch("builtins.input", new=Mock(return_value="1")):
                assert temp.C_conv() == "33.8 \u00b0F"

    @staticmethod
    def test_F():
        with patch("converters.Temperature.conv_to", new=Mock(return_value=2)):
            with patch("builtins.input", new=Mock(return_value="2")):
                assert temp.F_conv() == "255.92777777777775 K"

    @staticmethod
    def test_K():
        with patch("converters.Temperature.conv_to", new=Mock(return_value=1)):
            with patch("builtins.input", new=Mock(return_value="1")):
                assert temp.K_conv() == "-272.15 \u00b0C"
