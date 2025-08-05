col = int(input())
t = str(input())

matriz = []
soma = []

for linha in range(0, 12):
    dados = []

    for coluna in range(0, 12):
        n = float(input())
        dados.append(n)
    
    matriz.append(dados)

for l in range(0, 12):
    soma.append(matriz[l][col])

if t == 'S':
    print(f'{sum(soma):.1f}')
else:
    print(f'{(sum(soma))/len(soma):.1f}')
