vetor = []

for i in range(0, 10):
    x = int(input())

    if x <= 0:
       x = 1

    vetor.append(x)
    print(f'X[{i}] = {x}')

