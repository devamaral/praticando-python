""" 
Módulo Collections - Named Tuple

# Recapitulando tupla:

tupla = (1, 2 ,3);

print(tupla[1]);

Named tuple -> São tupla, diferenciadas, onde especificamos um nome para a mesma e também parâmentros
"""

# Importando

from collections import namedtuple;

# Precisamos definir o nome e parâmentros.

# Forma 1 - Declarando Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome');

# Forma 2 - Declarando Named Tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome');

# Forma 3 - Declarando Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome']);

# Usando

ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray');

print(ray);
print(ray[1]);