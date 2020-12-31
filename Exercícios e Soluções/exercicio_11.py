"""
Dada a matriz abaixo, construa uma estrutura de repetição para percorrer e somar todos os elementos da matriz.

matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])
"""

# Importando a Biblioteca numpy
import numpy as np


# Modelo do Exercício
matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])


# Criando Duas Estruturas de Repetição para Somar os Valores
soma = 0

# Criando a Primeira Estrutura de Repetição Utilizando o for
for i in range(matriz.shape[0]):
    # Criando a Segunda Estrutura de Repetição Utilizando o for
    for j in range(matriz.shape[1]):
        # Somando os Valores e Armazenando na Variável Soma
        soma += matriz[i][j]

# Apresentando os Valores na Tela
print('The sum is: ', soma)


soma = 0
for i in range(matriz.shape[0]):
  for j in range(matriz.shape[1]):
    #print(matriz[i][j])
    soma += matriz[i][j]
print('Soma: ', soma)








