o = str(input())

matriz = []
dAcima = []

for linha in range(0, 12):
    dados = []

    for coluna in range(0, 12):
        n = float(input())
        dados.append(n)

    matriz.append(dados)

for l in range(0, 12):
    for c in range(l + 1, 12):
        dAcima.append(matriz[l][c])

if o == 'S':
    print(f'{sum(dAcima):.1f}')
else:
    print(f'{(sum(dAcima))/len(dAcima):.1f}')




