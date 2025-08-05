import math

def descobrirH(a, b, c):

    rad = a * (3.141592654/180)
    h = (math.tan(rad) * b) + c

    return h

def main():

    while True:
        try:
            a, b, c = map(float, input().split())

            qtd_cordao = descobrirH(a, b, c) * 5
            print(f'{qtd_cordao:.2f}')
        except EOFError:
            break
main()