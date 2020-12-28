# Declarando uma Variável e Criando um Laço de Repetição Utilizando o while que Inicia no 1 até 5
numero = 1
while numero < 6:
    # Imprimindo os Valores na Tela se a Condição for Verdadeira
    print(numero)

    # Somando a Variável Número mais 1
    numero += 1


# Declarando uma Variável e Criando um laço de Repetição Utilizando o While que Inicia no 5 até 1
numero = 5
while numero > 0:
    # Imprimindo os Valores na Tela se a Condição for Verdadeira
    print(numero)

    # Subtraindo da Variável Número Menos 1
    numero -= 1


# Declarando Duas Variáveis e Criando uma Laço de Repetição para Somar os Valores de 1 até 5 utilizando o While

# Somando os Valares da Variável Soma Mais Número
soma = 0

# Contador do laço de Repetição While
numero = 1
while numero < 6:
    # Somando a Variável Soma Mais o Número
    soma += numero

    # Somando a Variável Número Mais 1
    numero += 1

# Imprimindo os Valores se a Condição for Verdadeira
print(soma)


# Declarando uma Variável e Criando um Laço de Repetição para Interagir com o Usuário Utilizando o While
numero = - 1
while numero < 1 or numero > 10:
    # Usuário Insere o Número Através do Input
    numero = int(input('Digite um número de 1 a 10: '))
