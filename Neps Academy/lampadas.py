n = int(input())
interruptores = [int(i) for i in input().split()]

lampada1 = 0
lampada2 = 0

for i in interruptores:
    if i == 1:
        lampada1 = 1 if (lampada1 == 0) else 0

    else:
        lampada1 = 1 if (lampada1 == 0) else 0

        lampada2 = 1 if (lampada2 == 0) else 0

print(lampada1)
print(lampada2)