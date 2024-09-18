# Inicializa a soma como 0
soma = 0

# Inicializa o contador
contador = 0

# Laço while para ler 10 números inteiros
while contador < 10:
    numero = int(input("Digite um número inteiro: "))
    soma += numero  # Adiciona o número à soma
    contador += 1   # Incrementa o contador

# Apresenta a soma dos números
print("A soma dos 10 números é:", soma)
