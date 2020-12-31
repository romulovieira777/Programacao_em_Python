# Criando um Dicionário e Declarando uma Variável
collect = {'Aedes Aegypt': 32, 'Aedes Albopictus': 22, 'Anopheles Darlingi': 14}

# Chamando uma Chave para Apresentar o Valor na Tela do Usuário
print(collect['Aedes Aegypt'])


# Adicionando Dados no Dicionário
collect['Rhodnius Montenegrensis'] = 11

# Apresentando Valor na Tela do Usuário
print(collect)


# Apagando um Dado do Dicionário
del(collect)['Aedes Albopictus']

# Apresentando os Valores em Tela
print(collect)


# Apresentando Todos os Items do Dicionário
print(collect.items())

# Apresentando Somente as Chaves na Tela
print(collect.values())


# Criando um Novo Diconário e Declarando uma Variável
collect_02 = {'Anopheles Gambiae': 13, 'Anopheles Deaneorum': 14}


# Concatenando os Dois Dicionários
collect.update(collect_02)

# Apresentando os Valores na Tela
print(collect)


# Percorrendo o Diconário
print(collect.items())


# Percorrendo o Diconário com for e Criando Duas Variáveis
for especie, num_especimes in collect.items():
    # Apresentando os Valores na Tela
    print(f'Species: {especie}, number of species collecetd: {num_especimes}')


# Criando uma Nova Variável e Criando uma Tupla
biomolecules = ('Proteína', 'Ácidos Nucleicos', 'Carboidrato', 'Lipídeo', 'Ácidos Nucleicos', 'Carboidrato',
                'Carboidrato', 'Carboidrato')

# Apresentando os Valores na Tela
print(biomolecules)


# Transformando a Tupla em Conjunto e Apresentando na Tela dos Valores
print(set(biomolecules))


# Criando Duas Variáveis
set_01 = {1, 2, 3, 4, 5}
set_02 = {3, 4, 5, 6, 7}

# Criando uma Variável fazendo a Intersecção das Duas Variaveis a cima
set_03 = set_01.intersection(set_02)

# Apresentando os Valores em Tela
print(set_03)

# Criando uma Variável e Apresentando a Diferença entre os Conjuntos 1 e 2
set_04 = set_01.difference(set_02)

# Apresentando os Valores na tela
print(set_04)

# Criando uma Variável e Apresentando a Diferença entre os Conjuntos 2 e 1
set_05 = set_02.difference(set_01)

# Apresentando o Valor na Tela
print(set_05)
