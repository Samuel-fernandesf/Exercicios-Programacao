n = int(input())
x = [int(i) for i in input().split()]

min = min(x)
posicao = x.index(min)

print(f'Menor valor: {min}')
print(f'Posicao: {posicao}')

