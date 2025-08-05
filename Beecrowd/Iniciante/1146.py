x = int(input())
lista = []

while x != 0:
    for i in range(1, x+1):
        lista.append(i)

    print(*lista)
    lista.clear()
    x = int(input())