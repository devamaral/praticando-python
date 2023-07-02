"""
Entendendo Iterador e Iterável

Iterador | Iterator -> 
    - Um objeto que pode ser iterado.
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada.

Iterável | Iterable ->
    - Um objeto que irá retornar um Iterador quando a função iter() for chamada.

""" 

nome = 'Lucas Gabriel'; # É um Iterável/Iterable mas não é um Iterador/Iterator.
numeros = [1, 2, 3, 4, 5]; # É um Iterável/Iterable mas não é um Iterador/Iterator.

it1 = iter(nome);
it2 = iter(numeros);

print(next(it1));
print(next(it2));