"""
Min e Max

max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elementos.

"""
# Com uma lista

lista = [1, 8, 44, 88, 2];

print(max(lista));

# Com um dicionario

dicionario = {'a': 1, 'b': 5, 'c': 18, 'd': 80};
print(max(dicionario.values()));

# Outros exemplos

nomes = ['Lucas', 'Leonardo', 'Vilva', 'Ruth'];

print(min(nomes));
print(max(nomes));

# OBS: Ele está levando em consideração a ordem alfabetica;

print(max(nomes, key=lambda nome: len(nome)));
print(min(nomes, key=lambda nome: len(nome)));

# Outros exemplos

musicas = [
    {'Titulo': 'Thunderstruck', "Tocou": 43},
    {'Titulo': 'Vida cara', "Tocou": 13},
    {'Titulo': 'War', "Tocou": 60},
];

print(min(musicas, key=lambda musica: musica['Tocou'])['Titulo']);
print(max(musicas, key=lambda musica: musica['Tocou'])['Titulo']);