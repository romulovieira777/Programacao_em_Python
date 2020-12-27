"""
Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem,
utilizando um automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário deve fornecer o
tempo gasto na viagem e a velocidade média durante ela. Desta forma, será possível obter a distância
percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a
quantidade de litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12.
O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a
quantidade de litros utilizada na viagem.
"""

# Criando Duas Variáveis
time = float(input('Enter the time spent traveling: '))
velocity = float(input('Enter the average speed: '))

# Criando uma Variável com o Cálculo da Distância
distance = time * velocity

# Criando uma Variável com o Cálculo de Litros Usados
used_liters = distance / 12

# Imprimindo os Valores das Variáveis na Tela
print('Average speed:', velocity)
print('Time spent traveling:', time)
print('Distance traveled:', distance)
print('Numbers of liters:', round(used_liters, 1))
