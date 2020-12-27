"""
Calcular a média de um aluno que cursou a disciplina de Programação I, a partir da leitura das notas M1, M2 e M3;
passando por um cálculo da média aritmética. Após a média calculada, devemos anunciar se o aluno foi aprovado,
reprovado ou pegou exame.
- Se a média estiver entre 0.0 e 4.0, o aluno está reprovado
- Se a média estiver entre 4.1 e 6.0, o aluno pegou exame
- Se a média for maior do que 6.0, o aluno está aprovado
- Se o aluno pegou exame, deve ser lida a nota do exame. Se a nota do exame for maior do que 6.0,
está aprovado, senão; está reprovado.
"""

# Criando Três Variáveis do Tipo Float
m_01 = float(input('Enter your first note: '))
m_02 = float(input('Enter your second note: '))
m_03 = float(input('Enter your third note: '))

# Criando uma Variável para Calcular a Média
average = (m_01 + m_02 + m_03) / 3

# Criando a Estrutura de Condição
if (average >= 0.0) and (average <= 4.0):
    # Imprimi o Valor na se a Primeira Condição for Verdadeira
    print('Student is disapproved!')

# Se a Primeira Condição for Falsa Executa esse Elif
elif (average >= 4.1) and (average <= 6.0):
    # Se o Aluno ficou de Exame Digitar a Nota do Exame
    exam = float(input('Enter exam grade: '))

    # Criando a Estrutura de Condição para a Nota do Exame
    if exam >= 6.0:
        # Imprimi o Valor na Tela se a Nota for Maior que 6.0
        print('Student passed the exam!')
    # Se a Nota for Menor que 6.0 Executa esse Else
    else:
        print('Student failing the exam!')

# Se a Primeira e a Segunda Condição forem Falsas Executa esse Elif
else:
    # Imprimi o Valor na Tela se a Primeira e a Segunda Condição forem Falsas
    print('Student is approved!')
