altura: float
sexo: str
ideal: float

altura = float(input("Digite a sua altura: "))
sexo = input("Digite seu sexo(F/M): ")

if sexo == 'F':
    ideal = (62.1 * altura) - 44.7
if sexo == 'M':
    ideal = (72.7 * altura) - 58

print(f"Seu peso ideal: {ideal:.2f}KG")