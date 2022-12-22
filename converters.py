"""
FUNCTION/CLASS DESC SUMMARY

Unit[class]: a class representing a unit (inherited by other classes)

    getUnit: prompts the user for a number. Returns that number for later use.
    showConv: displays the available actions for conversion
    conv_from: prompts the user which unit to convert from (will be used in other classes)
    conv_to_prompt: prompts the user which unit to convert to (will be used in other classes)


SIMILAR METHODS (common methods among the classes except Unit)
    engine: starts the conversion process
    conv_to: prompts (using conv_to_prompt) the user which unit to convert to (with choices and validation)
        :return: the input of the user (for later use)
        :return type: int

Length[class]: a class consisting of supported length conversions

    km_conv: returns the conversions from km to the supported units
    m_conv: returns the conversions from m to the supported units
    cm_conv: returns the conversions from cm to the supported units
    mm_conv: returns the conversions from mm to the supported units
    mi_conv: returns the conversions from mi to the supported units
    yd_conv: returns the conversions from yd to the supported units
    ft_conv: returns the conversions from ft to the supported units
    in_conv: returns the conversions from in to the supported units

Area[class]: a class consisting of supported area conversions

    km2_conv: returns the conversions from km² to the supported units
    m2_conv: returns the conversions from m² to the supported units
    mi2_conv: returns the conversions from mi² to the supported units
    yd2_conv: returns the conversions from yd² to the supported units
    ft2_conv: returns the conversions from ft² to the supported units
    in2_conv: returns the conversions from in² to the supported units
    ha_conv: returns the conversions from ha to the supported units
    acre_conv: returns the conversions from acre to the supported units

Volume[class]: a class consisting of supported volume conversions

    L_conv: returns the conversions from L to the supported units
    usgal_conv: returns the conversions from us gal to the supported units
    mL_conv: returns the conversions from mL to the supported units
    m3_conv: returns the conversions from m³ to the supported units
    uspt_conv: returns the conversions from us pt (pint) to the supported units
    floz_conv: returns the conversions from fl oz to the supported units
    ft3_conv: returns the conversions from ft³ to the supported units
    in3_conv: returns the conversions from in³ to the supported units

Temperature: a class consisting of supported temperature conversions

    C_conv: returns the conversions from °C to the supported units
    F_conv: returns the conversions from °F to the supported units
    K_conv: returns the conversions from K to the supported units

* returned unit depends on the value of conv_to
"""


import csv
from tabulate import tabulate
from fractions import Fraction as frac


# NOTE: ANY FRACTION INPUT BY THE USER ARE UNSUPPORTED (yet)


class Unit:
    def __init__(self, unit: int | float | str = 0):
        self.unit = unit

    @staticmethod
    def getUnit():
        while True:
            try:
                return int(input("Type the number you want to convert: "))
            except ValueError:
                try:
                    return float(input("Type the number you want to convert: "))
                except ValueError:
                    print("Invalid input")

    @staticmethod
    def showConv():
        table = []

        with open("options/conv_opts.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                table.append([row["#"], row["Converters"]])

        header = ["#", "Converters"]

        return tabulate(table, header, tablefmt="grid")

    @staticmethod
    def conv_from():
        return input("Choose a unit to convert from: ")

    @staticmethod
    def conv_to_prompt() -> str:
        convto: str = input("Choose a conversion: ")
        if convto.isnumeric():
            return convto
        else:
            raise ValueError

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, unit: int | float | str):
        self._unit = unit


# GLOBAL VARIABLES
LUnits: list[str] = ["Kilometre", "Meter", "Centimeter",
                     "Millimetre", "Mile", "Yard", "Foot", "Inch"]


class Length(Unit):
    def __init__(self, unit):
        super().__init__(unit)

    """Starts the conversion of a length"""

    def engine(self) -> str | None:
        global fromC
        while True:
            for c in range(len(LUnits)):
                print(f"{c+1}: {LUnits[c]}")

            print()

            match fromU := Unit.conv_from():
                case "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8":
                    fromC = LUnits.pop(int(fromU) - 1)
                    print()
                    if fromU == "1":
                        return self.km_conv()
                    elif fromU == "2":
                        return self.m_conv()
                    elif fromU == "3":
                        return self.cm_conv()
                    elif fromU == "4":
                        return self.mm_conv()
                    elif fromU == "5":
                        return self.mi_conv()
                    elif fromU == "6":
                        return self.yd_conv()
                    elif fromU == "7":
                        return self.ft_conv()
                    else:
                        return self.in_conv()

                case _:
                    print(f"Invalid option.\n")

    def conv_to(self):
        while True:
            for u in range(len(LUnits)):
                print(f"{u+1}: {fromC} to {LUnits[u]}")

            print()

            try:
                prompt: int = int(Unit.conv_to_prompt())
            except ValueError:
                print(f"Invalid option.\n")
            else:
                if prompt not in [i for i in range(1, 8)]:
                    print(f"Invalid option.\n")
                else:
                    return prompt

    def km_conv(self):
        match self.conv_to():
            # converts kilometre to meters
            case 1: return f"{self.unit * 1000} m"
            # converts kilometre to centimetre
            case 2: return f"{self.unit * 100000} cm"
            # converts kilometre to millimetre
            case 3: return f"{self.unit * 0.000001} mm"
            # converts kilometre to miles
            case 4: return f"{self.unit / 1.609} mi"
            # converts kilometre to yards
            case 5: return f"{self.unit * 1094} yd"
            # converts kilometre to feet
            case 6: return f"{self.unit * 3281} ft"
            # converts kilometre to inche
            case 7: return f"{self.unit * 39370} in"

    def m_conv(self):
        match self.conv_to():
            # converts meters to kilometre
            case 1: return f"{self.unit / 1000} km"
            # converts kilometre to centimetre
            case 2: return f"{self.unit * 100} cm"
            # converts kilometre to millimetre
            case 3: return f"{self.unit * 1000} mm"
            # converts kilometre to miles
            case 4: return f"{self.unit / 1609} mi"
            # converts kilometre to yards
            case 5: return f"{self.unit * 1.094} yd"
            # converts kilometre to feet
            case 6: return f"{self.unit * 3.281} ft"
            # converts kilometre to inches
            case 7: return f"{self.unit * 39.37} in"

    def cm_conv(self):
        match self.conv_to():
            # converts centimeters to kilometre
            case 1: return f"{self.unit * 100000} km"
            # converts centimetre to meters
            case 2: return f"{self.unit / 100} m"
            # converts centimetre to millimetre
            case 3: return f"{self.unit * 10} mm"
            # converts centimetre to miles
            case 4: return f"{self.unit / 160900} mi"
            # converts centimetre to yards
            case 5: return f"{self.unit / 91.44} yd"
            # converts centimetre to feet
            case 6: return f"{self.unit / 30.48} ft"
            # converts centimetre to inches
            case 7: return f"{self.unit / 2.54} in"

    def mm_conv(self):
        match self.conv_to():
            # converts millimetre to kilometre
            case 1: return f"{self.unit / 1000000} km"
            # converts millimetre to meter
            case 2: return f"{self.unit / 1000} m"
            # converts millimetre to centimeter
            case 3: return f"{self.unit / 10} cm"
            # converts millimetre to mile
            case 4: return f"{self.unit / (1.609 * 10**6)} mi"
            # converts millimetre to yard
            case 5: return f"{self.unit / 914.4} yd"
            # converts millimetre to foot
            case 6: return f"{self.unit / 304.8} ft"
            # converts millimetre to inch
            case 7: return f"{self.unit / 25.4} in"

    def mi_conv(self):
        match self.conv_to():
            # converts mile to kilometre
            case 1: return f"{self.unit * 1.609} km"
            # converts mile to meter
            case 2: return f"{self.unit * 1609} m"
            # converts mile to centimeter
            case 3: return f"{self.unit * 160900} cm"
            # converts mile to millimetre
            case 4: return f"{self.unit * (1.609 * 10**6)} mm"
            # converts mile to yard
            case 5: return f"{self.unit * 1760} yd"
            # converts mile to foot
            case 6: return f"{self.unit * 5280} ft"
            # converts mile to inch
            case 7: return f"{self.unit * 63360} in"

    def yd_conv(self):
        match self.conv_to():
            # converts yard to kilometre
            case 1: return f"{self.unit / 1094} km"
            # converts yard to meter
            case 2: return f"{self.unit / 1.094} m"
            # converts yard to centimeter
            case 3: return f"{self.unit * 91.44} cm"
            # converts yard to millimetre
            case 4: return f"{self.unit * 914.4} mm"
            # converts yard to mile
            case 5: return f"{self.unit / 1760} mi"
            # converts yard to foot
            case 6: return f"{self.unit * 3} ft"
            # converts yard to inch
            case 7: return f"{self.unit * 36} in"

    def ft_conv(self):
        match self.conv_to():
            # converts foot to kilometre
            case 1: return f"{self.unit / 3281} km"
            # converts foot to meter
            case 2: return f"{self.unit / 3.281} m"
            # converts foot to centimeter
            case 3: return f"{self.unit * 30.48} cm"
            # converts foot to millimetre
            case 4: return f"{self.unit * 304.8} mm"
            # converts foot to mile
            case 5: return f"{self.unit / 5280} mi"
            # converts foot to yard
            case 6: return f"{self.unit / 3} yd"
            # converts foot to inch
            case 7: return f"{self.unit * 12} in"

    def in_conv(self):
        match self.conv_to():
            # converts inch to kilometre
            case 1: return f"{self.unit / 39370} km"
            # converts inch to meter
            case 2: return f"{self.unit / 39.37} m"
            # converts inch to centimeter
            case 3: return f"{self.unit * 2.54} cm"
            # converts inch to millimetre
            case 4: return f"{self.unit * 25.4} mm"
            # converts inch to mile
            case 5: return f"{self.unit / 63360} mi"
            # converts inch to yard
            case 6: return f"{self.unit / 36} yd"
            # converts inch to foot
            case 7: return f"{self.unit / 12} ft"


# GLOBAL VARIABLE
AUnits: list[str] = ["Square kilometer", "Square meter", "Square mile",
                     "Square yard", "Square foot", "Square inch", "Hectare", "Acre"]


class Area(Unit):
    def __init__(self, unit):
        super().__init__(unit)

    """Starts the conversion of an area"""

    def engine(self) -> str | None:
        global fromC
        while True:
            for c in range(len(AUnits)):
                print(f"{c+1}: {AUnits[c]}")

            print()

            match fromU := Unit.conv_from():
                case "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8":
                    fromC = AUnits.pop(int(fromU) - 1)
                    print()
                    if fromU == "1":
                        return self.km2_conv()
                    elif fromU == "2":
                        return self.m2_conv()
                    elif fromU == "3":
                        return self.mi2_conv()
                    elif fromU == "4":
                        return self.yd2_conv()
                    elif fromU == "5":
                        return self.ft2_conv()
                    elif fromU == "6":
                        return self.in2_conv()
                    elif fromU == "7":
                        return self.ha_conv()
                    else:
                        return self.acre_conv()

                case _:
                    print(f"Invalid option.\n")

    def conv_to(self):
        while True:
            for u in range(len(AUnits)):
                print(f"{u+1}: {fromC} to {AUnits[u]}")

            print()

            try:
                prompt = int(Unit.conv_to_prompt())
            except ValueError:
                print(f"Invalid option.\n")
            else:
                if prompt not in [i for i in range(1, 8)]:
                    print(f"Invalid option.\n")
                else:
                    return prompt

    def km2_conv(self):
        match self.conv_to():
            # converts sq kilometer to sq meter
            case 1: return f"{self.unit * 1000000} m\u00b2"
            # converts sq kilometer to sq mile
            case 2: return f"{self.unit / 2.59} mi\u00b2"
            # converts sq kilometer to sq yard
            case 3: return f"{self.unit * 1.196e+6} yd\u00b2"
            # converts sq kilometer to sq foot
            case 4: return f"{self.unit * 1.076e+7} ft\u00b2"
            # converts sq kilometer to sq inch
            case 5: return f"{self.unit * 1.55e+9} in\u00b2"
            # converts sq kilometer to hectare
            case 6: return f"{self.unit * 100} ha"
            # converts sq kilometer to acre
            case 7: return f"{self.unit * 247.1} acre"

    def m2_conv(self):
        match self.conv_to():
            # converts sq meter to sq kilometer
            case 1: return f"{self.unit / 1e+6} km\u00b2"
            # converts sq meter to sq mile
            case 2: return f"{self.unit / 2.59e+6} mi\u00b2"
            # converts sq meter to sq yard
            case 3: return f"{self.unit * 1.196} yd\u00b2"
            # converts sq meter to sq foot
            case 4: return f"{self.unit * 10.764} ft\u00b2"
            # converts sq meter to sq inch
            case 5: return f"{self.unit * 1550} in\u00b2"
            # converts sq meter to hectare
            case 6: return f"{self.unit / 10000} ha"
            # converts sq meter to acre
            case 7: return f"{self.unit / 4047} acre"

    def mi2_conv(self):
        match self.conv_to():
            # converts sq mile to sq kilometer
            case 1: return f"{self.unit * 2.59} km\u00b2"
            # converts sq mile to sq meter
            case 2: return f"{self.unit * 2.59e+6} m\u00b2"
            # converts sq mile to sq yard
            case 3: return f"{self.unit * 3.098e+6} yd\u00b2"
            # converts sq mile to sq foot
            case 4: return f"{self.unit * 2.788e+7} ft\u00b2"
            # converts sq mile to sq inch
            case 5: return f"{self.unit * 4.014e+9} in\u00b2"
            # converts sq mile to hectare
            case 6: return f"{self.unit * 259} ha"
            # converts sq mile to acre
            case 7: return f"{self.unit * 640} acre"

    def yd2_conv(self):
        match self.conv_to():
            # converts sq yard to sq kilometer
            case 1: return f"{self.unit / 1.196e+6} km\u00b2"
            # converts sq yard to sq meter
            case 2: return f"{self.unit / 1.196} m\u00b2"
            # converts sq yard to sq mile
            case 3: return f"{self.unit / 3.098e+6} mi\u00b2"
            # converts sq yard to sq foot
            case 4: return f"{self.unit * 9} ft\u00b2"
            # converts sq yard to sq inch
            case 5: return f"{self.unit * 1296} in\u00b2"
            # converts sq yard to hectare
            case 6: return f"{self.unit / 11960} ha"
            # converts sq yard to acre
            case 7: return f"{self.unit / 4840} acre"

    def ft2_conv(self):
        match self.conv_to():
            # converts sq foot to sq kilometer
            case 1: return f"{self.unit / 1.076e+7} km\u00b2"
            # converts sq foot to sq meter
            case 2: return f"{self.unit / 10.764} m\u00b2"
            # converts sq foot to sq mile
            case 3: return f"{self.unit / 2.788e+7} mi\u00b2"
            # converts sq foot to sq yard
            case 4: return f"{self.unit / 9} yd\u00b2"
            # converts sq foot to sq inch
            case 5: return f"{self.unit * 144} in\u00b2"
            # converts sq foot to hectare
            case 6: return f"{self.unit / 107600} ha"
            # converts sq foot to acre
            case 7: return f"{self.unit / 43560} acre"

    def in2_conv(self):
        match self.conv_to():
            # converts sq inch to sq kilometer
            case 1: return f"{self.unit / 1.55e+9} km\u00b2"
            # converts sq inch to sq meter
            case 2: return f"{self.unit / 1550} m\u00b2"
            # converts sq inch to sq mile
            case 3: return f"{self.unit / 4.014e+9} mi\u00b2"
            # converts sq inch to sq yard
            case 4: return f"{self.unit / 1296} yd\u00b2"
            # converts sq inch to sq foot
            case 5: return f"{self.unit / 144} ft\u00b2"
            # converts sq inch to hectare
            case 6: return f"{self.unit / 1.55e+7} ha"
            # converts sq inch to acre
            case 7: return f"{self.unit / 6.273e+6} acre"

    def ha_conv(self):
        match self.conv_to():
            # converts hectare to sq kilometer
            case 1: return f"{self.unit / 100} km\u00b2"
            # converts hectare to sq meter
            case 2: return f"{self.unit * 10000} m\u00b2"
            # converts hectare to sq mile
            case 3: return f"{self.unit / 259} mi\u00b2"
            # converts hectare to sq yard
            case 4: return f"{self.unit * 11960} yd\u00b2"
            # converts hectare to sq foot
            case 5: return f"{self.unit * 107600} ft\u00b2"
            # converts hectare to sq inch
            case 6: return f"{self.unit * 1.55e+7} in\u00b2"
            # converts hectare to acre
            case 7: return f"{self.unit * 2.471} acre"

    def acre_conv(self):
        match self.conv_to():
            # converts acre to sq kilometer
            case 1: return f"{self.unit / 247.1} km\u00b2"
            # converts acre to sq meter
            case 2: return f"{self.unit * 4047} m\u00b2"
            # converts acre to sq mile
            case 3: return f"{self.unit / 640} mi\u00b2"
            # converts acre to sq yard
            case 4: return f"{self.unit * 4840} yd\u00b2"
            # converts acre to sq foot
            case 5: return f"{self.unit * 43560} ft\u00b2"
            # converts acre to sq inch
            case 6: return f"{self.unit * 6.273e+6} in\u00b2"
            # converts acre to hectare
            case 7: return f"{self.unit / 2.471} ha"


# GLOBAL VARIABLE
VUnits: list[str] = ["Liter", "Us Liquid Gallon", "Milliliter", "Cubic Meter",
                     "Us Liquid Pint", "Fluid Ounce", "Cubic Foot", "Cubic Inch"]


class Volume(Unit):
    def __init__(self, unit):
        super().__init__(unit)

    """Starts the conversion of a volume"""

    def engine(self) -> str | None:
        global fromC
        while True:
            for c in range(len(VUnits)):
                print(f"{c+1}: {VUnits[c]}")

            print()

            match fromU := Unit.conv_from():
                case "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8":
                    fromC = VUnits.pop(int(fromU) - 1)
                    print()
                    if fromU == "1":
                        return self.L_conv()
                    elif fromU == "2":
                        return self.usgal_conv()
                    elif fromU == "3":
                        return self.mL_conv()
                    elif fromU == "4":
                        return self.m3_conv()
                    elif fromU == "5":
                        return self.uspt_conv()
                    elif fromU == "6":
                        return self.floz_conv()
                    elif fromU == "7":
                        return self.ft3_conv()
                    else:
                        return self.in3_conv()

                case _:
                    print(f"Invalid option.\n")

    def conv_to(self):
        while True:
            for u in range(len(VUnits)):
                print(f"{u+1}: {fromC} to {VUnits[u]}")

            print()

            try:
                prompt = int(Unit.conv_to_prompt())
            except ValueError:
                print(f"Invalid option.\n")
            else:
                if prompt not in [i for i in range(1, 8)]:
                    print(f"Invalid option.\n")
                else:
                    return prompt

    def L_conv(self):
        match self.conv_to():
            # converts liter/s to US liquid gallon
            case 1: return f"{self.unit / 3.785} US gal"
            # converts liter/s to milliliter
            case 2: return f"{self.unit * 1000} mL"
            # converts liter/s to cubic meter
            case 3: return f"{self.unit / 1000} m\u00b3"
            # converts liter/s to US liquid pint
            case 4: return f"{self.unit * 2.113} US pt"
            # converts liter/s to fluid ounce
            case 5: return f"{self.unit * 33.814} fl oz"
            # converts liter/s to cubic foot
            case 6: return f"{self.unit / 28.317} ft\u00b3"
            # converts liter/s to cubic inch
            case 7: return f"{self.unit * 61.024} in\u00b3"

    def usgal_conv(self):
        match self.conv_to():
            # converts US liquid gallon to liter
            case 1: return f"{self.unit * 3.785} L"
            # converts US liquid gallon to milliliter
            case 2: return f"{self.unit * 3785} mL"
            # converts US liquid gallon to cubic meter
            case 3: return f"{self.unit / 264.2} m\u00b3"
            # converts US liquid gallon to US liquid pint
            case 4: return f"{self.unit * 8} US pt"
            # converts US liquid gallon to fluid ounce
            case 5: return f"{self.unit * 128} fl oz"
            # converts US liquid gallon to cubic foot
            case 6: return f"{self.unit / 7.48} ft\u00b3"
            # converts US liquid gallon to cubic inch
            case 7: return f"{self.unit * 231} in\u00b3"

    def mL_conv(self):
        match self.conv_to():
            # converts milliliter to liter
            case 1: return f"{self.unit / 1000} L"
            # converts milliliter to US liquid gallon
            case 2: return f"{self.unit / 3785} US gal"
            # converts milliliter to cubic meter
            case 3: return f"{self.unit / 1e+6} m\u00b3"
            # converts milliliter to US liquid pint
            case 4: return f"{self.unit / 473.2} US pt"
            # converts milliliter to fluid ounce
            case 5: return f"{self.unit / 29.574} fl oz"
            # converts milliliter to cubic foot
            case 6: return f"{self.unit / 28320} ft\u00b3"
            # converts milliliter to cubic inch
            case 7: return f"{self.unit / 16.387} in\u00b3"

    def m3_conv(self):
        match self.conv_to():
            # converts cubic meter to liter
            case 1: return f"{self.unit * 1000} L"
            # converts cubic meter to US liquid gallon
            case 2: return f"{self.unit * 264.2} US gal"
            # converts cubic meter to milliliter
            case 3: return f"{self.unit * 1e+6} mL"
            # converts cubic meter to US liquid pint
            case 4: return f"{self.unit * 2113} US pt"
            # converts cubic meter to fluid ounce
            case 5: return f"{self.unit * 33810} fl oz"
            # converts cubic meter to cubic foot
            case 6: return f"{self.unit * 35.315} ft\u00b3"
            # converts cubic meter to cubic inch
            case 7: return f"{self.unit * 61020} in\u00b3"

    def uspt_conv(self):
        match self.conv_to():
            # converts US liquid pint to liter
            case 1: return f"{self.unit / 2.113} L"
            # converts US liquid pint to US liquid gallon
            case 2: return f"{self.unit / 8} US gal"
            # converts US liquid pint to milliliter
            case 3: return f"{self.unit * 473.2} mL"
            # converts US liquid pint to cubic meter
            case 4: return f"{self.unit / 2113} m\u00b3"
            # converts US liquid pint to fluid ounce
            case 5: return f"{self.unit * 16} fl oz"
            # converts US liquid pint to cubic foot
            case 6: return f"{self.unit / 59.844} ft\u00b3"
            # converts US liquid pint to cubic inch
            case 7: return f"{self.unit * 28.875} in\u00b3"

    def floz_conv(self):
        match self.conv_to():
            # converts fluid ounce to liter
            case 1: return f"{self.unit / 33.814} L"
            # converts fluid ounce to US liquid gallon
            case 2: return f"{self.unit / 128} US gal"
            # converts fluid ounce to milliliter
            case 3: return f"{self.unit * 29.574} mL"
            # converts fluid ounce to cubic meter
            case 4: return f"{self.unit / 33810} m\u00b3"
            # converts fluid ounce to US liquid pint
            case 5: return f"{self.unit / 16} US pt"
            # converts fluid ounce to cubic foot
            case 6: return f"{self.unit / 957.5} ft\u00b3"
            # converts fluid ounce to cubic inch
            case 7: return f"{self.unit * 1.805} in\u00b3"

    def ft3_conv(self):
        match self.conv_to():
            # converts cubic foot to liter
            case 1: return f"{self.unit * 28.317} L"
            # converts cubic foot to US liquid gallon
            case 2: return f"{self.unit * 7.481} US gal"
            # converts cubic foot to milliliter
            case 3: return f"{self.unit * 28320} mL"
            # converts cubic foot to cubic meter
            case 4: return f"{self.unit / 35.315} m\u00b3"
            # converts cubic foot to US liquid pint
            case 5: return f"{self.unit * 59.844} US pt"
            # converts cubic foot to fluid ounce
            case 6: return f"{self.unit * 957.5} fl oz"
            # converts cubic foot to cubic inch
            case 7: return f"{self.unit * 1728} in\u00b3"

    def in3_conv(self):
        match self.conv_to():
            # converts cubic inch to liter
            case 1: return f"{self.unit / 61.024} L"
            # converts cubic inch to US liquid gallon
            case 2: return f"{self.unit / 231} US gal"
            # converts cubic inch to milliliter
            case 3: return f"{self.unit * 16.387} mL"
            # converts cubic inch to cubic meter
            case 4: return f"{self.unit / 61020} m\u00b3"
            # converts cubic inch to US liquid pint
            case 5: return f"{self.unit / 28.875} US pt"
            # converts cubic inch to fluid ounce
            case 6: return f"{self.unit / 1.805} fl oz"
            # converts cubic inch to cubic foot
            case 7: return f"{self.unit / 1728} ft\u00b3"


# GLOBAL VARIABLE

TUnit = ["Celsius", "Fahrenheit", "Kelvin"]


class Temperature(Unit):
    def __init__(self, unit):
        super().__init__(unit)

    """Starts the conversion of temperature"""

    def engine(self) -> str | None:
        global fromC
        while True:
            for c in range(len(TUnit)):
                print(f"{c+1}: {TUnit[c]}")

            print()

            match fromU := Unit.conv_from():
                case "1" | "2" | "3":
                    fromC = TUnit.pop(int(fromU) - 1)
                    print()
                    if fromU == "1":
                        return self.C_conv()
                    elif fromU == "2":
                        return self.F_conv()
                    else:
                        return self.K_conv()

                case _:
                    print(f"Invalid option.\n")

    def conv_to(self):
        while True:
            for u in range(len(TUnit)):
                print(f"{u+1}: {fromC} to {TUnit[u]}")

            print()

            try:
                prompt = int(Unit.conv_to_prompt())
            except ValueError:
                print(f"Invalid option.\n")
            else:
                if prompt not in [i for i in range(1, 4)]:
                    print(f"Invalid option.\n")
                else:
                    return prompt

    def C_conv(self):
        match self.conv_to():
            # converts celsius to fahrenheit
            case 1: return f"{float(self.unit * frac(9, 5)) + 32} \u00b0F"
            # converts celsius to kelvin
            case 1: return f"{self.unit + 273.15} K"

    def F_conv(self):
        match self.conv_to():
            # converts fahrenheit to celsius
            case 1: return f"{float(self.unit - 32) * frac(5/9)} \u00b0C"
            # converts fahrenheit to kelvin
            case 2: return f"{float(self.unit - 32) * frac(5, 9) + 273.15} K"

    def K_conv(self):
        match self.conv_to():
            # converts kelvin to celsius
            case 1: return f"{self.unit - 273.15} \u00b0C"
            # converts kelvin to fahrenheit
            case 2: return f"{float(self.unit - 273.15) * frac(9, 5) + 32} \u00b0F"
