def fatorial(nro):
    fat = nro

    for i in range(nro-1, 0, -1):
        fat = fat*i

    return(fat)

def main():

    while True:
        n = str(input())
        n = n[::-1]
        cont = 0

        if n == '0':
            break
        
        for i in range(1, len(n)+1, 1):
            cont += int(n[i-1]) * fatorial(i)

        print(cont)

main()