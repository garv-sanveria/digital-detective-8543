# Mission 5 — Numbers and data

## 1. Task / objective
The objective of Mission 5 was to understand how data is represented numerically in computer systems, perform manual conversions between decimal, binary, and hexadecimal number bases, verify the calculations using Python, build an interactive number converter program, and explore character encoding standards like ASCII and Unicode (UTF-8).

## 2. Work completed
- Calculated seven manual conversions step-by-step between decimal, binary, and hexadecimal formats.
- Verified all manual math in the Python interactive shell using `bin()`, `hex()`, and `int()`.
- Wrote and tested `number_converter.py` using three positive integers (`42`, `128`, and `255`).
- Researched ASCII values for uppercase and lowercase letters and explained why computers need encoding standards.

## 3. Commands / tools used
- Python 3 interactive shell: Verified conversions using `bin()`, `hex()`, and `int()`.
- `python3 mission-05-numbers-data/number_converter.py`: Executed the custom converter script with user inputs.

## 4. My understanding

### Task 5.1 — Convert numbers by hand

| Question | Your working and answer |
| :--- | :--- |
| **Convert decimal 13 to binary** | $13 \div 2 = 6$ rem $1$<br>$6 \div 2 = 3$ rem $0$<br>$3 \div 2 = 1$ rem $1$<br>$1 \div 2 = 0$ rem $1$<br>Reading remainders from bottom to top: **`1101₂`** |
| **Convert decimal 25 to binary** | $25 \div 2 = 12$ rem $1$<br>$12 \div 2 = 6$ rem $0$<br>$6 \div 2 = 3$ rem $0$<br>$3 \div 2 = 1$ rem $1$<br>$1 \div 2 = 0$ rem $1$<br>Reading remainders from bottom to top: **`11001₂`** |
| **Convert binary 1010 to decimal** | $(1 \times 2^3) + (0 \times 2^2) + (1 \times 2^1) + (0 \times 2^0) = 8 + 0 + 2 + 0 =$ **`10`** |
| **Convert binary 1101 to decimal** | $(1 \times 2^3) + (1 \times 2^2) + (0 \times 2^1) + (1 \times 2^0) = 8 + 4 + 0 + 1 =$ **`13`** |
| **Convert hexadecimal A to decimal** | In hex: $0\text{–}9$ represent $0\text{–}9$, and letters $A\text{–}F$ represent $10\text{–}15$. Therefore, $A =$ **`10`** |
| **Convert hexadecimal 1F to decimal** | $(1 \times 16^1) + (F \times 16^0) = (1 \times 16) + (15 \times 1) = 16 + 15 =$ **`31`** |
| **Convert binary 1111 to hexadecimal** | In decimal: $(1 \times 8) + (1 \times 4) + (1 \times 2) + (1 \times 1) = 15$. In hexadecimal, 15 is **`F`** (or **`0xF`**) |

---

### Task 5.2 — Verify using Python
I opened the terminal and tested each expression interactively:

```python
>>> bin(13)
'0b1101'           # Matches manual calculation 1101

>>> bin(25)
'0b11001'          # Matches manual calculation 11001

>>> int('1010', 2)
10                 # Matches manual calculation 10

>>> int('1101', 2)
13                 # Matches manual calculation 13

>>> int('A', 16)
10                 # Matches manual calculation 10

>>> int('1F', 16)
31                 # Matches manual calculation 31

>>> hex(0b1111)
'0xf'              # Matches manual calculation F
```
All outputs matched my hand calculations exactly.

---

### Task 5.3 — Build a small number converter
I wrote `number_converter.py`, which asks the user for a decimal number using `input()`, converts it using `int()`, and then uses Python's built-in `bin()` and `hex()` functions to display the results.

**Test Runs:**

| Test number | Binary output | Hexadecimal output |
| :---: | :--- | :--- |
| **42** | `0b101010` | `0x2a` |
| **128** | `0b10000000` | `0x80` |
| **255** | `0b11111111` | `0xff` |

**Explanation of functions:**
- `bin(x)`: Converts an integer `x` into its binary equivalent string (prefixed with `'0b'`).
- `hex(x)`: Converts an integer `x` into its hexadecimal equivalent string (prefixed with `'0x'`).

---

### Task 5.4 — How is text stored?
- **ASCII decimal codes:**
  - Uppercase `'A'` = `65` (Binary: `01000001`)
  - Lowercase `'a'` = `97` (Binary: `01100001`)
  Notice that adding 32 (flipping the 6th bit) converts an uppercase ASCII letter to its lowercase equivalent.
- **Why computers need an encoding standard:**
  Computers cannot store letters or symbols directly; they can only store binary numbers (voltage states represented as 0s and 1s). An encoding standard establishes a universally recognized mapping between binary integers and visual characters so that any computer system reads and renders the exact same characters without garbled text.
- **Character not in basic ASCII:**
  The emoji 👋 (Unicode code point `U+1F44B`) or the Indian Rupee symbol `₹` (`U+20B9`). Basic ASCII only supports 128 characters (0–127), so modern systems use Unicode (UTF-8) which can encode over a million characters across multiple bytes.

## 5. Difficulties faced
When I first wrote `bin(input("Enter number: "))`, Python threw a `TypeError` because `input()` returns a string instead of an integer.

## 6. How I resolved them
I wrapped `input()` with `int()` so the text entered by the user is properly converted into an integer before being passed to `bin()` and `hex()`.

## 7. Evidence / files
- `mission-05-numbers-data/README.md` (this file)
- `mission-05-numbers-data/number_converter.py`

## 8. Commit details
- Branch: `main`
- Commit message: `Build number converter and practise data representation`
