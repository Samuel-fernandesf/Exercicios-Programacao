n1 = int(input())
n2 = int(input())
n3 = int(input())

andar1 = n1*0 + n2*2 + n3*4
andar2 = n1*2 + n2*0 + n3*2
andar3 = n1*4 + n2*2 + n3*0

tempo = min(andar1, andar2, andar3)
print(tempo)