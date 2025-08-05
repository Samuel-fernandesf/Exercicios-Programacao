n = int(input())
total = 0

for i in range(0, n):
    acessos = int(input())
    total+= acessos

    if(total >= 1000000):
        print(i+1)
        break