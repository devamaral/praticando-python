""" 
Módulo Collections - Counter (Contador)

Collections -> High-performace Container Datetypes

Counter -> Recebe um interável como parâmentro e cria um objeto do tipo Collections Counter que é parecido com um dicionário, contento como chave o elemento da lista passado como parâmentro e como valor a quantidade de ocorrências desse elemento.

# Utilizado para conta o número de ocorrencia do elemento/iterável passado como parâmentro;


# Utilizando o Counter

from collections import Counter;

# Podemos utilizar qualquer iterável, aqui usamos uma lista

lista = [1, 1, 1, 2, 2, 2, 3, 4, 4, 5, 5, 6];

# Utilizando o Counter
res = Counter(lista);

print(type(res)); # <class 'collections.Counter'>
print(res); # Counter({1: 3, 2: 3, 4: 2, 5: 2, 3: 1, 6: 1})
"""

from collections import Counter;

print(Counter('Lucas Gabriel Gaiao do Amaral'));