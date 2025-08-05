n = int(input())

for i in range(0, n):
    jogador1, escolha1, jogador2, escolha2 = map(str, input().split())
    nro1, nro2 = map(int, input().split())
    
    soma = nro1 + nro2
    if soma % 2 == 0:
        if escolha1 == 'PAR':
            print(jogador1)
        else:
            print(jogador2)
    else:
        if escolha1 == 'IMPAR':
            print(jogador1)
        else:
            print(jogador2)