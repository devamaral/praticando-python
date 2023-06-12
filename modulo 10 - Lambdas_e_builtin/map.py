""" 
Map

Com map, fazemos mapeamento de valores para função.
"""

import math

def area(r):
    """Calcula a área de circulo com raio 'r'. """
    return math.pi * (r ** 2);

print(area(2));
print(area(5.3));

raios = [2, 5, 7.1, 0.3, 10, 44];

# Forma comum

areas = [];

for r in raios:
    areas.append(area(r));

print(areas);

# Forma 2 - Map
# OBS: Map é uma função que recebe dois parâmentros: O primeiro a função, O segundo um interável


areas = map(area, raios);

print(list(areas))

# OBS: Após utilizar a função map() depois da primeira utilização do resultado, ela zera.

Clientes = ['lucas', 'jonathan', 'douglas', 'albert', 'thomas'];

formata_nome = lambda nome: nome.title();

print(list(map(formata_nome, Clientes)));

# OBS: Função sempre que é utilizada dentro de um map ele recebe apenas um parâmentro (obrigatório)