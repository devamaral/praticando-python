""" 
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência à Teoria dos Conjuntos da matemática.

- No Python, os conjuntos são chamados de Sets.

Dito isto, da mesma forma que a matemática:

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar com chave, valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos (Set) e Maps (Dict) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;


# Definindo um conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 6, 7, 5, 2});

print(s);
print(type(s));

# OBS: Ao criar um conjunto, caso seja adicionado um valor existente, o mesmo será ignorado sem gerar error e não fará parte do conjunto. 

# Forma 2 - Mais comum

s = {1, 2, 3, 4, 5};

print(s);
print(type(s));


# Adicionando um elemento em um conjunto

s = {1, 2, 3};

s.add(4);
s.add(4); # Duplicidade não gera error e sim ignorado
print(s);


# Remover elementos em um conjunto

# Forma 1

s.remove(3) # Informamos o valor a ser removido

# OBS: Caso o valor não seja encontrado será gerado o erro KeyError

# Forma 2 

s.discard(2);
print(s);
"""

# Separando elementos unicos:

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'};
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'};

# Forma 1 - Union

unicos1 = estudantes_python.union(estudantes_java);
print(unicos1)

# Forma 2 - Utilizando o caractere pipe |

unicos2 = estudantes_python | estudantes_java;
print(unicos2);


# gerar um conjunto de estudante em ambos os cursos

# Forma 1 - Utilizando intersection

ambos1 = estudantes_python.intersection(estudantes_java);

# Forma 2 - Utilizando o &

ambos2 = estudantes_python & estudantes_java
print(ambos2)


# Gerando um conjunto de estudantes que não estão no outro curso

so_python = estudantes_python.difference(estudantes_java);
so_java = estudantes_java.difference(estudantes_python);

print(so_python);
print(so_java);