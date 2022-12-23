# **Kalkoulator**

## Description:

This project is a calculator in an interactive shell. The user can choose between operations the calculator can perform such as basic arithmetic, modulo and many more. It also has a converter that can (currently) convert between Length, Area, Volume and Temperature. <br> <br>

And fun fact: The project's name came from a friend who said "**kalkoulator** is calculator but with strong indian accent"

## Features
- arithmetic operations (addition, subtraction, multiplication, division)
- modulo operation
- conversion (Length, Area, Volume, Temperature)
- Exponentation (xⁿ)
- Roots (√x)
- Conditionals (>, <, ≥, ≤, =, ≠)


## Installing Libraries

A list of libraries used is stored in requirements.txt
<br> <br>
To install the libraries, do: <br>
```pip install -r requirements.txt```

NOTE: There may be changes in the project that will use new libraries.


## Project Structure
```
Kalkoulator/
├── options/
│   ├── calc_opts.csv
│   ├── conv_opts.csv
│   └── oth_opts.csv
├── calculator.py
├── converters.py
├── others.py
├── project.py
├── README.md
├── requirements.txt
├── test_project.py
├── test_calculator.py
├── test_converters.py
└── test_others.py
```

**<ins>A brief description of each file is provided below: </ins>** <br>
<br>
**project.py** : the main file connected with other files for the app's functionality <br>
**calculator.py** : consists of basic arithmetic + modulo <br>
**converters.py** : contains unit conversions (Length, Area, Volume and Temperature) <br>
**others.py** : contains uncategorized operations (Exponentation, nth root, & Conditionals) <br>
**test_project.py** : unit tests for project.py <br>
**test_calculator.py** : unit test for calculator.py <br>
**test_converters.py** : unit test for converters.py <br>
**test_others.py** : unit test for others.py <br>
**requirements.txt** : contains non-built-in libraries used <br>
**README.md** : this file <br>
**options/** <br>
&nbsp;&nbsp;&nbsp;&nbsp; **calc_opts.csv** : csv of options for calculator.py <br>
&nbsp;&nbsp;&nbsp;&nbsp; **conv_opts.csv** : csv of options for converters.py <br> <br>
&nbsp;&nbsp;&nbsp;&nbsp; **oth_opts.csv** : csv of options for others.py <br>


<hr>
**Note**: The program is relatively new and fresh (and so is my knowledge in math). Some may encounter unsupported features, or even a bug. I will try my best to continuously develop this app. <br> <br>

For more information about the project, a wiki will be worked on soon. ( If I'm on the mood :] )
