""" 
Generators


"""
nomes = ['Lucas',' Leonardo', 'Leo', 'Leandro']

# List Comprehension
# print([nome[0] == 'L' for nome in nomes]);

# Generator
# print((nome[0] == 'L' for nome in nomes));


# Qual utilizar?
    # - Se queremos exibir/precisar da lista para algo utilize o List
    # - Se for para apenas fazer uma checagem no caso não utilizar, exibir a lista utilize o generator

# Qual é o mais performatico, que economiza mais memória, ocupa menos recurso em memória
    # - Generator
    # - Pelo fato do que ele retorna;


# Qual é a utilidade de getsizeof() ? -> Retorna a quantidade de bytes em memória do elemento passado como parâmentro

from sys import getsizeof;

# List Comprehension
print(getsizeof('List Comprehension: ', [x * 10 for x in range(1000)]), 'Bytes');

# Generator
print(getsizeof('Generator: ', (x * 10 for x in range(1000))), 'Bytes');

# Set Comprehension
print(getsizeof('Set Comprehension: ', {x * 10 for x in range(1000)}), 'Bytes');


