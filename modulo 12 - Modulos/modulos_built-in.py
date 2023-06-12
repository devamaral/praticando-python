""" 
Trabalhando com Módulos Builtin (módulos integrados, que já vem instalado no Python)


""" 
# utilizando alias (apelidos) para módulos/funções

import random as rdm;

print(rdm.random());

# alias para função

from random import randint as rdi, random as rdm;

print(rdi(1, 21));
print(rdm());

# Podemos importar todas as funções de um módulo utilizando o *

from random import *;

print(random());


# Importando varias funções do módulo random - tuple para múltiplos imports de um mesmo módulo

from random import (
    random,
    randint,
    shuffle,
    choice
);