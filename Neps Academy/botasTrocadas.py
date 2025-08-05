n = int(input())
botas = []

for i in range(0, n):
    m, l = map(str, input().split())

    bota = {m:l}
    botas.append(bota)

semDuplicata = set(botas)
semDuplicata = list(semDuplicata)

pares = 0
for i in range(0, len(semDuplicata)):
    if botas.count(semDuplicata[i]) // 2:
        pares += 1

print(pares)