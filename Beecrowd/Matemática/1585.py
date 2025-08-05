# Devo descobrir a área da pipa, que é um losango ou seja A = d * D / 2

n = int(input())

for i in range(0, n):

    x, y = map(int, input().split())
    area = (x*y)//2

    print(f'{area} cm2')