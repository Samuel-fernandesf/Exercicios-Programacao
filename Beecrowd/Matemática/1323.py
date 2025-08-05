# O exercício quer saber quantos quadrados são formados por um quadrado NxN, há duas formas de se pensar:
    # 1. Somar os quadrados de 1 até N, que é o total de quadrados de todos os tamanhos possíveis.
    # 2. Usar a fórmuça de somatória dos quadrados = (N.(N+1).(2.N +1))/6

while True:
    n = int(input())

    if n == 0:
        break

    total = (n*(n+1)*(2*n+1))//6
    print(total)
