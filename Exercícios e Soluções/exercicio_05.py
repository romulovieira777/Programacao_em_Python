"""
Ler 5 notas e informar a média.
"""

# Declarando Três Variáveis e Criando um laço de Repetição Utilizando o While

# Somando as Notas
sum = 0

# Declarando a Variável
note = 0

# Contador de Notas Digitadas
count = 0

# Criando o Laço de Repetição com o While
while count < 5:
    # Usuário Insere as Notas Através do Input
    note = float(input('Digite a sua nota: '))

    # Somando as Notas
    sum += note

    # Contando a Passagem no Laço de Repetição
    count += 1

# Imprimindo a Média das Notas na Tela
print(f'Their average was: {sum / count}!')
