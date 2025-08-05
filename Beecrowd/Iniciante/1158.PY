n = int(input())
soma = 0
for i in range(0, n):
    x, y = map(int, input().split())

    if x % 2 == 0:
        x +=1
    
    for j in range(0, y):
        if x % 2 != 0:
            soma += x
        x+=2

    print(soma)
    soma = 0