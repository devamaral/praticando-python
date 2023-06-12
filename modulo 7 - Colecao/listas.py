"""
Listas

Listas em Python funciona como vetores/matrizes (arrays), com a diferença de serem
DINÂMICO e também de podermos colocar QUALQUER tipo de dado.

Linguagens C/Java: Array
    - Possuem tamanho e tipo de dado fixo;

Já em Python:

- Dinâmico: Não possui tamanho fixo; (enquanto houver memória disponivel);
- Qualquer tipo de dado;

As listas em Python são representadas por colchetes: []

lista = [1, 4, 3, 2, 5,];

def esta_na_lista(lista):
    if 2 in lista:
        print('Encontrei o 2');

# esta_na_lista(lista);


# Podemos ordenar uma lista facilmente
def ordenar_lista(lista):
    lista_ordenada = lista.copy();
    lista_ordenada.sort();

    print(lista);
    print(lista_ordenada);

# ordenar_lista(lista);


# Podemos facilmente contar o número de ocorrencia em uma lista
def contar_ocorrencias(lista):
    lista.append(1)
    print(lista.count(1));

# contar_ocorrencias(lista);


# Adiciona UM elemento em uma lista, só é possivel adiciona um elemento por vez.
# Possivel adiciona uma lista dentro de outra lista. (Sublista)
def adicionar_elemento(lista):
    lista.append(42);
    print(lista);

# adicionar_elemento(lista);


# Junta mais de um valor em uma unica lista
# Junta duas lista em uma unica
# Só aceita iteraveis
def juncao_multiplas_listas(lista):
    lista_ordenada = [5, 2, 20, 50];
    lista.extend(lista_ordenada);
    print(lista);

# juncao_multiplas_listas(lista);


# Adiciona um elemento a lista na posição especifica
def adicionar_elemento_posicao(lista):
    lista.insert(0, 55);
    print(lista);

# adicionar_elemento_posicao(lista);


# Podemos facilmente juntar duas lista
def juncao_lista_concat(lista):
    lista_nova = [5, 6, 7];
    lista_juncao = lista + lista_nova;
    print(lista_juncao)

# juncao_lista_concat(lista);


# Inverter uma lista
def inverter_lista(lista):
    lista.reverse();
    print(lista);

# inverter_lista(lista);


# Podemos contar quantos elementos tem dentro de uma lista
def contar_elementos(lista):
    print(len(lista));

# contar_elementos(lista);


# Podemos facilmente remover o último elemento de uma lista
# OBS¹: o metodo pop tem um retorno
# OBS²: podemos remover por indice, só passar nos ()
# OBS³: os elementos serão deslocados para esquerda
def remover_elemento(lista):
    print(lista);
    numRemovido = lista.pop();
    print(lista);
    print(numRemovido);

# remover_elemento(lista);


# Removendo todos os elementos (Zerando a lista)
def zerando_lista(lista):
    print(lista);
    lista.clear();
    print(lista);

# zerando_lista(lista);


# Repetindo os elementos da lista
def repetindo_elementos(lista):
    print(lista)
    lista = lista * 3;
    print(lista);

# repetindo_elementos(lista);


# Convertendo uma string para lista
# OBS: Por padrão o split separada os elementos da lista pelo espaço entre elas
def string_para_lista():
    nome = 'Lucas Gabriel';
    nome = nome.split();
    print(nome);

# string_para_lista();


# Convertendo uma lista em uma string
def lista_para_string():
    nome = ['Lucas', 'Gabriel', 'Gaiao', 'do', 'Amaral'];
    nome = ' '.join(nome);
    print(nome);

# lista_para_string();


# Iterando sobre uma lista

# Exemplo 1 - Utilizando while

carrinho = [];
produto = '';

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ");
    print('Nome do produto: ', end='');
    produto = input();

    if produto != 'sair':
        carrinho.append(produto);

for produto in carrinho:
    print(produto);


# Utilizando variáveis em listas

num1 = 1;
num2 = 2;
num3 = 3;
num4 = 4;
num5 = 5;

numeros = [num1, num2, num3, num4, num5];

print(numeros);


cores = ['Azul', 'Vermelho', 'Rosa', 'Verde'];

for indice, cor in enumerate(cores):
    print(indice, cor);
    
cores = list(enumerate(cores));
print(cores)



# buscando o cinco a partir do indice 3

print(lista.index(5, 3));


# Revisão slicing

# lista[inicio:fim:passo]
# range[inicio:fim:passo]

lista = list(range(1, 11));

# Trabalhando com slice de lista com parâmentro 'inicio'

print(lista[1:]); # Iniciando no índice 1 e pegando todos os elementos restantes
print(lista[:5]); # do começo até o indice 5
print(lista[::2]); # do começo até o fim pulando de dois em dois


# Invertendo valores de uma lista

nomes = ['Lucas', 'Gabriel'];
nomes[0], nomes[1] = nomes[1], nomes[0];

print(nomes)


"""


