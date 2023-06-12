""" 
Funções com Parâmentro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída;

"""

# Refatorando uma função

def quadrado(numero):
    # return numero * numero
    return numero ** 2

print(quadrado(2));
print(quadrado(5));
print(quadrado(7));

# OBS¹: Se determinamos parâmentro em nossa função e não for passado irá gerar um error -> TypeError
# OBS²: OBS¹ serve tanto para parâmetros a menos quanto parâmetros a mais.

# parâmetros são variáveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função;
# A ordem dos parêmntros importa!

def nome_completo(nome, sobrenome):
    return f'seu nome completo é {nome} {sobrenome};'

nome = 'Lucas';
sobrenome = 'Gabriel';

print(nome_completo(sobrenome, nome));


# Argumentos nomeados (Keyword Arguments)
# Caso utilizemos nomes dos parâmetros nos argumentos para informálos, podemos utilizar qualquer ordem.

print(nome_completo(nome=nome, sobrenome=sobrenome));
print(nome_completo(sobrenome=sobrenome, nome=nome));