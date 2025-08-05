n = int(input())
hobbit = 0
humano = 0
elfo = 0
anao = 0
mago = 0

for i in range(0, n):
    
    sociedade = str(input())

    especie = sociedade[-1]

    if especie == 'X':
        hobbit +=1
    elif especie == 'H':
        humano +=1
    elif especie == 'E':
        elfo +=1
    elif especie == 'A':
        anao += 1
    else:
        mago += 1

print(f'{hobbit} Hobbit(s)')
print(f'{humano} Humano(s)')
print(f'{elfo} Elfo(s)')
print(f'{anao} Anao(oes)') 
print(f'{mago} Mago(s)')   
    
    