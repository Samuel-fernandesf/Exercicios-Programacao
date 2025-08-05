n = int(input())
pilha = []
pares = {'(':')', '[':']', '{':'}'}

for i in range(0, n):
    expressao = str(input())

    for i in expressao:

        if i in '([{':
            pilha.append(i)
        
        else:
            if pilha[-1] != pares[i]

