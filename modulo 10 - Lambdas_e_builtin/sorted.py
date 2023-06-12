""" 
Sorted

OBS: Não confunda, apesar do nome, com a função sort() que já estudamos em Listas. O sort()
só fuinciona em listas.

Podemos utilizar o sorted() com qualquer iterável

Como o próprio nome diz, sorted() serve para ordenar elementos.
"""

# Exemplo

numeros = [6, 1, 8, 2];
print(numeros);

print(sorted(numeros)); # Ordenar do menor para o maior;
print(sorted(numeros, reverse=True)); # Ordenar do maior para o menor;


# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {'Username': 'Lucas', 'Tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'Username': 'Julio', 'Tweets': ['Eu amo meu gato']},
    {'Username': 'Robert', 'Tweets': []},
    {'Username': 'Sandro', 'Tweets': []},
    {'Username': 'Bernado', 'Tweets': ['Eu gosto de cachorros', 'Vou sair hoje']}
];

# Ordenando pelo username 
print(sorted(usuarios, key=lambda usuario: usuario['Username']));

# Ultimo exemplo

musicas = [
    {'Titulo': 'Thunderstruck', "Tocou": 43},
    {'Titulo': 'Vida cara', "Tocou": 13},
    {'Titulo': 'War', "Tocou": 60},
];

print(sorted(musicas, key=lambda musica: musica['Tocou'], reverse=True));