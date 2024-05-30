x: int
y: int
diferenca:int

print(f"Digite dois numeros: ")
x = int(input())
y = int(input())

if x > y:
    print(f"MAIOR NUMERO = {x}")
    diferenca = x - y
    print(f"DIFERENÇA = {diferenca}")

else:
    print(f"MAIOR NUMERO = {y}")
    diferenca = y - x
    print(f"DIFERENÇA = {diferenca}")