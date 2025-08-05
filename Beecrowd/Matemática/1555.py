def fMath(x, y):

    equacoes = {'Rafael':(3*x)**2 + y**2,
                'Beto': 2*(x**2) + (5*y)**2,
                'Carlos':-100*x + y**3
    } 
    chave_maior_valor = max(equacoes, key=equacoes.get)
    
    print(f'{chave_maior_valor} ganhou')

def main():
    n = int(input())

    for i in range(0, n):
        x, y = map(int, input().split())

        fMath(x, y)
main()