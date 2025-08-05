n, amizade = map(int, input().split())
runas = {}
totalAmizade = []

for i in range(0, n):
    letra, poder = input().split()

    letra = str(letra)
    poder = int(poder)

    runas[letra] = poder

x = int(input())
runasRecitadas = str(input())

#.replace() substitui partes de uma string por outra
runasRecitadas = runasRecitadas.replace(' ', '') # irá tirar todos os espaços do str 

for i in range(0, x):
    if runasRecitadas[i] in runas:
        totalAmizade.append(runas[runasRecitadas[i]])

totalAmizade = sum(totalAmizade)
print(totalAmizade)

if totalAmizade >= amizade:
    print('You shall pass!')
else:
    print('My precioooous')




