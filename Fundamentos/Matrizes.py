"""
Matrizes em Python
------------------

Uma matriz é uma estrutura de dados bidimensional que pode ser representada em Python
por meio de listas aninhadas. Cada elemento da matriz pode ser acessado através de
índices de linha e coluna.
"""

matriz = []
listaPar = []
somaColuna = []

for linha in range(0, 3):
    dados = []

    for coluna in range(0, 3):
        dado = int(input(f'Posicao [{linha},{coluna}]: '))
        dados.append(dado)

    matriz.append(dados)


for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end=' ')

        if matriz[l][c] % 2 == 0:
            listaPar.append(matriz[l][c])
        
        if c == 2:
            somaColuna.append(matriz[l][c])

    print()

print(f'A soma dos pares: {sum(listaPar)}')
print(f'A soma dos valores da 3 coluna: {sum(somaColuna)}')
print(f'O maior valor da 2 linha: {max(matriz[1])}')


'''
MATRIZES E SUAS DIAGONAIS
'''

#DIAGONAL PRINCIPAL

#A DIAGONAL PRINCIPAL SÃO OS ÍNDICES LINHA = COLUNA

#Valores abaixo dessa diagonal:
matriz = []
dAbaixo = []

for linha in range(0, 3):
    dados = []

    for coluna in range(0, 3):
        n = float(input('Diagonal PRINCIPAL abaixo: '))
        dados.append(n)

    matriz.append(dados)

#Para pegar o valor de baixo o for da coluna deve ser igual a linha, para pegar sempre o valor linha-1
#PODE SEGUIR ESSA LOGICA OU FAZER UM IF QUE SE A LINHA FOR MAIOR QUE A COLUNA PEGAR OS VALORES DE BAIXO
for l in range(0, 3):
    for c in range(0, l):
        dAbaixo.append(matriz[l][c])

print(matriz)
print(dAbaixo)

#Valores acima dessa diagonal
matriz = []
dAcima = []

for linha in range(0, 3):
    dados = []

    for coluna in range(0, 3):
        n = float(input('Diagonal PRINCIPAL acima: '))
        dados.append(n)

    matriz.append(dados)

#Nesse caso segue a lógica ao contrário, ao invés de pegar o valor de linha-1, será linha+1
#PODE SEGUIR ESSA LOGICA OU FAZER UM IF QUE SE A LINHA FOR MENOR QUE A COLUNA PEGAR OS VALORES DE CIMA
for l in range(0, 3):
    for c in range(l + 1, 3):
        dAcima.append(matriz[l][c])

print(matriz)
print(dAcima)

#DIAGONAL SECUNDÁRIA

#A DIAGONAL SECUNDÁRIA SÃO OS INDICES LINHA+COLUNA == N-1 SENDO N O NxN

#Valores abaixo dessa diagonal
matriz = []
dAbaixo = []
for linha in range(0, 3):
    dados = []

    for coluna in range(0, 3):
        n = float(input('Diagonal SECUNDÁRIA abaixo: '))
        dados.append(n)

    matriz.append(dados)

for l in range(0, 3):
    for c in range(0, 3):

        #SEGUINDO A FÓRMULA, SE LINHA+COLUNA FOR MAIOR QUE O TAMANHO DA MATRIZ - 1
        if l + c > len(matriz) - 1:
            dAbaixo.append(matriz[l][c])


print(matriz)
print(dAbaixo)

#Valores Acima dessa diagonal
matriz = []
dAcima = []
for linha in range(0, 3):
    dados = []

    for coluna in range(0, 3):
        n = float(input('Diagonal SECUNDÁRIA abaixo: '))
        dados.append(n)

    matriz.append(dados)

for l in range(0, 3):
    for c in range(0, 3):
        #SEGUINDO A FÓRMULA, SE LINHA+COLUNA FOR MENOR QUE O TAMANHO DA MATRIZ - 1
        if l + c < len(matriz) - 1:
            dAcima.append(matriz[l][c])


print(matriz)
print(dAcima)

