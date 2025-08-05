o = str(input())

matriz = []
dAbaixo = []

for linha in range(0, 12):
    dados = []

    for coluna in range(0, 12):
        n = float(input())
        dados.append(n)

    matriz.append(dados)

for l in range(0, 12):
    for c in range(0, l):
        dAbaixo.append(matriz[l][c])

if o == 'S':
    print(f'{sum(dAbaixo):.1f}')
else:
    print(f'{(sum(dAbaixo))/len(dAbaixo):.1f}')


