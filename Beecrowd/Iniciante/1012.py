a, b, c = map(float, input('').split())

pi = 3.14159

area_triRetangulo = (a * c)/2
areaCirculo = pi * (c**2)
areaTrapezio = ((a + b) * c)/2
areaQuadrado = b * b
areaRetangulo = a * b

print(f'TRIANGULO: {area_triRetangulo:.3f}')
print(f'CIRCULO: {areaCirculo:.3f}')
print(f'TRAPEZIO: {areaTrapezio:.3f}')
print(f'QUADRADO: {areaQuadrado:.3f}')
print(f'RETANGULO: {areaRetangulo:.3f}')