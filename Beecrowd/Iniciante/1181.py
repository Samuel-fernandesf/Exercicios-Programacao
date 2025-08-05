l = int(input())
t = str(input())

matriz = []
for linha in range(0, 12):
    dados = []
    for coluna in range(0, 12):
        nro = float(input())
        dados.append(nro)

    matriz.append(dados)

if t == 'S':
    print(f'{sum(matriz[l]):.1f}')
else:
    print(f'{(sum(matriz[l]))/12:.1f}')
