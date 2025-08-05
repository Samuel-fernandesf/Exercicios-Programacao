nro = int(input())

if nro == 0 or nro == 1:
    fib = 1
else:
    fib = (nro -1) + (nro - 2)

print(fib)