#!/usr/bin/env python3
"""
Mission 05 - Number Converter
A simple terminal tool to convert positive decimal integers into
binary and hexadecimal representations.
"""


def convert_number():
    print("=== Number Base Converter ===")
    user_input = input("Enter a positive decimal integer: ").strip()

    try:
        decimal_val = int(user_input)
        if decimal_val < 0:
            print("Please enter a positive integer.")
            return

        binary_rep = bin(decimal_val)[2:]
        hex_rep = hex(decimal_val)[2:].upper()

        print(f"\nResults for decimal: {decimal_val}")
        print(f"  Binary:      {binary_rep} (with prefix: {bin(decimal_val)})")
        print(f"  Hexadecimal: {hex_rep} (with prefix: {hex(decimal_val)})")

    except ValueError:
        print("Invalid input! Please enter a valid decimal whole number.")


def main():
    convert_number()


if __name__ == "__main__":
    main()
