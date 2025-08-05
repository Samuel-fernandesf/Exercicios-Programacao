n = int(input())
listaX = [int(i) for i in input().split()]

indice0 = []
valores = []

for i in listaX:
    if i == 0:
        indice0.append(listaX.index(i))

n = 0
for i in indice0:
    valores.append(listaX[n:i])
    n = i

print(valores)
    

