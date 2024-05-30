
import math
x = int
raiz = float

x = int(input("Digite um numero: "))

if x >= 0:
    raiz = math.sqrt(x)
    print(f"RAIZ QUADRADA = {raiz:.2f}")
else:
    print(f"VALOR INVALIDO!")
