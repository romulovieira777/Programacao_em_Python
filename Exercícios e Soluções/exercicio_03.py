"""
Leia a idade do usuário e classifique-o em:
- Criança – 0 a 12 anos
- Adolescente – 13 a 17 anos
- Adulto – acima de 18 anos
-Se o usuário digitar um número negativo, mostrar a mensagem que a idade é inválida.
"""

# Criando uma Variável do Tipo int
age = int(input('Enter your age: '))

# Criando a Estrutura de Condição
if (age >= 0) and (age <= 12):
    # Imprimi o Valor na Tela se a Primiera Condição for Verdadeira
    print('Your are Child!')

# Se a Primeira Condição for Falsa Excuta esse elif
elif (age >= 13) and (age <= 17):
    # Imprimi na Tela se a Primeira Condição for Falsa
    print(' Your are a Teenager!')

# Se a Primeira e a Segunda Condição for Falsa Excuta esse elif
elif age >= 18:
    # Imprimi na Tela se a Primeira e a Segunda Condição for Falsa
    print('Your are Adult!')

# Se Nenhumas das Três Condições forem Verdadeiras Executa o else
else:
    # Imprimi na Tela os Valores se Nenhuma das Três Condições forem Verdadeiras
    print('Age is Invalid!')
