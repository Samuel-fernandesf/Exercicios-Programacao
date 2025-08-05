h, p, f, d = map(int, input().split())
posicao = f

for i in range(0, 16):
    posicao = (posicao + d) % 16 # O 16 é o numero de quadrados em uma volta
  
    if p == posicao:
        print('N')
        break
        
    if h == posicao:
        print('S')
        break

        

