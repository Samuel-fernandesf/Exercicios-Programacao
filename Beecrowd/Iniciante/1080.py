lista = []

for i in range(0, 100):
    n = int(input())

    lista.append(n)

maior = max(lista)
posicao = lista.index(maior) + 1

print(maior)
print(posicao)


    