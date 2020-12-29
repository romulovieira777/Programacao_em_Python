"""
Imprimir a tabuada do número 3 (3 x 1 = 1 - 3 x 10 = 30).
"""

# Criando uma Variável e Criando um Laço de Repetição Utilizando o for

# Usuário Insere o Número Através do Input
number = int(input('Enter a number: '))

# Criando o Laço de Repetição com for que fará o Cálculo
for num in range(1, 11):
    # Imprimindo o Valor na Tela da Multiplicação
    print(f'{number} x {num} = {number * num} ')
