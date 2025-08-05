jogo = 1
partidasX = 0
partidasY = 0
empate = 0
grenais = 0

while jogo != 2:

    x, y = map(int, input().split())
    grenais += 1

    if(x > y):
        partidasX += 1
    else:
        if(y > x):
            partidasY += 1
        else:
            empate += 1

    print('Novo grenal (1-sim 2-nao)')
    jogo = int(input())

if partidasX > partidasY:
    vencedor = 'Inter venceu mais'
else:
    if partidasY > partidasX:
        vencedor = 'Gremio venceu mais'
    else:
        vencedor = 'Nao houve vencedor'

print(f'{grenais} grenais')
print(f'Inter:{partidasX}')
print(f'Gremio:{partidasY}')
print(f'Empates:{empate}')
print(vencedor)
        
 