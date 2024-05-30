def main():

    salario: float
    emprestimo: float
    limite_prestacao: float

    salario = float(input("Digite o seu salario: "))
    emprestimo = float(input("Digite o valor do emprestimo: "))

    limite_prestacao = salario * (20/100)

    if emprestimo > limite_prestacao:
        print(f"EMPRESTIMO NAO CONCEDIDO!")
    else:
        print(f"EMPRESTIMO CONCEDIDO!")


if __name__ == "__main__":
    main()