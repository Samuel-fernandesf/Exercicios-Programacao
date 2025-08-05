n = int(input())
cont = 0
for i in range(0, n):

    x = int(input())
    for i in range(1, x+1):
        if x % i == 0:
            cont+=1
    
    if cont == 2:
        print(f'{x} eh primo')
    else:
        print(f'{x} nao eh primo')

    cont = 0
