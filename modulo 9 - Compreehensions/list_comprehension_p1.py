"""
List Comprehension

- Utilizando List Comprihension nós podemos gerar novas listas com dados processados a partir de outro iterável.

# Sintaxe da List Comprehension

[ dado for dado in iterável ]
"""

# Exemplos

numeros = range(1, 6);

res = [numero * 10 for numero in numeros];

print(res); # 10, 20, 30, 40, 50

"""
Para entender melhor o que está acontecendo devemos dividir a expressão em duas partes:

- A primeira parte: for numero in numeros
- Segunda parte: numero * 10
"""

def funcao(valor):
    return valor * valor;

res = [funcao(numero) for numero in numeros];

print(res);
