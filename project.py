
"""
KALKOULATOR

it's calculator + extra stuff :)
"""

import sys
from time import sleep
from calculator import *
from converters import *
from others import *
import os


def main():
    kalkoulator = {"1": "Calculators",
                   "2": "Converters", "3": "Others", "4": "Exit"}

    while True:
        for i in kalkoulator:
            print(f"{i}: {kalkoulator[i]}")

        main_choose = input(
            "Choose from the list (type its corresponding index): ")

        match main_choose:
            case "1":
                while True:
                    print(f"\n{Basic.showBasic()}\n")
                    prompt = input("Select action: ").strip()
                    act = choose_calc(prompt)
                    if act == hex(0):
                        print("Invalid option.\n")
                    else:
                        print(f"\n{act}")
                        break
                break
            case "2":
                while True:
                    print(f"\n{Unit.showConv()}\n")
                    prompt = input("Select action: ").strip()
                    act = choose_conv(prompt)
                    if act == hex(0):
                        print("Invalid option.\n")
                    else:
                        print(f"\n{act}")
                        break
                break
            case "3":
                while True:
                    print(f"\n{showOth()}\n")
                    prompt = input("Select action: ").strip()
                    act = choose_oth(prompt)
                    if act == hex(0):
                        print("Invalid option.\n")
                    else:
                        print(f"\n{act}")
                        break
                break
            case "4":
                os.system('cls' if os.name == 'nt' else 'clear')
                sys.exit("\nPROGRAM CLOSED\n")
            case _:
                print("Invalid option.\n")
    sleep(1)
    repeat()


"""
shows options the program can do

:param choice: determines the action to be done
:type choice: str
:return: an int/float or str of the result
"""


def choose_calc(choice: str) -> int | float | str:
    if choice in [str(x) for x in range(1, 6)]:
        print()
        nums: tuple[int] = Basic.getNums()
        if isinstance(nums, int) or isinstance(nums, float):
            return nums
        else:
            basic: Basic = Basic(nums)
            match choice:
                case "1":
                    return basic.add()
                case "2":
                    return basic.subtract()
                case "3":
                    return basic.multiply()
                case "4":
                    return basic.divide()
                case "5":
                    return basic.modulo()
    else:
        return hex(0)


"""
shows options the program can do

:param choice: determines the action to be done
:type choice: str
:return: an int/float or str of the result
"""


def choose_conv(choice: str) -> int | float | str:
    if choice in [str(x) for x in range(1, 5)]:
        print()
        num: int = Unit.getUnit()
        match choice:
            case "1":
                return Length(num).engine()
            case "2":
                return Area(num).engine()
            case "3":
                return Volume(num).engine()
            case "4":
                return Temperature(num).engine()
    else:
        return hex(0)


"""
shows options the program can do

:param choice: determines the action to be done
:type choice: str
:return: an int, str, or bool of the result
"""


def choose_oth(choice: str) -> int | str | bool:
    if choice in [str(x) for x in range(1, 9)]:
        print("")
        match choice:
            case "1":
                b, r = PowerNRoot.getRational("Exponent")
                other = PowerNRoot(b, r)
                return other.power()
            case "2":
                b, r = PowerNRoot.getRational("Index")
                other = PowerNRoot(b, r)
                return other.roots()
            case "3" | "4" | "5" | "6" | "7" | "8":
                n1, n2 = Conditionals.getCondNums()
                cond = Conditionals(n1, n2)
                if choice == "3":
                    return cond.isGreater()
                elif choice == "4":
                    return cond.isLess()
                elif choice == "5":
                    return cond.isGreaterEqual()
                elif choice == "6":
                    return cond.isLessEqual()
                elif choice == "7":
                    return cond.isEqual()
                else:
                    return cond.isNotEqual()
    else:
        return hex(0)


def repeat():
    prompt_rep = input("\n\nRelaunch? (y/n): ")
    if prompt_rep == "y":
        os.system('cls' if os.name == 'nt' else 'clear')
        return main()
    elif prompt_rep == "n":
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit("\nPROGRAM CLOSED\n")
    else:
        print("\nINVALID INPUT...")
        sleep(0.5)
        sys.exit("\nPROGRAM CLOSED\n")


if __name__ == "__main__":
    main()
