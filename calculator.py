"""
FUNCTION/CLASS DESC SUMMARY

Basic[class]: consists of basic operations like: addition, subtraction, multiplication, division
with extra operation: modulus division

    getNums: promps the user for space-separated numbers. Returns the number for later use
    showBasic: displays the available actions for calculation
    add: adds the numbers together
    subtract: subtracts the numbers together
    multiply: multiply the numbers together
    divide: divide the numbers together
    modulus: does the modulus division of numbers

"""

import csv
from tabulate import tabulate
from fractions import Fraction as frac


# NOTE: ANY FRACTION INPUT BY THE USER ARE UNSUPPORTED (yet)

"""
consists of basic operations like: addition, subtraction, multiplication, division
with extra operation: modulus division

:param nums: the numbers that will be used for the operation
:type nums: tuple[int or float] or list[int or float]

NOTE: Unfortunately, this cannot support order of operations. Putting parentheses around numbers are not supported (yet).
"""


class Basic:
    def __init__(self, nums: int | float | tuple[int, float] | list[int, float]) -> None:
        self.nums = nums
        if isinstance(self.nums, list) or isinstance(self.nums, tuple):
            # initial value of total is the first number
            self.total = self.nums[0]
        else:
            pass

    """Gets the number to be used later"""
    @staticmethod
    def getNums() -> tuple[int]:
        while True:
            try:
                nums = input(
                    "Type numbers (put spaces to separate values): ").strip().split(" ")
            except (ValueError, TypeError):
                print("Please separate the values with spaces. (1 space per num)\n")
            else:
                try:
                    fl_l: list[float] = [float(n) for n in nums]
                except (ValueError, TypeError):
                    print("Invalid input.\n")
                else:
                    if [x.is_integer() for x in fl_l] is True:
                        return [int(n) for n in fl_l]
                    else:
                        return fl_l

    """
    displays the available actions for calculation

    :return: a neatly formatted table
    :return type: str
    """

    @staticmethod
    def showBasic():
        table = []

        with open("options/calc_opts.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                table.append([row["#"], row["Calculator"]])

        header = ["#", "Basic Calculator"]

        return tabulate(table, header, tablefmt="grid")

    """
    Adds the numbers together

    :return: the sum of the numbers
    :return type: int or float
    """

    def add(self) -> int | float:
        for num in self.nums[1:]:
            self.total += num
        if isinstance(self.total, float):
            if (self.total).is_integer():
                return int(self.total)
        return float(self.total)

    """
    subtracts the numbers togetehr

    :return: the difference of the numbers
    :return type: int or float
    """

    def subtract(self) -> int | float:
        for num in self.nums[1:]:
            self.total -= num
        if isinstance(self.total, float):
            if (self.total).is_integer():
                return int(self.total)
        return float(self.total)

    """
    multiplies the numbers together

    :return: the product of the numbers
    :return type: int or float
    """

    def multiply(self) -> int | float:
        for num in self.nums[1:]:
            self.total *= num
        if isinstance(self.total, float):
            if (self.total).is_integer():
                return int(self.total)
            return float(self.total)
        return int(self.total)

    """
    divides the numbers together

    :return: the quotient of the numbers in decimal and fractions if does not result in ZeroDivisionError, otherwise outputs 'Undefined or Indeterminate'
    :return type: formatted string (of the int | float)
    """

    def divide(self) -> int | float:
        try:
            for num in self.nums[1:]:
                self.total /= num
        except ZeroDivisionError:
            return "Undefined or Indeterminate"
        else:
            if isinstance(self.total, float):
                if (self.total).is_integer():
                    return int(self.total)
            return float(self.total)

    """
    does the modulus division of numbers
    
    :return: the remainder of the numbers if does not result in ZeroDivisionError, otherwise outputs 'Cannot determine remainder.'
    :return type: int or str
    """

    def modulo(self) -> int | str:
        try:
            for num in self.nums[1:]:
                self.total %= num
        except ZeroDivisionError:
            return "Cannot determine remainder."
        else:
            return self.total

    @property
    def nums(self):
        return self._nums

    @nums.setter
    def nums(self, nums):
        self._nums = nums

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, total):
        self._total: float | int = total
