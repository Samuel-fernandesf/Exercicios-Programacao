n = int(input())
soma = 0

for i in range(0, n):

    x = int(input())
    for i in range(1, x):
        if x % i == 0:
            soma += i
    
    if soma == x:
        print(f'{x} eh perfeito')
    else:
        print(f'{x} nao eh perfeito')

    soma = 0