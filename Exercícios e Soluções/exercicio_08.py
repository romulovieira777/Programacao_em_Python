"""
Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel
que faz 12 Km por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a
velocidade média durante ela. Desta forma, será possível obter a distância percorrida com a fórmula
DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a quantidade de litros de
combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar
os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros
utilizada na viagem.
- Função para ler os valores (não recebe parâmetro e retorna os dois valores).
- Função para calcular a distância (recebe como parâmetro o tempo e a velocidade e retorna a distância).
- Função para calcular a quantidade de litros (recebe como parâmetro a distância e retorna os litros).
- Função para apresentar o resultado (recebe como parâmetro os valores e somente imprime o resultado).
"""


# Criando uma Função e Declarando Duas Variáveis
def reading():
    # Usuário passa o Valor do Tempo Gasto na Viagem e a Velocidade Média através do input
    time = float(input('Enter the time spent on the trip: '))
    velocity = float(input('Enter the average speed: '))

    # Retorna os Valores Passados pelo Usuário
    return time, velocity


# Criando uma Função para Calcular a Distância percorrida e Declarando a Variável
def calculate_distance(time, velocity):
    # Calculando a Distância percorrida e Retorna o Valor da Distância Calculado
    return time * velocity


# Criando uma Função para Calcular a Quantidade de Litros Gasto na Viagem e Declarando a Variável
def used_liters(distance):
    # Calculando a Quantidade de Litros Gasto na Viagem e Retorna o Valor da Quantidade de Litros Gasto na Viagem
    return round(distance / 12, 2)


# Criando uma Função para Apresentar os Valores na Tela do Usuário

def show(velocity, time, distance, liters):
    # Apresenta os Valores na Tela do Usuário
    print('', velocity)
    print('', time)
    print('', distance)
    print('', liters)


# Chamando as Fuções Criadas a cima e Criando Três Variáveis
tim, velocit = reading()

distanc = calculate_distance(tim, velocit)

liter = used_liters(distanc)

show(tim, velocit, distanc, liter)
