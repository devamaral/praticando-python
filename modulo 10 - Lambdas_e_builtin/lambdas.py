"""
Utilizando Labdas

Conhecidas por expressões Lambdas, ou simplesmente Lambdas, são funções sem nome, ou seja funções anônimas.

# Expressão Lambda

lambda x: 3 * x + 1;

# Utilizando expressão lambda

calc = lambda x: 3 * x + 1;

print(calc(4));
print(calc(7));
""" 

# Expressões lambdas com multiplas entradas

nome_completo = lambda nome, sobrenome: f'{nome.strip().title()} {sobrenome.strip().title()}';

print(nome_completo('Lucas', 'Gabriel'));
print(nome_completo('JAMIlLY', '  braz  '));


# Mais exemplos - Ordenando sobre o sobrenome.

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arhur C. Clarke'];

autores.sort(key= lambda sobrenome: sobrenome.split(' ')[-1].lower());

print(autores)