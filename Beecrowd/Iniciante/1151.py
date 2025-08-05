n = int(input())

vetor = [0, 1]

for i in range(2, n):
    vetor.append(vetor[-1] + vetor[-2])

print(*vetor)
