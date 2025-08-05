#len -----------> Retorna o tamanho da lista
l = [1,2,3,4]
len(l)

# in --------> Verifica se um valor aparece na lista
#l = [1,2,3,4]
#3 in l ---> True

# Adiciona vários elementos na lista de uma vez
l = [1,2,3,4]
l.extend([1,2,3])

# Soma todos os valores da lista
l = [1,2,3,4]
sum(l)

#Ordenar a lista
l = [2, 3, 7,1 ,0 ,4]
l.sort()
print(l)

#Para ordenar em ordem decrescente
l.sort(reverse=True)
print(l)

#para copiar uma lista
m = l.copy()

#Para juntar 2 listas utilizar +
l = [1, 2, 3]
m = ['a', 'b', 'c']
p = l + m
print(p)

#Adicionar mais um valor na lista
l = [3, 1, 2, 5, 4]
l.append(7)
#Para limpar, remover todos os dados
l.clear()
#-----------------------------------------------------------

l = [3, 1, 2, 5, 4]

#Informa quantas vezes um valor aparece na lista
l.count(5)

#Indica a posição onde um valor está na lista
l.index(4)

#Inverte os dados da lista
l.reverse()

for i, x in enumerate(m):
    print(f'{i}:{x}')
    
#Printar listas em cada linha
lista = [1,2,3,4]

print(*lista, sep='\n')


