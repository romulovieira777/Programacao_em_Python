# Criando uma Variável do Tipo Tupla
tupla = ('Homo Sapiens', 'Canis Familiaris', 'Felis Catus')

# Apresenta os Valores na Tela
print(tupla)


# Acessando a Posição 0 na Tupla e Apresenta os Valores na Tela
print(tupla[0])


# Vendo a Posição do Valor na Tupla e Apresenta os Valores na Tela
print(tupla.index('Canis Familiaris'))


# Percorrendo a Tupla Utilizando o for e Criando uma Variável
for elemento in tupla:
    print(elemento)


# Criando uma Variável do Tipo Lista
lista_01 = ['Homo Sapiens', 'Canis Familiaris', 'Felis Catus']
lista_02 = ['Xenopus Laevis', 'Ailuropoda Melanoleuca']


# Concatenando as Duas Listas Criadas e Criando uma Nova Lista
lista_03 = lista_01 + lista_02

# Apresenta os Valores na Tela
print(lista_03)


# Criando uma Lista, Declarando uma Variável e Multiplicando essa Lista
lista_04 = lista_02 * 2

# Apresenta os Valores na Tela
print(lista_04)


# Acessando Somente Dois Elementos da Lista e Apresenta os Valores na Tela
print(lista_04[0:2])


# Adicionado Valores na Lista_04
lista_04.append('Gorila')


# Removendo um Dado da Lista
lista_01.remove('Felis Catus')

# Apresenta os Valores na Tela
print(lista_01)


# Percorrendo a Lista Utilizando o for e Criando uma Variável
for item in lista_04:
    # Apresenta os Valores
    print(item)
