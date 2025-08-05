x = [int(x) for x in input().split()]

a = x[0]
x.remove(a)
n = x[len(x)-1]

soma = []
for i in range(0, n):
    soma.append(a+i)

print(sum(soma))
