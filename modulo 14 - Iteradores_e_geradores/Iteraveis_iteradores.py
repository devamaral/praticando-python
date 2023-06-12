"""
Entendendo Iterador e Iterável

Iterador | Iterator -> 
    - Um objeto que pode ser iterado.
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada.

Iterável | Iterable ->
    - Um objeto que irá retornar um Iterador quando a função iter() for chamada.

""" 

nome = 'Lucas Gabriel'; # É um Iterável mas não é um Iterador.
numeros = [1, 2, 3, 4, 5]; # É um Iterável mas não é um Iterador.

print(hasattr(numeros, '__iter__'));

for letra in nome:
    print(letra);