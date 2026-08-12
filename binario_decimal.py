def binario_a_decimal(binario: str) -> int:
    decimal = 0

    for digito in binario:
        decimal = decimal * 2 + int(digito)

    return decimal

def decimal_a_binario(decimal: int) -> str:
    if decimal == 0:
        return "0"
    binario = ""

    while decimal > 0:
        residuo = decimal % 2
        binario = str(residuo) + binario
        decimal = decimal // 2

    return binario


if __name__ == "__main__":
    print(binario_a_decimal("1010"))
    print(decimal_a_binario(10))