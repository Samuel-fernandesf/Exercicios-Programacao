o = str(input())

matriz = []
dEsquerda = []
for linha in range(0, 12):
    dados = []

    for coluna in range(0, 12):
        n = float(input())
        dados.append(n)

    matriz.append(dados)

for l in range(0, 12):
    for c in range(0, 12):

        if l > c and (l+c) < (len(matriz) -1):
            dEsquerda.append(matriz[l][c])

if o == 'S':
    print(f'{sum(dEsquerda):.1f}')
else:
    print(f'{(sum(dEsquerda))/len(dEsquerda):.1f}')

