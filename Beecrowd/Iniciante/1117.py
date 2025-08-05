lista = []

while(len(lista) < 2):

    n = float(input())

    if n >= 0 and n <= 10:
        lista.append(n)
    else:
        print('nota invalida')

soma = sum(lista)

print(f'media = {soma/2}')
