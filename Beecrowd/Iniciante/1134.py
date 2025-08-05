cod = int(input())
gasolina = 0
alcool = 0
diesel =  0

while cod != 4:

    if cod == 1:
        alcool += 1
    if cod == 2:
        gasolina += 1
    if cod == 3:
        diesel += 1

    cod = int(input())

print('MUITO OBRIGADO')
print(f'Alcool: {alcool}')
print(f'Gasolina: {gasolina}')
print(f'Diesel: {diesel}')
            