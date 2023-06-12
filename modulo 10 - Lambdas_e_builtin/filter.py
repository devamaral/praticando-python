""" 
Filter

filter() -> Serve para filtrar dados de uma determinada coleção

"""
# Bibilioteca para trabalhar com dados estatísticos
import statistics;

# Dados coletados de algum sensor

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1];

# Calculando a média dos dados utilizando a função mean()

media = statistics.mean(dados);

print(media);
res = filter(lambda dado: dado >= media, dados);

print(list(res));
print(list(res));

# OBS: Assim como a função map(), após serem utilizados os dados de filter() eles são excluidos da memória.

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador'];

res = filter(None, paises);

print(list(res));


# Diferença entre map e filter:

# Map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento do iterável.
# Filter() -> Recebe dois parâmetros, uma função e um iterável e retorna um objetado filtrando apenas  

usuarios = [
    {'Username': 'Lucas', 'Tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'Username': 'Julio', 'Tweets': ['Eu amo meu gato']},
    {'Username': 'Robert', 'Tweets': []},
    {'Username': 'Sandro', 'Tweets': []},
    {'Username': 'Bernado', 'Tweets': ['Eu gosto de cachorros', 'Vou sair hoje']}
];

inativos = list(filter(lambda u: len(u['Tweets']) == 0, usuarios));

print([user['Username'] for user in inativos]);