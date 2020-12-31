### :computer: Comandos em Python que foram usados nos Arquivos acima: :rocket:
**O que faz a função append:**

Adiciona qualquer valor completo, por exemplo, se enviarmos um objeto, ele adiciona o objeto, se enviarmos uma lista, ele adiciona a lista inteira ao invés de seus itens.

**Sintaxe**

~~~py
append(<variável>):
~~~

**Exemplo**

~~~py
lista_04.append('Gorila')
~~~

**O que faz a função as:**

Adiciona um apelido.

**Sintaxe**

~~~py
as(<apelido>):
~~~

**Exemplo**

~~~py
import numpy as np
~~~

**O que faz a função array:**

São estruturas de dados semelhantes às listas do Python, mas não tão flexíveis.

**Sintaxe**

~~~py
array([[2, 3, 1], [4, 5, 7]])
~~~

**Exemplo**

~~~py
matriz = np.array([[2, 3, 1], [4, 5, 7]])
~~~

**O que faz a função def:**

É para definir uma função que é uma sequência de comandos que executa alguma tarefa e que tem um nome.

**Sintaxe**

~~~py
def nome(<parâmetros>):
    comandos:
~~~

**Exemplo**

~~~py
def hello(meu_nome):
    print('Olá',meu_nome)
~~~

**O que faz a função del:**

Remove um dado do seu dataset

**Sintaxe**

~~~py
del(<variável[<posição>]>)
~~~

**Exemplo**

~~~py
del(collect)['Aedes Albopictus']
~~~

**O que faz a função difference:**

Traz os valores não correspondente nos dois conjuntos.

**Sintaxe**

~~~py
difference(<variável>)
~~~

**Exemplo**

~~~py
set_05 = set_02.difference(set_01)
~~~

**O que faz a função else:**

A instrução else é uma instrução dependente, isto é, uma instrução que não pode ser utilizada sozinha. A seguir, temos um exemplo, utilizando a instrução if junto a instrução else. A instrução else só é executada se a condição do if for falsa.

**Sintaxe**

~~~py
else:
~~~

**Exemplo**

~~~py
idade = 18
if idade >= 18:
    print('maior de idade')
else:
    print('menor de idade')
~~~

**O que faz a função float:**

Devolve um número de ponto flutuante construído a partir de um número ou string.

**Sintaxe**

~~~py
float(<variável>)
~~~

**Exemplo**

~~~py
nota1 = float(input("Entre com a primeira nota: "))
~~~

**O que faz a função for:**

Executa um ciclo para cada elemento do objeto que está sendo iterado.

**Sintaxe**

~~~py
for <variável> in <objeto iterável>:
    bloco de instrução
~~~

**Exemplo**

~~~py
for numero in range(1, 6):
    print(numero)
~~~

**O que faz a função if:**

É uma estrutura de condição que permite avaliar uma expressão e, de acordo com seu resultado, executar uma determinada ação.

**Sintaxe**

~~~py
if(<variável>)
~~~

**Exemplo**

~~~py
idade = 18
if idade < 20:
    print('Você é jovem!')
~~~

**O que faz a função import:**

É uma linha com o caminho completo para o arquivo python que contem o módulo que se deseja importar.

**Sintaxe**

~~~py
import(<biblioteca>)
~~~

**Exemplo**

~~~py
import math
~~~

**O que faz a função in:**

Verifica se o operando a sua esquerda, está contido na lista a sua direita.

**Sintaxe**

~~~py
 in (<variável>)
~~~

**Exemplo**

~~~py
2 and 3 in range(1,6)
~~~

**O que faz a função index:**

Retorna o index de determinado elemento.

**Sintaxe**

~~~py
 list.index(x[, start[, end]])
~~~

**Exemplo**

~~~py
print(tupla.index('Canis Familiaris'))
~~~

**O que faz a função input:**

É para entrada de dados feita pelo usuário.

**Sintaxe**

~~~py
input(<variável>)
~~~

**Exemplo**

~~~py
nome = input('Entre com o nome do aluno: ')
~~~

**O que faz a função intersection:**

Traz somente os valores existentes nos dois conjuntos.

**Sintaxe**

~~~py
intersection(<variável>)
~~~

**Exemplo**

~~~py
set_03 = set_01.intersection(set_02)
~~~

**O que faz a função items:**

Traz todos os items da lista

**Sintaxe**

~~~py
items()
~~~

**Exemplo**

~~~py
print(collect.items())
~~~

**O que a função print faz:**

Imprimir um argumento passado na tela.

**Sintaxe**

~~~py
print(<variável>)
~~~

**Exemplo**

~~~py
print('Olá, Mundo!')
~~~

**O que a função range faz:**

Permite-nos especificar o início da sequência, o passo, e o valor final.

**Sintaxe**

~~~py
range(<variável>):
~~~

**Exemplo**

~~~py
range(0, 10)
~~~

**O que a função remove faz:**

Remove o primeiro item encontrado na lista cujo valor é igual a x.

**Sintaxe**

~~~py
list.remove(x)
~~~

**Exemplo**

~~~py
lista_01.remove('Felis Catus')
~~~

**O que a função return faz:**

É utilizada para declarar a informação a ser retornada pela função.

**Sintaxe**

~~~py
return(<condição>):
~~~

**Exemplo**

~~~py
def soma(x,y):
    num = x * y
    return num
~~~

**O que a função round faz:**

É receber um número qualquer e arredondar ele.

**Sintaxe**

~~~py
round(<variável>)
~~~

**Exemplo**

~~~py
print(round(1.3569874587, 6))
~~~

**O que a função set faz:**

Transforma uma lista ou tupla em conjunto.

**Sintaxe**

~~~py
set(<lista ou tupla>)
~~~

**Exemplo**

~~~py
print(set(biomolecules))
~~~

**O que a função shape faz:**

Retorna um tuple de dimensões da matriz.

**Sintaxe**

~~~py
my_array.shape
~~~

**Exemplo**

~~~py
array_shape = my_array.shape
~~~

**O que a função sqrt faz:**

Retorna a raíz quadrada do número.

**Sintaxe**

~~~py
sqrt(<variável>)
~~~

**Exemplo**

~~~py
print(sqrt(81))
~~~

**O que a função str faz:**

Converte um dado para string.

**Sintaxe**

~~~py
str(<variável>)
~~~

**Exemplo**

~~~py
nome = str(input('Qual é seu nome? '))
~~~

**O que a função update faz:**

Atualiza dicionário com pares chave/valor, sobrescrevendo chaves existentes.

**Sintaxe**

~~~py
update(<dicionário>)
~~~

**Exemplo**

~~~py
collect.update(collect_02)
~~~

**O que a função values faz:**

Traz todos os valores do dicionário.

**Sintaxe**

~~~py
values()
~~~

**Exemplo**

~~~py
print(collect.values())
~~~

**O que a função while faz:**

Repete a sequência de comandos definida em seu corpo enquanto a <condição> permanece verdadeira.

**Sintaxe**

~~~py
while(<condição>):
~~~

**Exemplo**

~~~py
numero = 1
while numero < 6:
    print(numero)
    numero += 1
~~~
