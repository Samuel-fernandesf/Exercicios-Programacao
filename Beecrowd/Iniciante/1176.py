n = int(input())

vetor = [0, 1]
for i in range(2, 61):
    vetor.append(vetor[-1] + vetor[-2])

for j in range(0, n):
    nro = int(input())

    print(f'Fib({nro}) = {vetor[nro]}')
