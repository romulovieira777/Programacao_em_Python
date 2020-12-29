# Criando uma Função sem Parâmetro e sem Retorno
def mensagem():
    # Imprimi na Tela o Valor da Função
    print('Texto da Função!')


# Chamando a Função
mensagem()


# Criando uma Função com Passagem de Parâmetro e Declarando uma Variável
def mensagem(texto):
    # Imprimi na Tela a Mensagem passada pelo Usuário dentro da Fução
    print(texto)


# Chamando a Função e Passando os Valores
mensagem('Hello, World!')


# Criando uma Função com Passagem de Parâmentro e Declarando Duas Variáveis
def soma(a, b):
    # Imprimi na Tela a Soma das Duas Variáveis
    print(a + b)


# Chamando a Função e Passando os Valores
soma(2, 3)


# Criando uma Função com Passagem de Parâmentro, Retorno e Declarando Duas Variáveis
def soma(a, b):
    # Retorna a Soma das Duas Variáveis
    return a + b


# Chamando a Função e Passando os Valores
print(soma(2, 3))


# Criando uma Função com Passagem de Parâmentro, Retorno, Declarando Três Variáveis e Deixando um Valor Padrão
# na Terceira Variável
def calcula_energia_potencial_gravitacional(m, h, g=10):
    # Criando uma Variável e Atribuindo o Cáculo para a Função
    '''
     Calcula a energia potencial gravitacional
     Argumentos:
     m: massa, entrada como uma variável float
     h: altura, entrada como uma variável float

     Argumento opcional:
     g: aceleração gravitacional, com valor default de 10
     '''
    e = g * m * h

    # Retorna a Soma das Variáveis
    return e


# Chamando a Função e Passando os Valores
print(calcula_energia_potencial_gravitacional(30, 12))

# Chamando a Função e Passando os Valores
print(calcula_energia_potencial_gravitacional(30, 12, 9.8))
