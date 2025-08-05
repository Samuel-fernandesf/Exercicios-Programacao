n = float(input())

print('NOTAS:')

n = n*100
nota100 = n//10000
n = n % 10000
print(f'{nota100:.0f} nota(s) de R$ 100.00')

nota50 = n//5000
n = n % 5000
print(f'{nota50:.0f} nota(s) de R$ 50.00')

nota20 = n//2000
n = n % 2000
print(f'{nota20:.0f} nota(s) de R$ 20.00')

nota10 = n//1000
n = n % 1000
print(f'{nota10:.0f} nota(s) de R$ 10.00')

nota5 = n//500
n = n % 500
print(f'{nota5:.0f} nota(s) de R$ 5.00')

nota2 = n//200
n = n % 200
print(f'{nota2:.0f} nota(s) de R$ 2.00')

print('MOEDAS:')

moeda1 = n//100
n = n % 100
print(f'{moeda1:.0f} moeda(s) de R$ 1.00')

moeda50 = n//50
n = n % 50
print(f'{moeda50:.0f} moeda(s) de R$ 0.50')

moeda25 = n//25
n = n % 25
print(f'{moeda25:.0f} moeda(s) de R$ 0.25')

moeda10 = n//10
n = n % 10
print(f'{moeda10:.0f} moeda(s) de R$ 0.10')

moeda5 = n//5
n = n % 5
print(f'{moeda5:.0f} moeda(s) de R$ 0.05')

moeda001 = n//1
print(f'{moeda001:.0f} moeda(s) de R$ 0.01')







