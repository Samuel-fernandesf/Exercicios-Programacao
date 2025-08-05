# Devo encontrar o máximo divisor comun MDC, e a partir dele eu sei qual a maior distancia que as estacas podem ficar, depois disso é só dividir cada lado com seu respectivo tamanho pela distancia
def mdc(x, y):
    a = max(x, y)
    b = min(x, y)

    while b != 0:
        a, b = b, a%b
    
    return a

def main():

    while True:
        try:
            x, y = map(int, input().split())
            maiorDistancia = mdc(x, y)

            nroEstacas = ((2*x) + (2*y))/maiorDistancia
            print(f'{nroEstacas:.0f}')

        except EOFError:
            break
main()


