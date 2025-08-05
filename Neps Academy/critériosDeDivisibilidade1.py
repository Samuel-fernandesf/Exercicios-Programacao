nro = str(input())

print('S' if nro[-1] in '02468' else 'N')

soma = sum(int(i) for i in nro)
print('S' if soma % 3 == 0 else 'N')

print('S' if nro[-1] in '05' else 'N')

