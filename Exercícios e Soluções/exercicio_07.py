"""
Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit.
A fórmula de conversão é F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit e
C é a temperatura em graus Celsius.
- Função para ler e retorna o valor da temperatura (não recebe parâmetro).
- Função para fazer o cálculo (recebe como parâmetro a temperatura em graus Celsius).
- Função para mostrar o resultado, recebendo como parâmetro o valor e fazendo a impressão.
"""


# Criando uma Função que lê a Temperatura em Graus Celsius e Declarando uma Variável
def read_temperature():
    # Usuário passa o Valor da Temperatura através do input
    temperature = float(input('Enter the temperature in degress Celsus: '))

    # Retorna o Valor da Temperatura
    return temperature


# Criando uma Função para Converter a Temperatura em Celsius para Fahrenheit e Declarando uma Variável
def calculation(temperature_celsus):
    # Convertendo o Valor da Temperatura Celsius para Fahrenheit
    temperature_fahrenheit = (9 * temperature_celsus + 160) / 5

    # Retorna o Valor da Temperatura Convertido para Fahrenheit
    return temperature_fahrenheit


# Criando uma Função para Mostrar o Cálculo da Temperatura na tela e Criando uma Variável
def show(temperature_fahrenheit):
    # Imprimindo o Valor na Tela
    print(temperature_fahrenheit)


# Chamando as Três Funções Criadas e Criando Três Variáveis
temperature_celsus = read_temperature()

temperature_fahrenheit = calculation(temperature_celsus)

show(temperature_fahrenheit)
