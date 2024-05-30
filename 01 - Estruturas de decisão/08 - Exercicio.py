import sys

nota1: float
nota2: float
media: float

nota1 = float(input("Digite a primeira nota: "))
if nota1 < 0 or nota1 > 10:
    print(f"NOTA INVALIDA! ")
    sys.exit()
nota2 = float(input("Digite a segunda nota: "))
if nota2 < 0 or nota2 > 10:
    print(f"NOTA INVALIDA! ")
    sys.exit()

media = (nota1 + nota2) / 2

print(f"MEDIA = {media:.2f}")
