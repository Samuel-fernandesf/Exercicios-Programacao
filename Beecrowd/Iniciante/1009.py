nome = str(input())
salario = float(input())
vendas = float(input())

salario_comissao = salario + (vendas * 0.15)
print(f'TOTAL = R$ {salario_comissao:.2f}')