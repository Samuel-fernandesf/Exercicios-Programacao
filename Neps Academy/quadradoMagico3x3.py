lista = []

for i in range(0, 9):
    x = int(input())
    lista.append(x)

if sum(lista[0:2]) == sum(lista[3:5]) ==  sum(lista[6:8]):
    print('OLA')


diagonais = lista[0] + lista[len(lista)-1] + lista[(len(lista)-1)//2]
