n = int(input())
n = n - 3

voltas = (n % 8)

if voltas == 4:
    print(2)
elif voltas == 3: 
    print(1)
elif voltas == 5:
    print(3)