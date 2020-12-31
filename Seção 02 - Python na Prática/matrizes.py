# Importando uma Biblioteca e Apelidando
import numpy as np


# Criando uma Matriz e Criando uma Variável
matriz = np.array([[2, 3, 1], [4, 5, 7]])

# Apresentando os Valores na Tela
print(matriz)

# Para saber o Número de Linhas e Colunas
print(matriz.shape)

# Para Acessar Posições Específicas da Matriz que Retornam Linhas
print(matriz[0])

# Para Acessar Posições Específicas da Matriz que Retornam Colunas
print(matriz[0][0])

# Percorrendo todas as linhas da Matriz
for i in range(matriz.shape[0]):
    # Apresentando os Valores na Tela
    print(matriz[i])

    # Percorrendo todas as Colunas da Matriz
    for j in range(matriz.shape[1]):
        # Apresentando os Valores na Tela
        print(matriz[i][j])
