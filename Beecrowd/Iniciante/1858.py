n = int(input())
t = [int(i) for i in input().split()]

min = min(t)
posicao = t.index(min) + 1

print(posicao)