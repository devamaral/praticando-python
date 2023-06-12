"""
Loop For

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis


nome = 'Lucas Gabriel';
lista = [1, 2, 5, 6, 8];
numeros = range(1, 10);


for letra in nome:
    print(letra, end='');


for numero in lista:
    print(numero);


novaLista = [];

for numero in numeros:
    novaLista.append(numero);

print(novaLista);

for indice, letra in enumerate(nome):
    print(indice, letra);


OBS: Quando não precisamos de um valor, utilizamos o underline para descarta-lo

for _, letra in enumerate(nome):
    print(letra);


for letra in enumerate(nome):
    print(letra[1])
"""

print('\U0001F604')