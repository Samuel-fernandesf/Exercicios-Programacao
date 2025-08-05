x = int(input())
y = int(input())

lista = []
if x < y:
    inicio = x
    fim = y
else:
    inicio = y
    fim = x

for i in range(inicio+1, fim):

    if i % 5 == 2 or i % 5 == 3:
        print(i)