nro = str(input())
lista = [int(i) for i in nro]
par = 0
impar = 0

for indice, valor in enumerate(lista):
    if (indice+1) % 2 == 0:
        par += valor
    else:
        impar += valor

res = impar - par

print('S' if res % 11 == 0 else 'N')