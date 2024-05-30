import math

x = int
quadrado = int
raiz = float

x = int(input("Digite um numero: "))

if x >= 0:
    quadrado = x ** 2
    raiz = math.sqrt(x)
    print(f"Seu numero ao quadrado: {quadrado}")
    print(f"Raiz quadrada do seu numero: {raiz:.2f}")