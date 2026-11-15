# Mission 05 - Numbers and data

Status: Completed.

## 1. Task / objective

Show the seven number conversions required by the PDF, check them using Python, complete the decimal number converter, and explain basic text encoding.

## 2. Work completed

Codex prepared the worked calculations and ran the commands in my Mac's zsh environment. The arithmetic steps are shown below. No handwritten notebook evidence is included.

A bit is a binary digit, either 0 or 1. Eight bits make one byte. Decimal uses base 10 and digits 0–9. Binary uses base 2 and digits 0–1. Hexadecimal uses base 16 and digits 0–9 and A–F, where A=10 through F=15.

### Task 5.1 - Convert numbers by hand

For decimal to binary, divide by 2 repeatedly and read the remainders from bottom to top. For binary or hexadecimal to decimal, multiply each digit by its place value and add the results.

| Conversion | Working | Answer |
| --- | --- | --- |
| Decimal 13 to binary | 13 ÷ 2 = 6 remainder 1; 6 ÷ 2 = 3 remainder 0; 3 ÷ 2 = 1 remainder 1; 1 ÷ 2 = 0 remainder 1. Read upwards: 1101. | 1101₂ |
| Decimal 25 to binary | 25 ÷ 2 = 12 remainder 1; 12 ÷ 2 = 6 remainder 0; 6 ÷ 2 = 3 remainder 0; 3 ÷ 2 = 1 remainder 1; 1 ÷ 2 = 0 remainder 1. Read upwards: 11001. | 11001₂ |
| Binary 1010 to decimal | 1 × 2³ + 0 × 2² + 1 × 2¹ + 0 × 2⁰ = 8 + 0 + 2 + 0. | 10₁₀ |
| Binary 1101 to decimal | 1 × 2³ + 1 × 2² + 0 × 2¹ + 1 × 2⁰ = 8 + 4 + 0 + 1. | 13₁₀ |
| Hexadecimal A to decimal | A = 10, so 10 × 16⁰ = 10 × 1. | 10₁₀ |
| Hexadecimal 1F to decimal | F = 15, so 1 × 16¹ + 15 × 16⁰ = 16 + 15. | 31₁₀ |
| Binary 1111 to hexadecimal | One group of four bits: 1 × 8 + 1 × 4 + 1 × 2 + 1 × 1 = 15. The hexadecimal digit for 15 is F. | F₁₆ |

Only the conversions specified in the PDF are included. Octal and extra manual conversions are not required.

### Task 5.2 - Verify using Python

The expressions below were entered into Python's interactive mode using `python3 -q -i`. Python reported version `3.9.6`. The evidence records the input expressions, standard output and interactive prompts separately.

| Expression tested | Actual result | Matches the working? |
| --- | --- | --- |
| `bin(13)` | `'0b1101'` | Yes: 1101₂. |
| `bin(25)` | `'0b11001'` | Yes: 11001₂. |
| `int("1010", 2)` | `10` | Yes. |
| `int("1101", 2)` | `13` | Yes. |
| `int("A", 16)` | `10` | Yes. |
| `int("1F", 16)` | `31` | Yes. |
| `hex(10)` | `'0xa'` | Yes: the reverse check of A₁₆ = 10₁₀. |
| `hex(31)` | `'0x1f'` | Yes: the reverse check of 1F₁₆ = 31₁₀. |
| `hex(int("1111", 2))` | `'0xf'` | Yes: F₁₆. |

`0b` marks a binary string and `0x` marks a hexadecimal string. Python uses lowercase hexadecimal letters here; `f` and `F` have the same value. Quotes in interactive results show that `bin()` and `hex()` return strings. The arithmetic steps above remain separate from these Python checks.

### Task 5.3 - Build a small number converter

The main converter uses functions and while loops. A separate demonstration below uses the built-in `bin()` and `hex()` functions requested by the PDF. Both methods were checked using actual Python results.

[number_converter.py](number_converter.py):

```python
def decimal_to_binary(n):
    if n == 0:
        return "0b0"

    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2

    return "0b" + binary


def decimal_to_hex(n):
    if n == 0:
        return "0x0"

    digits = "0123456789abcdef"
    hexadecimal = ""

    while n > 0:
        remainder = n % 16
        hexadecimal = digits[remainder] + hexadecimal
        n = n // 16

    return "0x" + hexadecimal


number = int(input("Enter a decimal integer: "))

if number < 0:
    positive = -number
    print("Binary: -" + decimal_to_binary(positive))
    print("Hexadecimal: -" + decimal_to_hex(positive))
else:
    print("Binary:", decimal_to_binary(number))
    print("Hexadecimal:", decimal_to_hex(number))
```

Run it from this mission folder with:

```sh
python3 number_converter.py
```

`input()` reads the entry and `int()` turns it into an integer. The two functions then build the result strings:

- Binary: divide by 2 using `//` and take the remainder using `%`.
- Hexadecimal: divide by 16 and use the remainder as an index in `"0123456789abcdef"`. Indices 10–15 give the letters a–f.
- Each remainder is added to the beginning of the string because division finds the rightmost digit first.
- Zero returns `0b0` or `0x0` directly.
- For a negative integer, the main code converts its positive magnitude and prints a minus sign before the result. This is signed notation, not a fixed-width two's-complement encoding.

This version expects an integer. It does not catch invalid input or show a friendly error for text such as `abc` or a decimal fraction such as `2.5`.

The updated code was run with all five inputs below. These are fresh results, not results reused from the previous converter. Every run ended with status `0` and no error output.

| Test input | Binary result line | Hexadecimal result line |
| --- | --- | --- |
| 13 | `Binary: 0b1101` | `Hexadecimal: 0xd` |
| 25 | `Binary: 0b11001` | `Hexadecimal: 0x19` |
| 31 | `Binary: 0b11111` | `Hexadecimal: 0x1f` |
| 0 | `Binary: 0b0` | `Hexadecimal: 0x0` |
| -1 | `Binary: -0b1` | `Hexadecimal: -0x1` |

The first three tests meet the positive-number testing requirement. Zero and -1 check the extra branches in the new code.

Actual stdout for input `13`:

```text
Enter a decimal integer: Binary: 0b1101
Hexadecimal: 0xd
```

The prompt and first result share a line because input was supplied through stdin without echoing it. The transcript records the supplied input separately.

#### Built-in function demonstration

The following code was run in a separate Python interactive session:

```python
print(13, bin(13), hex(13))
print(25, bin(25), hex(25))
print(31, bin(31), hex(31))
```

Actual output:

```text
13 0b1101 0xd
25 0b11001 0x19
31 0b11111 0x1f
```

`bin()` converts an integer to a binary representation string. `hex()` converts an integer to a hexadecimal representation string. The main converter performs the same calculations manually using while loops; it does not call either function. These three built-in results match the converter's results for the same inputs.

### Task 5.4 - How is text stored?

A character encoding gives a consistent way to represent text as bytes, so software can save and read the same characters correctly. Without an agreed encoding, the same stored data could be interpreted as different text.

ASCII is a basic set of 128 character codes. Unicode assigns code points to characters from many writing systems. UTF-8 is an encoding that represents Unicode code points using one to four bytes.

The ASCII decimal code for `A` is **65** and for `a` is **97**. The character `é` is not part of basic ASCII.

These results were checked using `ord()` and `.encode("utf-8")` in the same Python interactive session:

| Character | Decimal code point from `ord()` | Unicode code point | UTF-8 bytes, decimal |
| --- | --- | --- | --- |
| `A` | 65 | U+0041 | `[65]` |
| `a` | 97 | U+0061 | `[97]` |
| `é` | 233 | U+00E9 | `[195, 169]` |

`"é".encode("utf-8").hex(" ")` returned `'c3 a9'`, the same two bytes written in hexadecimal. The code point 233 identifies `é`; it is not the UTF-8 byte sequence. In UTF-8, this character uses the two bytes 195 and 169.

## 3. Commands / tools used

- `python3 --version`: checked the interpreter version.
- `python3 -q -i`: opened interactive mode for the conversion and encoding checks. The `-q` option suppresses the startup banner and `-i` keeps interactive evaluation when stdin is supplied by the helper.
- `python3 number_converter.py`: ran each converter test with recorded input.
- `input()`, `int()`, `str()`, `print()`: read an integer, build result strings and display them.
- Functions, `while` loops, `%`, `//` and string indexing: carry out the converter's repeated-division steps.
- `bin()` and `hex()`: used in Task 5.2 verification and the separate Task 5.3 demonstration, not in the main converter.
- `ord()`, `format()`, `.encode("utf-8")`, `list()` and `.hex(" ")`: checked character codes and encoded bytes.
- Python helper and zsh: ran the commands, checked expected results and captured evidence.
- Swift, PDFKit and Vision: read the exact Mission 5 instructions from PDF pages 7–8 using OCR.
- Git: checked the repository, `main` branch, clean starting state and latest Mission 4 commit.

## 4. My understanding

I learned that the same number can be written in decimal, binary and hexadecimal. To convert a decimal number to binary, I divide it by 2 repeatedly and use the remainders. For hexadecimal, I divide by 16 instead. I used while loops and functions to make a Python converter that follows these steps. I also learned that text is stored using character encodings such as ASCII and UTF-8.

## 5. Difficulties faced

No personal difficulties. The Python verification, five loop-based converter runs and separate built-in demonstration passed without unexpected errors.

## 6. How I resolved them

Not applicable. No unexpected technical errors or personal difficulties needed a resolution.

## 7. Evidence / files

- [Converter source](number_converter.py): the completed program.
- [Python transcript](evidence/python-session.txt): the preserved version check and 17 interactive expression results, followed by five loop-based converter runs and a separate built-in demonstration for 13, 25 and 31, with stdin, stdout, stderr and exit status.
- [This README](README.md): worked calculations, verification tables, converter explanation and encoding notes.

No screenshots were required or created. The arithmetic working is recorded in this README; no handwritten notebook evidence is included.

## 8. Evidence / links

- [Project overview](../README.md).
- [Actual Python evidence](evidence/python-session.txt).
- [Mission 5 commit history](https://github.com/aryangetsreal/digital-detective-8427/commits/main/mission-05-numbers-data/README.md).

## 9. Commit details

- Commit message: `Complete numbers and data mission`.
- Scope: approved Mission 5 files and the root README mission status, progress and converter-description corrections.
- Branch: `main`.
- Commit hash: `f4b238d01886090cf9a6690dbe43a8bb792d0274`.
- Push status: Verified on GitHub `main`; the published commit and files were checked during the final review.
- [Published commit](https://github.com/aryangetsreal/digital-detective-8427/commit/f4b238d01886090cf9a6690dbe43a8bb792d0274).

Verification checks the published files, public visibility, matching local and remote commits, and a clean working tree before reporting success.
