""" 
Reversed 

OBS: Não confunda com a função reverse() das listas.

A função reverse() só funciona em listas.

Já a função reversed() funciona com qualquer iterável.

Sua função é inverter o iterável.

A função retorna um iterável chamado list_reverseiterator.
"""

# Exemplos

lista = list(range(1, 6));

# Podemos converter o elemento retornado para uma Lista, Tupla ou Conjunto

# Lista
print(list(reversed(lista)));

# Tupla
print(tuple(reversed(lista)));

# Conjunto
print(set(reversed(lista))); # O set/conjunto não define/guarda ordem.


# Podemos iterar sobre o reversed

for letra in reversed('Geek University'):
    print(letra, end='');


# Mesma coisa que a de cima sem utilizar for
print('');
print(''.join(list(reversed('Geek'))));


# Forma mais facil com slice de strings
print('Geek University'[::-1]);