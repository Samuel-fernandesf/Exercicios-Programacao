# Importando o módulo re para trabalhar com expressões regulares
import re

# --- Função 1: re.match() ---
# O re.match() tenta casar o padrão no começo da string. Se o padrão não ocorrer no início da string, retorna None.

print("Função 1: re.match()")
# Verificando se a string começa com números
resultado = re.match(r'^\d+', '123abc')
if resultado:
    print(f"Match encontrado: {resultado.group()}")  # Saída: 123
else:
    print("Nenhum match encontrado.")
print()

# --- Função 2: re.search() ---
# O re.search() procura pelo padrão em qualquer lugar na string, ou seja, ele não se limita ao começo da string, como o re.match().

print("Função 2: re.search()")
# Procurando um número em qualquer parte da string
resultado = re.search(r'\d+', 'abc123def')
if resultado:
    print(f"Número encontrado: {resultado.group()}")  # Saída: 123
else:
    print("Nenhum número encontrado.")
print()

# --- Função 3: re.findall() ---
# O re.findall() retorna uma lista de todas as ocorrências do padrão encontrado na string.

print("Função 3: re.findall()")
# Encontrando todos os números em uma string
resultado = re.findall(r'\d+', 'abc123def456ghi789')
print(f"Números encontrados: {resultado}")  # Saída: ['123', '456', '789']
print()

# --- Função 4: re.sub() ---
# O re.sub() substitui todas as ocorrências do padrão por uma outra string fornecida.

print("Função 4: re.sub()")
# Substituindo todos os números por 'X'
resultado = re.sub(r'\d+', 'X', 'abc123def456ghi')
print(f"Texto após substituição: {resultado}")  # Saída: 'abcXdefXghi'
print()

# --- Função 5: re.split() ---
# O re.split() divide a string onde o padrão é encontrado, retornando uma lista de substrings.

print("Função 5: re.split()")
# Dividindo a string onde os números aparecem
resultado = re.split(r'\d+', 'abc123def456ghi')
print(f"Texto dividido: {resultado}")  # Saída: ['abc', 'def', 'ghi']
print()

# --- Função 6: re.subn() ---
# A re.subn() é similar à re.sub(), mas além de retornar a string com as substituições feitas, ela também retorna o número de substituições realizadas.

print("Função 6: re.subn()")
# Substituindo todos os números por 'X' e contando quantas substituições foram feitas
resultado, num_substituicoes = re.subn(r'\d+', 'X', 'abc123def456ghi')
print(f"Texto após substituição: {resultado}")  # Saída: 'abcXdefXghi'
print(f"Quantas substituições? {num_substituicoes}")  # Saída: 2
print()

# --- Função 7: re.finditer() ---
# A re.finditer() retorna um iterador de objetos Match, permitindo iterar sobre todas as ocorrências do padrão.

print("Função 7: re.finditer()")
# Encontrando todos os números e mostrando suas posições
resultado = re.finditer(r'\d+', 'abc123def456ghi789')
for match in resultado:
    print(f"Número encontrado: {match.group()} na posição {match.start()} até {match.end()}")
# Saída: 
# Número encontrado: 123 na posição 3 até 6
# Número encontrado: 456 na posição 9 até 12
# Número encontrado: 789 na posição 15 até 18
print()

# --- Função 8: re.compile() ---
# A re.compile() é usada para compilar uma expressão regular em um objeto, o que pode melhorar a performance se você precisar usar a mesma expressão várias vezes.

print("Função 8: re.compile()")
# Compilando uma expressão regular
padrao = re.compile(r'\d+')
# Usando o padrão compilado para encontrar números
resultado = padrao.findall('abc123def456ghi789')
print(f"Números encontrados com o padrão compilado: {resultado}")  # Saída: ['123', '456', '789']
print()

# --- Função 9: re.fullmatch() ---
# O re.fullmatch() verifica se toda a string corresponde ao padrão.

print("Função 9: re.fullmatch()")
# Verificando se a string é composta apenas por números
resultado = re.fullmatch(r'\d+', '12345')
if resultado:
    print(f"A string corresponde completamente ao padrão: {resultado.group()}")
else:
    print("A string não corresponde completamente ao padrão.")
print()

# --- Função 10: re.split() com múltiplos padrões ---
# A função re.split pode dividir a string usando múltiplos padrões, como uma lista de expressões regulares.

print("Função 10: re.split() com múltiplos padrões")
# Dividindo a string em números ou letras
resultado = re.split(r'\d+|\D+', 'abc123def456ghi789')
print(f"Resultado da divisão: {resultado}")  # Saída: ['', 'abc', '', 'def', '', 'ghi', '']
print()

# --- Função 11: Caracteres Especiais em Expressões Regulares ---
# Os caracteres especiais incluem os metacaracteres que têm um significado especial nas expressões regulares.
# Exemplos de metacaracteres:
# . - Corresponde a qualquer caractere
# ^ - Início da string
# $ - Final da string
# * - Zero ou mais repetições do padrão
# + - Uma ou mais repetições do padrão
# ? - Zero ou uma repetição do padrão
# [] - Corresponde a qualquer caractere dentro dos colchetes
# () - Captura de grupos
# \ - Caractere de escape para metacaracteres

print("Função 11: Caracteres Especiais")
# Usando '.' para encontrar qualquer caractere
resultado = re.search(r'a.b', 'axb')
if resultado:
    print("Padrão 'a.b' encontrado: qualquer caractere entre 'a' e 'b'.")
else:
    print("Padrão não encontrado.")
print()

# --- Função 12: r'raw' strings em expressões regulares ---
# Em Python, a expressão regular pode ser escrita usando 'raw strings', que são strings em que os caracteres de escape (como \n) não têm efeito. Isso é útil para evitar erros de interpretação de caracteres especiais.

print("Função 12: Usando raw strings")
# Expressão regular com barra invertida
resultado = re.match(r'\d+', '12345')
if resultado:
    print(f"Números encontrados: {resultado.group()}")
else:
    print("Nenhum número encontrado.")
print()

#---------------------------------------------------------------------

# Definindo uma string de exemplo para testes
texto = "O número 123 é o primeiro, o número 456 é o segundo, e o 789 é o terceiro."

# Exemplo 1: \d - Corresponde a qualquer dígito (0-9)
# Aqui usamos \d para buscar todos os números (dígitos) na string
numeros = re.findall(r'\d+', texto)  # \d+ encontra um ou mais dígitos consecutivos
print("Números encontrados:", numeros)  # Saída: ['123', '456', '789']

# Exemplo 2: \w - Corresponde a qualquer caractere alfanumérico (letras e números)
# \w também corresponde ao caractere de underline (_)
# Aqui buscamos todas as palavras, incluindo números e letras
palavras = re.findall(r'\w+', texto)  # \w+ encontra uma ou mais letras/números consecutivos
print("Palavras encontradas:", palavras)  # Saída: ['O', 'número', '123', 'é', 'o', 'primeiro', 'o', 'número', '456', 'é', 'o', 'segundo', 'e', 'o', '789', 'é', 'o', 'terceiro']

# Exemplo 3: \s - Corresponde a qualquer espaço em branco (espaço, tabulação, nova linha)
# Aqui vamos usar \s para encontrar os espaços em branco na string
espacos = re.findall(r'\s+', texto)  # \s+ encontra um ou mais espaços consecutivos
print("Espaços encontrados:", espacos)  # Saída: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# Exemplo 4: \b - Corresponde a uma fronteira de palavra (espaço entre palavras ou no início/fim da string)
# Vamos usar \b para encontrar as palavras "número" nas bordas
limites = re.findall(r'\bnúmero\b', texto)  # \b verifica o limite da palavra 'número'
print("Limites encontrados:", limites)  # Saída: ['número', 'número']

# Exemplo 5: ^ - Corresponde ao início de uma linha
# Aqui verificamos se a string começa com a palavra "O"
inicio = re.findall(r'^O', texto)  # ^ verifica se começa com 'O'
print("Começa com 'O'?", bool(inicio))  # Saída: True

# Exemplo 6: $ - Corresponde ao final de uma linha
# Aqui verificamos se a string termina com "terceiro."
fim = re.findall(r'terceiro\.$', texto)  # $ verifica se termina com 'terceiro.'
print("Termina com 'terceiro.'?", bool(fim))  # Saída: True

# Exemplo 7: [] - Corresponde a qualquer caractere dentro dos colchetes
# Vamos procurar todas as ocorrências de letras minúsculas ou dígitos
letras_ou_numeros = re.findall(r'[a-z0-9]+', texto)  # [a-z0-9] encontra letras minúsculas e números
print("Letras ou números encontrados:", letras_ou_numeros)  # Saída: ['número', '123', 'é', 'o', 'primeiro', 'o', 'número', '456', 'é', 'o', 'segundo', 'e', 'o', '789', 'é', 'o', 'terceiro']

# Exemplo 8: () - Grupos de captura
# Usamos parênteses para capturar partes específicas da expressão
# Aqui, capturamos as palavras seguidas de números
grupos = re.findall(r'(\w+)\s(\d+)', texto)  # (\w+) captura palavras, (\d+) captura números
print("Grupos capturados:", grupos)  # Saída: [('número', '123'), ('número', '456'), ('789', 'terceiro')]

# Exemplo 9: ? - Tornando um caractere opcional
# Aqui buscamos por "número" seguido de uma quantidade opcional de espaços
opcional = re.findall(r'número\s?', texto)  # \s? significa que o espaço pode ocorrer 0 ou 1 vez
print("Encontrado 'número' com espaço opcional:", opcional)  # Saída: ['número', 'número']

# Exemplo 10: * - Zero ou mais ocorrências de um padrão
# Aqui procuramos por palavras seguidas de zero ou mais espaços
multiplo = re.findall(r'\w+\s*', texto)  # \s* significa que pode ter zero ou mais espaços após as palavras
print("Palavras seguidas de espaços:", multiplo)  # Saída: ['O ', 'número ', '123 ', 'é ', 'o ', 'primeiro ', 'o ', 'número ', '456 ', 'é ', 'o ', 'segundo ', 'e ', 'o ', '789 ', 'é ', 'o ', 'terceiro.']

# Exemplo 11: + - Um ou mais caracteres de um padrão
# Aqui procuramos por palavras seguidas de um ou mais números
um_ou_mais = re.findall(r'\w+\d+', texto)  # \w+ captura palavras, \d+ captura números
print("Palavras seguidas de números:", um_ou_mais)  # Saída: ['número123', 'número456', '789']

# Exemplo 12: | - Ou lógico (alternância)
# Aqui procuramos por "número" ou "terceiro"
alternancia = re.findall(r'número|terceiro', texto)  # número|terceiro, ou um ou outro
print("Encontrado 'número' ou 'terceiro':", alternancia)  # Saída: ['número', 'número', 'terceiro']
