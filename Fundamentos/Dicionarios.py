# Criar um dicionário
d = {'nome': 'João', 'idade': 25, 'cidade': 'São Paulo'}
 
# Acessar um valor no dicionário
print(d['nome'])  # João

# Verificar se uma chave está no dicionário
print('idade' in d)  # True

# Adicionar um novo par chave-valor
d['profissao'] = 'Engenheiro'

# Atualizar um valor
d['idade'] = 26

# Remover um item do dicionário
del d['cidade']

# Obter todas as chaves do dicionário
print(d.keys())

# Obter todos os valores do dicionário
print(d.values())

# Obter todos os itens (chave, valor) do dicionário
print(d.items())

# Copiar um dicionário
novo_d = d.copy()

# Limpar o dicionário
d.clear()

# Criar um dicionário com chaves pré-definidas e um valor padrão
chaves = ['a', 'b', 'c']
d_padrao = dict.fromkeys(chaves, 0)

# Usar o método get para acessar valores de forma segura
print(d.get('nome', 'Não encontrado'))

# Remover e retornar um item do dicionário
profissao = d.pop('profissao', 'Não encontrado')

# Iterar sobre um dicionário
for chave, valor in d.items():
    print(f'{chave}: {valor}')
