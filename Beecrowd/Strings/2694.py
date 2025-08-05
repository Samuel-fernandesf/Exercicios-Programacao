import re

n = int(input())

for i in range(0, n):
    char = str(input())

    #Busca todos os numeros em uma string
    nros = re.findall(r'\d+', char)
    
    nros = [int(i) for i in nros]
    soma = sum(nros)

    print(soma)