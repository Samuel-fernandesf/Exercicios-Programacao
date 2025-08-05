a, b, c = map(int, input().split())

maiorAB = (a + b + abs(a-b))/2
maiorC = (maiorAB + c + abs(maiorAB - c))/2

print(f'{maiorC:.0f} eh o maior')