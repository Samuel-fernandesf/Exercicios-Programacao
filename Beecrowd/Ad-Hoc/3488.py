#MÉTODO QUE REALIZEI
#  def boolIsPowerOfTwo(n):
#     while n > 1:
#         n //= 2

#     return 'true' if n == 1 else 'false'

#MÉTODO UTILIZANDO FUNÇÃO LOGARÍTMA
# import math

# def is_power_of_two_log(n):
#     if n <= 0:
#         return "false"
#     log_val = math.log2(n)
#     return "true" if log_val.is_integer() else "false"



#MÉTODO SOLICITADO, UTILIZANDO BINÁRIO
# Função para verificar se um número é potência de 2 usando operação bit a bit.
# Em binário, uma potência de 2 tem exatamente um único bit 1 ligado (ex: 1, 10, 100, 1000...).
# Ao fazer n & (n - 1), removemos o bit 1 mais baixo de n.
# Se o resultado for 0, significa que só havia um bit 1 em n, confirmando que é potência de 2.
# Exemplo: 8 (1000) & 7 (0111) = 0 (0000) → é potência de 2.
def boolIsPowerOfTwo(n):
    return "true" if n > 0 and (n & (n - 1)) == 0 else "false"


 
def main():
    n = int(input())

    print(boolIsPowerOfTwo(n))

main()


