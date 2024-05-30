def soma_digitos(numero):
    soma = 0
    # Verifica se o número é negativo
    if numero < 0:
        numero = -numero
    
    # Converte o número em uma string
    numero_str = str(numero)
    
    # Percorre cada dígito na string
    for digito in numero_str:
        # Converte o dígito de volta para um número inteiro e adiciona à soma
        soma += int(digito)
    
    return soma

# Obtém o número do usuário
numero = int(input("Digite um número inteiro: "))

# Calcula a soma dos dígitos
resultado = soma_digitos(numero)

# Exibe o resultado
print(f"A soma dos dígitos de {numero} é: {resultado}")