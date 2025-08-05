n = int(input())

while n != 0:

    matriz = []

    for linha in range(0, n):
        dados = []
        for coluna in range(0, n):
            dados.append(linha)

        matriz.append(dados)
    print(matriz)
    n = int(input())
