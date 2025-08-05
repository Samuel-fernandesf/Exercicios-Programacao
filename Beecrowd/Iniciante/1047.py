h1, m1, h2, m2 = map(int, input().split())

inicio = h1*60 + m1
fim = h2*60 + m2

if inicio >= fim:
    fim = fim + 24*60

tempo = fim - inicio

tempoH = tempo//60
tempoM = tempo % 60

print(f'O JOGO DUROU {tempoH} HORA(S) E {tempoM} MINUTO(S)')
