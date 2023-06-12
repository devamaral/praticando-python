""" 
Mapas -> Conhecidos em Python como Dicionários

Dicionários em Python são representados por chaves {}


receita = {'jan': 150, 'fev': 200, 'mar': 250};

# Interar sobre dicionários

# Imprimindo chaves
for chave in receita:
    print(chave);

# Imprimindo valores
for cahve in receita:
    print(receita[chave]);

for chave in receita:
    print(f'{chave} : {receita[chave]}');

# Outra forma para mostrar chaves e valores

print(receita.keys());
print(receita.values());

# Modo paitonico

for chave in receita.keys():
    print(receita[chave]);
"""

# Desempacotamento de dicionários
receita = {'jan': 150, 'fev': 200, 'mar': 250};

print(receita.items());

for chave, valor in receita.items():
    print(f'chave: {chave} e valor: {valor}');


# Encontrando valor maximo, minimo, soma e tamanho

print(max(receita.values()));
print(min(receita.values()));
print(sum(receita.values()));
print(len(receita));