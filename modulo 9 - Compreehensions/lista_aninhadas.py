"""
Listas Aninhadas (Nested Lists)

- Algumas lingaguens de programação possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais (Arrays/Vetores);
    - Multidimensionais (Matrizes);

Em Python nós temos as Listas

numeros = [1, 2, 3, 4, 5];
"""

# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]; # Matriz 3 X 3

# print(listas);
# print(type(listas));


# Acessando os dados

# print(listas[1][2]);


# Iterando com loops em listas aninhadas

for lista in listas:
    for elemento in lista:
        print(elemento);

# List Comprehension

[[print(elemento) for elemento in lista] for lista in listas];