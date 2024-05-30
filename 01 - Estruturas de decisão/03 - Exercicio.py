import math

x: float
quadrado: float
raiz: float

x = float(input("Digite um numero: "))

if x >= 0:
    raiz = math.sqrt(x)
    print(f"Raiz quadrada do seu numero: {raiz:.2f}")

else:
    quadrado = x ** 2
    print(f"Seu numero ao quadrado: {quadrado:.2f}")