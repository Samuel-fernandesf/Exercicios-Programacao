x, y = map(int, input().split())

nroLinha = 0
for i in range(0, y):
    nroLinha +=1

    if nroLinha == x:
        print(f'{i+1}', end='\n')
        nroLinha = 0
    else:
        print(i+1, end=' ')
