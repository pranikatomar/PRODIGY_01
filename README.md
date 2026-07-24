# PRODIGY_01
# 🌡️ Temperature Conversion Program

**Task-01**

A clean, well-documented command-line Python program that converts a temperature between **Celsius**, **Fahrenheit**, and **Kelvin**.

![Python](https://img.shields.io/badge/Python-3.7%2B-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Dependencies](https://img.shields.io/badge/Dependencies-None-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📋 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Conversion Formulas](#-conversion-formulas)
- [Reference Points](#-reference-points)
- [Sample Output](#-sample-output)
- [Getting Started](#-getting-started)
- [Project Structure](#-project-structure)
- [How It Works](#-how-it-works)
- [Possible Improvements](#-possible-improvements)
- [Author](#-author)
- [License](#-license)

---

## 📖 Overview

This program prompts the user for a temperature value and its original unit (Celsius, Fahrenheit, or Kelvin), then instantly converts it to the other two units and displays a neatly formatted result.

**Example:** entering `25` with unit `C` returns **77.00 F** and **298.15 K**.

## ✨ Features

- 🔄 Converts between all three scales — C → F, C → K, F → C, F → K, K → C, K → F
- 🔤 Accepts both short (`C`) and full-word (`Celsius`) unit input, case-insensitive
- ✅ **Input validation** — rejects non-numeric values and invalid units, and re-prompts instead of crashing
- 🌡️ **Physical validation** — rejects any temperature below absolute zero (-273.15 °C / -459.67 °F / 0 K)
- 🔁 **Loop-based interface** — convert as many temperatures as you like in a single session
- 🚪 Type `exit` at any prompt to quit immediately
- 📦 **Zero dependencies** — pure Python standard library, nothing to install
- 🧹 Clean, modular, fully-commented, PEP8-friendly code with type hints throughout

## 🧮 Conversion Formulas

| From | To | Formula |
|---|---|---|
| Celsius | Fahrenheit | `F = (C × 9/5) + 32` |
| Celsius | Kelvin | `K = C + 273.15` |
| Fahrenheit | Celsius | `C = (F − 32) × 5/9` |
| Fahrenheit | Kelvin | `K = (F − 32) × 5/9 + 273.15` |
| Kelvin | Celsius | `C = K − 273.15` |
| Kelvin | Fahrenheit | `F = (K − 273.15) × 9/5 + 32` |

> 💡 **Fun fact:** −40° is the one point where Celsius and Fahrenheit agree — `-40 °C` really does equal `-40 °F`!

## 📍 Reference Points

| Reference Point | Celsius | Fahrenheit | Kelvin |
|---|---|---|---|
| Absolute Zero | -273.15 | -459.67 | 0.00 |
| Water Freezes | 0.00 | 32.00 | 273.15 |
| Human Body Temp | 37.00 | 98.60 | 310.15 |
| Water Boils | 100.00 | 212.00 | 373.15 |

## 🖥️ Sample Output

![Sample program run](demo/sample_run.png)

<details>
<summary><strong>Click to view plain-text transcript</strong></summary>

```text
$ python3 temperature_converter.py
================================================================
                 TEMPERATURE CONVERSION PROGRAM
              (Celsius  |  Fahrenheit  |  Kelvin)
================================================================

Convert a temperature between Celsius, Fahrenheit and Kelvin.
Type 'exit' at any prompt to quit the program.

Enter the temperature value (or 'exit' to quit): abc
  !! Invalid number. Please enter a numeric value (e.g. 25 or -10.5).

Enter the temperature value (or 'exit' to quit): 25
Enter the original unit (C/F/K): C

----------------------------------------------------------------
 INPUT TEMPERATURE : 25.00 C  (Celsius)
----------------------------------------------------------------
 CONVERTED VALUES  :
   Celsius     :      25.00 C  <-- original input
   Fahrenheit  :      77.00 F
   Kelvin      :     298.15 K
----------------------------------------------------------------

Convert another temperature? (y/n): y
Enter the temperature value (or 'exit' to quit): 98.6
Enter the original unit (C/F/K): F

----------------------------------------------------------------
 INPUT TEMPERATURE : 98.60 F  (Fahrenheit)
----------------------------------------------------------------
 CONVERTED VALUES  :
   Celsius     :      37.00 C
   Fahrenheit  :      98.60 F  <-- original input
   Kelvin      :     310.15 K
----------------------------------------------------------------

Convert another temperature? (y/n): n

Thank you for using the Temperature Conversion Program. Goodbye!
```

*(also available as a plain file at [`demo/sample_run.txt`](demo/sample_run.txt))*

</details>

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or newer — [download here](https://www.python.org/downloads/)
- No external libraries required

### Run it

```bash
git clone https://github.com/<your-username>/Task-01-Temperature-Converter.git
cd Task-01-Temperature-Converter
python3 temperature_converter.py
```

> On Windows, use `python temperature_converter.py` instead of `python3`.

## 📁 Project Structure

```
Task-01-Temperature-Converter/
├── temperature_converter.py   # main program
├── README.md                  # this file
├── LICENSE                    # MIT license
├── .gitignore
└── demo/
    ├── sample_run.png         # sample terminal output (image)
    └── sample_run.txt         # sample terminal output (plain text)
```

## ⚙️ How It Works

1. Displays a banner and short instructions.
2. Prompts for a numeric temperature value (loops until a valid number is entered).
3. Prompts for the original unit — `C`, `F`, or `K` (loops until valid).
4. Rejects any temperature below absolute zero for that unit.
5. Converts the value into the remaining two scales.
6. Displays all three values in a neatly aligned block, marking which one was the original input.
7. Asks whether to convert another temperature, or exits gracefully.

## 🔮 Possible Improvements

- Add a GUI version using Tkinter
- Support batch conversion from a CSV/text file
- Add Rankine and Réaumur scales
- Add automated unit tests with `pytest`

> *(Replace the placeholders above with your own name and GitHub username before submitting.)*

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
