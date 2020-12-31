"""
Crie um dicionário para armazenar o nome e a nota de 3 alunos, fazendo a leitura dos valores por meio de uma estrutura
de repetição. Depois, crie uma nova estrutura de repetição para somar todas as notas e retornar a média.
"""

# Criando uma Dicionário e uma Variável
student = {}

# Criando uma Estrutura de Repetição
for n in range(1, 4):
    # Usuário Insere os Valores
    name = input('Enter your name: ')
    note = float(input('Enter your note: '))

    # Inserindo os Dados no Dicionário
    student[name] = note


# Percorrendo o Dicionário e Criando uma Variável para fazer a Soma
soma = 0

# Criando uma Estrutura de Repetição Utilizando o for
for note in student.values():
    # Somando as Notas dos Alunos
    soma += note

# Calculando a Média das Notas e Apresentando na Tela
print('Your average is: ', soma / 3)
