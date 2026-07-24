#!/usr/bin/env python3
"""
==============================================================================
 Temperature Conversion Program                                     (Task-01)
==============================================================================
A command-line program that converts a temperature between Celsius,
Fahrenheit, and Kelvin.

Formulas:
    Fahrenheit = (Celsius x 9/5) + 32
    Kelvin     = Celsius + 273.15
    Celsius    = (Fahrenheit - 32) x 5/9

Run:
    python3 temperature_converter.py
==============================================================================
"""

import sys
from typing import Dict

UNIT_NAMES: Dict[str, str] = {"C": "Celsius", "F": "Fahrenheit", "K": "Kelvin"}
ABSOLUTE_ZERO: Dict[str, float] = {"C": -273.15, "F": -459.67, "K": 0.0}
EXIT_COMMANDS = {"exit", "quit", "q"}
BOX_WIDTH = 64


# ---------------------------------------------------------------------------
# Conversion functions
# ---------------------------------------------------------------------------
def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a Celsius temperature to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def celsius_to_kelvin(celsius: float) -> float:
    """Convert a Celsius temperature to Kelvin."""
    return celsius + 273.15


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert a Fahrenheit temperature to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    """Convert a Fahrenheit temperature to Kelvin."""
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))


def kelvin_to_celsius(kelvin: float) -> float:
    """Convert a Kelvin temperature to Celsius."""
    return kelvin - 273.15


def kelvin_to_fahrenheit(kelvin: float) -> float:
    """Convert a Kelvin temperature to Fahrenheit."""
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))


def convert_temperature(value: float, unit: str) -> Dict[str, float]:
    """Return the temperature expressed in Celsius, Fahrenheit and Kelvin."""
    if unit == "C":
        return {"C": value, "F": celsius_to_fahrenheit(value), "K": celsius_to_kelvin(value)}
    if unit == "F":
        return {"C": fahrenheit_to_celsius(value), "F": value, "K": fahrenheit_to_kelvin(value)}
    if unit == "K":
        return {"C": kelvin_to_celsius(value), "F": kelvin_to_fahrenheit(value), "K": value}
    raise ValueError(f"Unsupported unit: {unit}")


# ---------------------------------------------------------------------------
# Input helpers
# ---------------------------------------------------------------------------
def farewell() -> None:
    """Print a goodbye message and exit the program."""
    print("\nThank you for using the Temperature Conversion Program. Goodbye!\n")
    sys.exit(0)


def prompt_temperature_value() -> float:
    """Ask the user for a numeric temperature value; re-prompt until valid."""
    while True:
        raw = input("Enter the temperature value (or 'exit' to quit): ").strip()
        if raw.lower() in EXIT_COMMANDS:
            farewell()
        try:
            return float(raw)
        except ValueError:
            print("  !! Invalid number. Please enter a numeric value (e.g. 25 or -10.5).\n")


def prompt_unit() -> str:
    """Ask the user for the original unit; accepts letters or full names."""
    aliases = {
        "C": "C", "CELSIUS": "C",
        "F": "F", "FAHRENHEIT": "F",
        "K": "K", "KELVIN": "K",
    }
    while True:
        raw = input("Enter the original unit (C/F/K): ").strip().upper()
        if raw.lower() in EXIT_COMMANDS:
            farewell()
        if raw in aliases:
            return aliases[raw]
        print("  !! Invalid unit. Enter C (Celsius), F (Fahrenheit), or K (Kelvin).\n")


def prompt_continue() -> bool:
    """Ask whether the user wants to convert another temperature."""
    while True:
        raw = input("Convert another temperature? (y/n): ").strip().lower()
        if raw in ("y", "yes"):
            return True
        if raw in ("n", "no") or raw in EXIT_COMMANDS:
            return False
        print("  !! Please answer y or n.\n")


# ---------------------------------------------------------------------------
# Display helpers
# ---------------------------------------------------------------------------
def print_banner() -> None:
    """Print the program banner and short instructions."""
    print("=" * BOX_WIDTH)
    print("TEMPERATURE CONVERSION PROGRAM".center(BOX_WIDTH))
    print("(Celsius  |  Fahrenheit  |  Kelvin)".center(BOX_WIDTH))
    print("=" * BOX_WIDTH)
    print()
    print("Convert a temperature between Celsius, Fahrenheit and Kelvin.")
    print("Type 'exit' at any prompt to quit the program.")
    print()


def print_result(value: float, unit: str, results: Dict[str, float]) -> None:
    """Print the converted temperature values in an aligned block."""
    print()
    print("-" * BOX_WIDTH)
    print(f" INPUT TEMPERATURE : {value:.2f} {unit}  ({UNIT_NAMES[unit]})")
    print("-" * BOX_WIDTH)
    print(" CONVERTED VALUES  :")
    for u in ("C", "F", "K"):
        marker = "  <-- original input" if u == unit else ""
        print(f"   {UNIT_NAMES[u]:<12}: {results[u]:>10.2f} {u}{marker}")
    print("-" * BOX_WIDTH)


# ---------------------------------------------------------------------------
# Main program loop
# ---------------------------------------------------------------------------
def main() -> None:
    """Run the temperature conversion program."""
    print_banner()
    while True:
        value = prompt_temperature_value()
        unit = prompt_unit()

        if value < ABSOLUTE_ZERO[unit] - 1e-9:
            print(
                f"\n  !! {value:.2f} {unit} is below absolute zero "
                f"({ABSOLUTE_ZERO[unit]} {unit}). Please enter a valid temperature.\n"
            )
            continue

        results = convert_temperature(value, unit)
        print_result(value, unit, results)
        print()

        if not prompt_continue():
            break

    farewell()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nProgram interrupted. Goodbye!\n")
        sys.exit(0)
