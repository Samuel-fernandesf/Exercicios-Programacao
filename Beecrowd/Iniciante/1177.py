t = int(input())

vetor = []

for i in range(0, 1000):
    for j in range(0, t):
        vetor.append(j)
        
    print(f'N[{i}] = {vetor[i]}')
    
    