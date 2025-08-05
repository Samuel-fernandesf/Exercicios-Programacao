# ===========================================
# Guia rápido sobre enumerate() no Python
# ===========================================

# O enumerate() permite iterar sobre listas, tuplas ou strings
# ao mesmo tempo que fornece o índice e o valor do item.

# Exemplo 1: Iterando sobre uma lista normalmente
frutas = ['maçã', 'banana', 'uva']

print('Sem enumerate:')
for i in range(len(frutas)):
    print(f'Índice {i}: {frutas[i]}')

# Exemplo 2: Utilizando enumerate() para obter índice e valor
print('\nCom enumerate:')
for indice, fruta in enumerate(frutas):
    print(f'Índice {indice}: {fruta}')

# Exemplo 3: Definindo um índice inicial diferente
print('\nCom índice iniciando em 1:')
for indice, fruta in enumerate(frutas, start=1):
    print(f'Posição {indice}: {fruta}')

# Exemplo 4: Usando enumerate() para modificar elementos de uma lista
print('\nMultiplicando números com enumerate:')
numeros = [10, 20, 30, 40]
for i, valor in enumerate(numeros):
    numeros[i] = valor * 2
print('Lista modificada:', numeros)

# Exemplo 5: Usando enumerate() para criar um dicionário
print('\nCriando um dicionário com enumerate:')
frutas_dict = {i: fruta for i, fruta in enumerate(frutas)}
print(frutas_dict)
