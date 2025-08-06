codigo1, qtd1, val_uni1 = input().split()
codigo1 = int(codigo1)
qtd1 = int(qtd1)
val_uni1 = float(val_uni1)

codigo2, qtd2, val_uni2 = input().split()
codigo2 = int(codigo2)
qtd2 = int(qtd2)
val_uni2 = float(val_uni2)

total = (qtd1*val_uni1) + (qtd2*val_uni2)
print(f'VALOR A PAGAR: R$ {total:.2f}')

