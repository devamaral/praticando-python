""" 
**kwargs

Poderíamos chamar este parâmetro de **xis, mas por convenção chamamos de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extra em uma tupla. O **kwargs exige que utilizemos parâmetros nomeados e e transforma esses parâmetros extras em um dicionário.


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}');

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul');

# OBS: Os parâmetros de *args e **kwargs não são obrigatórios

cores_favoritas();


# Nas nossas funções, podemos ter (nesta ORDEM):

- Parâmetro obrigatórios;
- *args;
- Parâmetro default (Não obrigatórios);
- **kwargs

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos');
    print(args);
    if solteiro:
        print('Solteiro');
    else:
        print('Casado');
    print(kwargs);

minha_funcao(8, 'Julia');
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True);
minha_funcao(34, 'Felipe', eu='Não', voce='vai');
minha_funcao(19, 'Carla', 9, 4, 3, java='False', python=True);


# Desempactoar com **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}";

nomes = {'nome': 'Lucas', 'sobrenome': 'Gabriel'};

print(mostra_nomes(**nomes));
""" 

def soma_multiplos_numeros(a, b ,c):
    print(a + b + c);

# soma_multiplos_numeros(1, 2, 3);

lista = [1, 2, 3];

soma_multiplos_numeros(*lista);

