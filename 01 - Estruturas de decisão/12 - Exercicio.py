import math

x: int

x = int(input("Digite um numero: "))

if x >= 0:
    logaritmo = math.log(x)
    print(f"Logaritmo do seu numero: {logaritmo:.2f}")

else:
    print(f"NUMERO INVALIDO! ")