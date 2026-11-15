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
