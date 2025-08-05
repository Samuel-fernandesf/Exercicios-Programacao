t = int(input())

regras = {
    'tesoura': ['papel', 'lagarto'],
    'papel': ['pedra', 'Spock'],
    'pedra': ['lagarto', 'tesoura'],
    'lagarto': ['Spock', 'papel'],
    'Spock': ['tesoura', 'pedra']
}

for i in range(1, t+1):

    sheldon, raj = map(str, input().split())

    if sheldon == raj:
        print(f'Caso #{i}: De novo!')
    else:
        if raj in regras[sheldon]:
            print(f'Caso #{i}: Bazinga!')
        else:
            print(f'Caso #{i}: Raj trapaceou!')