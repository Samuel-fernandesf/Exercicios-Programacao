x = float(input())
vetor = []

for i in range(0, 100):
    vetor.append(x)
    print(f'N[{i}] = {x:.4f}')
    x /= 2
