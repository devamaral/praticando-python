"""
Zip

zip() -> Cria um iterável (Zip Object) que agrega elemento de cada um dos iteráveis passados como entrada em pares.


# Exemplo

lista1 = [1, 2, 3];
lista2 = [4, 5, 6];

zip1 = zip(lista1, lista2, 'abc');

print(zip1);
print(type(zip1));

# Sempre podemos gerar uma Lista, Tupla, Set ou dicionário

zip1 = zip(lista1, lista2, 'abc');
print(list(zip1));

zip1 = zip(lista1, lista2, 'abc');
print(tuple(zip1));

zip1 = zip(lista1, lista2, 'abc');
print(set(zip1));

zip1 = zip(lista1, lista2);
print(dict(zip1));
"""

# Podemos utilizar diferente iteráveis com zip

tupla = 1, 2, 3, 4, 5;
lista = [6, 7, 8, 9, 10];
dic = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15};

zt = zip(tupla, lista, dic.values());
print(list(zt));


# Lista de tuplas

dados = [(0, 1), (2, 3), (4, 5), (6, 7)];
print(list(zip(*dados)));


# Exemplo mais complexos

prova1 = [7.8, 2.4, 9.2];
prova2 = [5.5, 9.8, 7.1];
alunos = ['Lucas', 'Gabriel', 'Amaral'];

resp = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)};

print(resp);