n = int(input())

hora = n//3600
n = n % 3600

minuto = n//60
n = n % 60

segundo = n % 60

print(f'{hora}:{minuto}:{segundo}')