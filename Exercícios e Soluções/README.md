### :computer: Comandos em Python que foram usados nos Arquivos acima: :rocket:
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

**O que faz a função elif:**

É parecida com else, porém a usamos quando queremos atribuir uma condição para else.

**Sintaxe**

~~~py
elif(<variável>)
~~~

**Exemplo**

~~~py
age = int(input('Enter your age: '))

if (age >= 0) and (age <= 12):
    print('Your are Child!')
elif (age >= 13) and (age <= 17):
    print(' Your are a Teenager!')
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

**O que faz a função int:**

Converte um dado string para um número inteiro.

**Sintaxe**

~~~py
int(<variável>)
~~~

**Exemplo**

~~~py
number_01 = int(input('Enter the first number: '))
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


