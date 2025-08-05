nro = str(input())

dois_ultimos = nro[-2:]
dois_ultimos = int(dois_ultimos)
print('S' if dois_ultimos % 4 == 0 else 'N' )

soma = sum(int(i) for i in nro)
print('S' if soma % 9 == 0 else 'N')

print('S' if (nro[-2:]) in ['00', '25', '50', '75'] else 'N' )