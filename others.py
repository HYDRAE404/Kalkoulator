"""
FUNCTION/CLASS DESC SUMMARY:

showConv[func]: displays the available actions for calculation

is_empty[func]: checks if an iterable is empty

PowerNRoot[class]: consists of exponentials (.. to the nth power) and roots (nth root of...)

    getRational: prompts the user for two numbers. Returns that number for later use.
    power: calculates the param base to the nth power using param ratex (as exponent)
    root: calculates the nth root of param base using param ratex (as index)

Conditionals[class]: compares two numbers for equality (=) or inequalities (>,≥,<,≤,≠)

    getCondNums: prompts the user for two numbers. Returns that number for later use.
    isGreater: compares if num1 is greater than num2
    isLess: compares if num1 is less than num2
    isGreaterEqual: compares if num1 is greater than or equal to num2
    isLessEqual: compares if num1 is less than or equal to num2
    isEqual: compares if num1 is equal to num2
    isNotEqual: compares if num1 is not equal to num2
"""

import csv
from tabulate import tabulate
from sympy import *
from calculator import Basic
from fractions import Fraction as frac

# NOTE: ANY FRACTION INPUT BY THE USER ARE UNSUPPORTED (yet)

"""
displays the available actions for calculation using the tabulate module

:return: a neatly formatted table
:return type: str
"""


def showOth():
    table = []

    with open("options/oth_opts.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            table.append(
                [
                    row["#1"], row["Other1"],
                    row["#2"], row["Other2"]
                ]
            )

    header = ["#", "Others"]

    return tabulate(table, header*2, tablefmt="grid")


"""
checks if the iterable is empty

:param iterable: any iterable except strings
:type iterable: list, tuple, or dict
:return: true if empty, otherwise false
:rtype: bool
"""


# I wish this was a built-in data type method ;-;
def is_empty(iterable: list | tuple | dict) -> bool:
    if len(iterable) == 0:
        return True
    else:
        return False


"""
consists of exponentials (.. to the nth power) and roots (nth root of...)

:param base:
    as param for power(): a number which is multiplied by itself
    as param for root(): a number which will be broken down into its roots
:type base: int

:param ratex:
    as param for power(): the exponent of a base
    as param for root(): the index of the root (the nth root)
:type ratex: int
"""


class PowerNRoot:
    # base, ratex is either used for exponentiation or finding roots
    def __init__(self, base: int, ratex: int):
        self.base = base
        self.ratex = ratex

    """
    prompts the user for two numbers. Returns that number for later use.

    :param action: The term for ratex that will depend on the chosen action (exponent or index)
    :type action: str
    """
    def getRational(action: str) -> tuple:
        while True:
            base, act = input("Base: "), input(f"{action}: ")
            try:
                fl_v = float(base), float(act)
            except (ValueError, TypeError):
                print("Invalid input\n")
            else:
                if action == "Index" and int(act) < 0:
                    print("Negative index is unsupported\n")
                else:
                    if fl_v[0].is_integer() and fl_v[1].is_integer():
                        return int(base), int(act)
                    else:
                        return fl_v[0], fl_v[1]

    """
    calculates exponents (b to the nth power)
    
    :return: the evaluated expresion (also follows the negative exponent rule)
    :return type: int if exponent is positive, otherwise str
    """

    def power(self) -> int | str:  # ratex here is used as the exponent
        if self.ratex >= 0:
            return self.base**self.ratex
        else:
            return f"1/{self.base**abs(self.ratex)}"

    """
    calculates the root of a number
    
    :return: the evaluated expresion (everything is in radical form except for perfect roots)
    :return type: int if root is a whole number, otherwise str
    """

    def roots(self) -> str:  # ratex here is used as the index

        if self.base > 0:
            subscript = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
            outer: list[int] = []
            inner: list[int] = []
            factors: dict = factorint(self.base)
            for k, v in factors.items():
                if v >= self.ratex:
                    outer.append(int(k**round(v/self.ratex)))
                    if v % self.ratex != 0:
                        inner.append(k**(v - self.ratex))
                else:
                    inner.append(k**v)

            # if index (ratex) is 2, it will be omitted in the return value
            # this block of code with if and else checks the possible results (based on what this 14 yr old rookie knows)
            if is_empty(inner):
                return Basic(outer).multiply()

            if self.ratex > 2:
                index = str(self.ratex).translate(subscript)

                if is_empty(outer):
                    return f"{index}√{Basic(inner).multiply()}"
                else:
                    return f"{Basic(outer).multiply()} {index}√{Basic(inner).multiply()}"

            else:
                if is_empty(outer):
                    return f"√{Basic(inner).multiply()}"
                else:
                    return f"{Basic(outer).multiply()} √{Basic(inner).multiply()}"
        elif self.base == 0:
            return 0
        else:
            return "Oops!\nUnfortunately, negative roots are not supported yet. (ONGOING WORK)"

    @property
    def ratex(self):
        return self._ratex

    @ratex.setter
    def ratex(self, ratex):
        self._ratex = ratex

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):
        self._base = base


"""
consists of exponentials (.. to the nth power) and roots (nth root of...)

:param num1: the first number to be compared
:type num1: int or float

:param num2: the second number to be compared
:type num2: int or float
"""


class Conditionals:
    def __init__(self, num1: int | float, num2: int | float):
        self.num1 = num1
        self.num2 = num2

    """
    prompts the user for two numbers. Returns that number for later use.
    
    :return: the number prompted
    :return type: tuple[int]
    """
    def getCondNums() -> (tuple[float, float] | tuple[int, int]):
        while True:
            n1, n2 = input("First number: "), input("Second number: ")
            try:
                return float(n1), float(n2)
            except (ValueError, TypeError):
                try:
                    return int(n1), int(n2)
                except (ValueError, TypeError):
                    print("Invalid input\n")

    # compares if num1 is greater than num2. returns boolean expression (True or False)
    def isGreater(self) -> bool:
        return self.num1 > self.num2

    # compares if num1 is less than num2. returns boolean expression (True or False)
    def isLess(self) -> bool:
        return self.num1 < self.num2

    # compares if num1 is greater than or equal to num2. returns boolean expression (True or False)
    def isGreaterEqual(self) -> bool:
        return self.num1 >= self.num2

    # compares if num1 is less than or equal to num2. returns boolean expression (True or False)
    def isLessEqual(self) -> bool:
        return self.num1 <= self.num2

    # compares if num1 is equal to num2. returns boolean expression (True or False)
    def isEqual(self) -> bool:
        return self.num1 == self.num2

    # compares if num1 is not equal to num2. returns boolean expression (True or False)
    def isNotEqual(self) -> bool:
        return self.num1 != self.num2

    @property
    def num1(self):
        return self._num1

    @num1.setter
    def num1(self, num1):
        self._num1 = num1

    @property
    def num2(self):
        return self._num2

    @num2.setter
    def num2(self, num2):
        self._num2 = num2
