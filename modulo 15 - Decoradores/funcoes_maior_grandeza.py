"""
 Funções de Maior Grandeza - Higher Order Functions - HOF

 O que isso significa?

- Quando uma linguagem de programção suporta/permite HOF, indica que podemos ter funções que retornam outras funções como resultado ou mesmo que podemos passar funções como argumentos para outras funções, e até mesmo criar variáveis do tipo de funções nos nossos programas.

OBS: Na seção de funções, nós utilizamos isso.

Em Python, as funções são cidadões de Primeira Classe, Fisrt Class Citizen
""" 

# Exemplo - Definindo as funções

def somar(a, b):
    return a + b;


def diminuir(a, b):
    return a - b;


def multiplicar(a, b):
    return a * b;


def dividir(a, b):
    return a / b;


def calcular(num1, num2, funcao):
    return funcao(num1, num2);


print(calcular(4, 3, multiplicar));
print(calcular(4, 3, somar));
print(calcular(4, 3, diminuir));
print(calcular(4, 3, dividir));


# Nested Functions - Funções Aninhadas
# Podendo ter funções dentro de funções

# Exemplo

from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('E ai', 'Suma daqui', 'Gosto muito de você'));
    return humor() + pessoa;

print(cumprimento(' Lucas'));


# Retornando funções de outras funções

def faz_me_rir():
    def rir():
        return choice(('hahahaha', 'kskskssks', 'kkkkkkk'));
    return rir;

rindo = faz_me_rir();

print(rindo());


# Inner Functions (Funções internas) / (Nested Functions) podem acessa o escopo de funções mais externas.

def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahaha', 'kkkkkkk', 'akkakak'));
        return f'{risada} {pessoa}';
    return dando_risada;

rindo2 = faz_me_rir_novamente('Lucas');

print(rindo2())