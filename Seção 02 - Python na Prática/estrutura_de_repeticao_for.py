# Criando uma Estrutura de Repetição Usando o print
print(1)
print(2)
print(3)
print(4)
print(5)


# Criando um Laço de Repetição Utilizando o for que Inicia no 1 até o 5
for numero in range(1, 6):
    # Imprimindo os Valores na tela
    print(numero)


# Criando um Laço de Repetição Utilizando o for que Inicia no 5 até o 0
for numero in range(5, 0, -1):
    # Imprimindo os Valores na Tela
    print(numero)


# Declarando uma Variável e Criando um Laço de Repetição para Somar Valores de 1 até 5
soma = 0
for numero in range(1, 6):
    # Somando a Variável Soma com o Número que passa no laço for
    soma = soma + numero

    # Imprimindo os Valores Parciais da Soma
    print(soma)

# Imprimindo o Valor Final da Soma
print(soma)


# Declarando uma Variável e Criando um Laço de Repetição Utilizando o for
palavra = 'sorvete'
for letra in palavra:
    # Imprimindo as Letras na Tela
    print(letra)


# Declarando uma Variável e Criando um Laço de Repetição Utilizando o for
palavra = 'sorvete'
for letra in palavra:
    # Imprimindo as Letra na Tela
    print(letra)

    # Verificando se na Palavra Existe a Letra v
    if letra == 'v':
        # Imprmindo na Tela se a Condição for Verdadeira
        print('Achou a letra v')


# Criando Dois Laços de Repetição Usando for
for i in range(0, 5):
    # Imprimindo os Valores na Tela
    print(i)

    # Imprimindo Caracteres na Tela
    print('---')

    # Criando o Segundo Laço de Repetição Utilizando o for
    for j in range(0, 3):
        # Imprimindo os Valores na Tela
        print(j)

# Dando Espaço na Impressão na Tela
print()
