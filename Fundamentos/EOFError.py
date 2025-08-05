# Arquivo: exemplo_eoferror.py

# O EOFError é uma exceção que ocorre quando o Python tenta ler mais dados do que o arquivo ou a entrada de dados tem disponível.
# Isso pode acontecer ao tentar ler um arquivo ou ao tentar ler a entrada do usuário quando não há mais dados a serem lidos.

# Exemplo 1: EOFError com a função input()
# O EOFError ocorre se o usuário envia um sinal de fim de arquivo (EOF), que pode ser feito pressionando Ctrl+D (Linux/Mac) ou Ctrl+Z (Windows).

try:
    while True:
        valor = input("Digite algo (ou Ctrl+D/Ctrl+Z para sair): ")
        print(f"Você digitou: {valor}")
except EOFError:  # Quando o usuário envia o sinal de EOF
    print("Fim de arquivo (EOF) detectado! Programa encerrado.")

# Exemplo 2: EOFError ao tentar ler de um arquivo após o final
# O EOFError pode acontecer se tentarmos ler além do fim de um arquivo. 
# Embora a maioria das funções de leitura do Python não gere um EOFError diretamente (elas retornam uma string vazia ou uma estrutura vazia),
# se tentarmos um comportamento inesperado, podemos forçar a exceção.

# Neste exemplo, usaremos uma leitura simples de arquivo para simular a exceção:

# Criando um arquivo para o exemplo
with open("exemplo.txt", "w") as f:
    f.write("Linha 1\nLinha 2\nLinha 3")

# Abrindo o arquivo para leitura e tentando forçar um erro de EOF
try:
    with open("exemplo.txt", "r") as f:
        for line in f:
            print(line.strip())  # Imprime cada linha do arquivo
        # Tentando forçar a leitura após o final do arquivo
        line = f.read()  # Não há mais conteúdo, pode gerar EOFError se for mal usado
        print(line)  # Não será executado
except EOFError:
    print("EOFError detectado! Tentativa de ler além do final do arquivo.")

# Exemplo 3: EOFError ao tentar ler de um arquivo binário
# EOFError pode ocorrer em arquivos binários se o código tentar ler além do conteúdo do arquivo.

try:
    with open("exemplo.txt", "rb") as f:
        while True:
            data = f.read(10)  # Lê 10 bytes de cada vez
            if not data:
                break  # Final do arquivo
            print(data)
        # Tentando forçar a leitura após o final do arquivo
        extra_data = f.read(10)  # Tentativa de ler após o fim do arquivo
except EOFError:
    print("EOFError detectado em leitura binária! Tentativa de ler além do final do arquivo.")

# Exemplo 4: Como evitar o EOFError usando tratamento adequado
# Em vez de deixar o programa quebrar ao tentar ler além do arquivo ou ao receber um EOF, podemos usar o 'try-except' para capturar a exceção.
# Quando estamos lidando com entrada do usuário ou arquivos, sempre tenha em mente que pode ocorrer o EOF.

# Aqui, vamos tratar corretamente o EOFError com o 'try-except' para garantir que o programa funcione sem problemas.

def ler_entrada():
    try:
        while True:
            valor = input("Digite algo (ou Ctrl+D/Ctrl+Z para sair): ")
            print(f"Você digitou: {valor}")
    except EOFError:  # Quando o sinal de EOF for enviado pelo usuário
        print("Fim de arquivo (EOF) detectado! Programa encerrado corretamente.")

# Chama a função para testar
ler_entrada()

# Resumo
# O EOFError ocorre em situações como:
# - Tentar ler além do final de um arquivo (seja texto ou binário).
# - Quando a entrada do usuário atinge o sinal EOF (Ctrl+D/Ctrl+Z).
# - Tentar ler mais dados do que existem em um fluxo de entrada.
#
# A melhor forma de lidar com o EOFError é usar blocos de tratamento try-except para capturar e agir conforme necessário, como 
# exibir uma mensagem amigável ou realizar ações de limpeza (fechar arquivos, encerrar loops, etc.).
#
# Caso você esteja trabalhando com arquivos ou entrada de dados, sempre verifique a existência de dados antes de tentar ler.
