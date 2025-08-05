n = int(input())

for i in range(0, n):
    nome, newtons = map(str, input().split())

    if nome != 'Thor':
        print('N')
    else:
        print('Y')