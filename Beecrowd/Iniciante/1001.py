m, n = map(int, input().split())
lista = []

while m > 0 and n > 0:
    if m > n:
        inicio = n
        fim = m
    else:
        inicio = m
        fim = n
    
    for i in range(inicio, fim+1):
        lista.append(i)

    soma = sum(lista)
    print(*lista, f'Sum={soma}')
    lista.clear()

    m, n = map(int, input().split())


