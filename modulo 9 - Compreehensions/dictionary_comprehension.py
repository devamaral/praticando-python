"""
Dictionary Comprehension


"""

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4};

quadrado = {chave: valor ** 2 for chave, valor in dicionario.items()};

print(quadrado);

numero = range(1, 6);

quadrados = {valor: valor ** 2 for valor in numero};
print(quadrados) 