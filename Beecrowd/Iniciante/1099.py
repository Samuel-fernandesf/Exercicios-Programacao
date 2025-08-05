n = int(input())

lista = []

for i in range(0, n):
    x, y = map(int, input().split())

    if x > y :
        fim = x
        inicio = y
    else:
        fim = y
        inicio = x

    for j in range(inicio+1, fim, 1):
        if j % 2 != 0:
            lista.append(j)

    print(sum(lista))
    lista.clear()