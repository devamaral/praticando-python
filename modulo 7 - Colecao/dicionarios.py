"""   
Dicionários

OBS: Em algumas linguagens de programção, os dicionários Python são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}.

print(type({}));

OBS: Sobre dicionários
    - Chave e valor podem ser de qualquer tipo;
    - Chave e valor são separado por dois pontos 'chave':'valor';


# Criação de dicionários

# Forma 1 (Mais comum)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos'}
print(paises);
print(type(paises));


# Forma 2 (Menos comum)

paises = dict(br= 'Brasil', eua= 'Estados Unidos');


# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br']);


# Forma 2 - Acessando via get - Recomendada

print(paises.get('br'));
print(paises.get('us'));
print(paises.get('ru', 'Não encontrado')); # Utilizando um valor padrão, caso não localize a chave informada.


# Também podemos utilizar o in

paises = {'br': 'Brasil', 'eua': 'Estados Unidos'};

print('br' in paises);
print('us' in paises);


# Podemos utilizar qualquer tipo de dado
# Tuplas por exemplo são bastante interessante de serem utilizadas como chave de dicionários, pois são imutáveis. 

localidades = {
    (35.6823, 39.5232): 'Escritório em Tókio',
    (74.2145, 12.7851): 'Escritório em Paris',
    (15.2523, 21.3222): 'Escritório em Brasilia'
};

print(localidades);
print(type(localidades));


# Adicionar elementos em um dict

receita = {'janeiro': 100, 'fevereiro': 120, 'março': 200};
print(receita);

# Forma 1 - Mais comum

receita['abril'] = 350;
print(receita);

# Forma 2 

novo_dado = {'maio': 400};

receita.update(novo_dado);
print(receita);

# Atulizando dados em um dict

# Forma 1

receita['maio'] = 550;
print(receita);

# Forma 2

receita.update({'maio': 600});
print(receita);

# Conclusão¹: A forma de adicionar novos elementos ou atualizar dados em um dict é a mesma.
# Conclusão²: Em dicionários, NÃO podemos ter chave repertidas. 


# Removendo dados de um dicionário

# Forma 1 - Mais comum

receita.pop('maio');

# OBS¹: Precisamos SEMPRE informa a chavem caso não encontre um keyError é retornado.
# OBS²: Ao removervemos um objeto, o valor deste objeto é sempre retornado. 


# Forma 2 

del receita['fevereiro'];
print(receita);

# OBS¹: Se a chave não existir será gerado um KeyError.
# OBS²: Neste caso o valor removido não é retornado. 

"""

# A onde utilizar dicionario?

# OBS¹: Diferente da lista, conseguimos consultar pelo nome(chave) do produto;
# OBS²: Diferente de tuplas, conseguimos modificar os elementos;

# Froma não usual de criação de dicionários

outro = {}.fromkeys('a', 200);

print(outro);
print(type(outro));

# O método from keys recebe dois parâmentros: um interável e um valor