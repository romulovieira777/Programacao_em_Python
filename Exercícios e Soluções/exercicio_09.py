"""
Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros e os armazene dentro de uma lista.
Após a leitura, crie outra estrutura de repetição para somar todos os valores digitados.
"""

# Criando uma Lista e Declarando uma Variável
list_01 = []

# Percorrendo toda a Lista
for lista in range(1, 6):
    # Insere os Valores Percorridos no for na Lista Criada
    list_01.append(lista)

# Apresenta os Valores na Tela
print(list_01)


# Percorrendo a Lista e Criando uma Variável para fazer a Soma
soma = 0

# Criando uma Estrutura de Repetição Utilizando o for
for i in range(len(list_01)):
    # Somando os Valores na Variável Soma
    soma += list_01[0]
    soma += list_01[1]

# Apresenta os Valores na Tela
print('Sum', soma)
