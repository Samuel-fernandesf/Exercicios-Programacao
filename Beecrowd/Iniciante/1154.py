idade = int(input())
lista = []
while idade >= 0:
    lista.append(idade)
    idade = int(input())

media = sum(lista)/len(lista)

print(f'{media:.2f}')

    

