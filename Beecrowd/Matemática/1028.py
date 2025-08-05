n = int(input())

# Minha lógica - dividir todos os numeros de 0 ao maior da lista, se em ambos os valores da lista forem divisíveis eu armazeno em cont, porém esse cont é atualizado até o final, para se pegar o último divisor comum. Máximo divisor comum (MDC)
# n = int(input())
#Dá timelimit, pelo fato da demora no looping

for i in range(0, n):
    fig = [int(i) for i in input().split()]

    maior = max(fig)
    cont = 1

    for j in range(1, maior+1):

        if fig[0]%j == 0 and fig[1]%j == 0:
            cont = j

    print(cont)

# Lógica simples e rápida - Algoritmo de Euclides
# Divida os dois números por exemplo 12/8 caso dê 0, o maior divisor é 8, senão, divida o menor número no caso 8 pelo seu resto, no caso seria 8/4 nesse caso dá 0, o MDC(12,8) é 4.

def mdc(f1, f2):
    a = max(f1, f2)
    b = min(f1, f2)

    while b != 0:
        a, b = b, a % b

    return a

def main():
    n = int(input())

    for i in range(0, n):
        f1, f2 = map(int, input().split())

        print(mdc(f1, f2))

main()