""" 
Módulo Collections: Ordered Dict

# Em dicionário, a ordem de inserção dos elementos não é garantida.
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4};

for chave, valor in dicionario.items():
    print(f'chave: {chave} | valor: {valor}');

OrderedDict - > É um dicionário, que nos garante a ordem de inserção dos elementos.
"""

from collections import OrderedDict;

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4});

for chave, valor in dicionario.items():
    print(f'chave: {chave} | valor: {valor}');


# Entendendo a diferença entre Dict e Ordered Dict

dict1 = {'a': 1, 'b': 2};
dict2 = {'b': 2, 'a': 1};

print(dict1 == dict2); # True -> Já que a ordem dos elementos não importa para o dicionário

odict1 = OrderedDict({'a': 1, 'b': 2});
odict2 = OrderedDict({'b': 2, 'b': 1});

print(odict1 == odict2); # False -> A ordem dos elementos importa para Ordered Dict