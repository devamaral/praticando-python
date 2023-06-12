""" 
Módulo Random e o que são módulos?

- Em Python, módulos nada mais são do que outros arquivos Python.

Módulo Random -> Possui várias funções para geração de números pseudo-aleatório.

"""

# OBS: existem duas formas de se utilizar um módulo ou função deste

# Forma 1 - Importando todo o módulo (Não recomendado)
# Ao realizar o import de todo o módulo, todas as funções, atributos, calsses e propriedades que estiverem dentro do módulo ficarão disponíveis (Ficarão em memória)
# Caso você sabia quais funções utilizar, está não seria a forma ideal de utilização

import random

print(random.random());


# Forma 2 - Importando função especifica de um módulo

from random import random # Gera números aleatórios - (float) 
from random import uniform # Gera números aleatórios (a, b) - (float) 
from random import randint # Gera números aleatórios (a, b) - (inteiro) 
from random import choice # Mostra um valor aleatório entre um iterável
from random import shuffle # Serve para embaralhar dados

print(random());
print(uniform(1, 50));
print(randint(1, 50));
print(choice(['Pedra', 'Papel', 'Tesoura']));
cartas = ['K', 'Q', 'J', 'A', '2', '3', '4'];
shuffle(cartas)
print(cartas);