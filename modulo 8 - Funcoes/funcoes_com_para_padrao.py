""" 
Funções com Parâmetros Padrão (Default Paramters)

def quadrado(numero = 2):
    return numero ** 2;


print(quadrado());

# OBS: Em funções Python, os parâmentros com valores default (padrão) DEVEM sempre estar ao final da declaração. 
# Por quê utilizar parâmetros com valor dafault?
    - Nos permite ser mais flexíveis nas funções;
    - Evita erros com parâmetros incorretos;
    - Nos permite trabalhar com exemplos mais legíveis de código;

# Qualquer tipos de dados podemos utilizar com valores default, dentre eles:
    - Números, strings , floats, booleanos, listas, tuplas, dicionários, funções e etc. 
"""

total = 1;

def incrementa():
    global total # Avisando que queremos utilizar a variável global

    total = total + 1;

    return total;

print(incrementa())

# Atenção com variáveis globais (Se Puder evitar, evite!);
