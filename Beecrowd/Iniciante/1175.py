vetor = []

for i in range(0, 20):
    nro = int(input())

    vetor.append(nro)

vetor.reverse()

for j in range(0, 20):
    print(f'N[{j}] = {vetor[j]}')
