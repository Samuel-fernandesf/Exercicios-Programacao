x = int(input())
y = 0

cont = 1
while y <= x:
    y = int(input())


for i in range(x+1, y+1):
    if x <= y:
        x += i
        cont +=1

print(cont)
