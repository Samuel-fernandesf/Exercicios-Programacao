def encaixaOuNao(a, b):

    if a[-len(b):] == b:
        print('encaixa')
    else:
        print('nao encaixa')

def main():

    n = int(input())

    for i in range(0, n):
        a, b = map(str, input().split())

        encaixaOuNao(a, b)

main()