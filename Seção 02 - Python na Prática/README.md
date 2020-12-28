### :computer: Comandos em Python que foram usados nos Arquivos acima: :rocket:
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
