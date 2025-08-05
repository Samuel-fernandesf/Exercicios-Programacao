while True:
    n = str(input().strip())

    if n.startswith('0x') or len(n) > 2 and n[1] == 'x':

        hex_to_decimal = int(n, 16)
        print(hex_to_decimal)
    else:

        if int(n) < 0:
            break

        decimal_to_hex = int(n)
        print(f'0x{decimal_to_hex:X}') #x converte str em hexadecimal, maiúsculo, se fosse x seria minúsculo.

