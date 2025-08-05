par = []
impar = []

for i in range(0, 15):
    nro = int(input())

    if nro % 2 == 0:
        par.append(nro)
    else:
        impar.append(nro)
    

    if len(par) >= 5:
        for j in range(0, 5):
            print(f'par[{j}] = {par[j]}')
        par.clear()

    if len(impar) >= 5:
        for k in range(0, 5):
            print(f'impar[{k}] = {impar[k]}')
        impar.clear()

if len(impar) < 5:
    for l in range(0, len(impar)):
         print(f'impar[{l}] = {impar[l]}')

if len(par) < 5:
    for m in range(0, len(par)):
         print(f'par[{m}] = {par[m]}')

#ENUMERATE

# par = []
# impar = []

# for _ in range(15):
#     nro = int(input())

#     # Adiciona o número na lista correspondente
#     (par if nro % 2 == 0 else impar).append(nro)

#     # Se atingir 5 elementos, imprime e esvazia a lista
#     if len(par) == 5:
#         for i, v in enumerate(par):
#             print(f'par[{i}] = {v}')
#         par.clear()

#     if len(impar) == 5:
#         for i, v in enumerate(impar):
#             print(f'impar[{i}] = {v}')
#         impar.clear()

# # Imprime os restantes
# for i, v in enumerate(impar):
#     print(f'impar[{i}] = {v}')
# for i, v in enumerate(par):
#     print(f'par[{i}] = {v}')
