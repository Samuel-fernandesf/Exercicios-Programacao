x = int(input())
y = int(input())

lista = []
if x < y:
    inicio = x
    fim = y
else:
    inicio = y
    fim = x

for i in range(inicio, fim+1):

    if i % 13 != 0:
        lista.append(i)

soma = sum(lista)
print(soma)

