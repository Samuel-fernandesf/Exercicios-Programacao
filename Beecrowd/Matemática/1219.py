import math

def areasFlores(a, b, c):

    s = (a+b+c)/2 # Semiperimetro
    areaTriangulo = math.sqrt(s*(s-a)*(s-b)*(s-c)) # Formula de Heron

    raioMenor = areaTriangulo/s 
    areaCirculoMenor = math.pi * (raioMenor**2)

    raioMaior = (a*b*c)/(4*areaTriangulo) 
    areaCirculoMaior = (math.pi * (raioMaior**2))

    girassois = areaCirculoMaior - areaTriangulo
    violetas = areaTriangulo - areaCirculoMenor
    rosas = areaCirculoMenor

    return(girassois, violetas, rosas)

def main():

    while True:
        try:
            a, b, c = map(int, input().split())

            girassois, violetas, rosas = areasFlores(a, b, c)
            print(f'{girassois:.4f} {violetas:.4f} {rosas:.4f}')

        except EOFError:
            break

main()