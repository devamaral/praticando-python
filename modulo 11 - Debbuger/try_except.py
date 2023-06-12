""" 
O bloco try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Previnindo assim que o programa para de funcionar e o usuário receba mensagens de erro inesperadas.

A forma geral mais sinmples é:

try:
    // execução problemática
except:
    // solução problemática caso haja


# Exemplo 1 - Tratando um erro genérico.

try:
    nome();
except:
    print('Deu algum problema');

# OBS: Trata erro de forma genérica não é a melhor forma de tratamento de erro, O ideal é SEMPRE tratar de forma específica.


# Exemplo 2 - Tratando um erro específico.

try:
    nome();
except NameError:
    print('Você está utilizando uma função inexistente');

# Exemplo 3 - Tratando um erro específico com detalhes do erro.

try:
    len(5);
except TypeError as error:
    print(f'A aplicação gerou o sequinte erro: {error}');

"""

# Exemplo 3 - Utilizando varios tratamentos de erros de uma vez.

try:
    # len(5);
    nome();
except NameError  as erra:
    print(f'Deu NameError: {erra}');
except TypeError as errb:
    print(f'Deu TypeError {errb}');

# OBS: Podemos efetuar diversos tratamentos de erros de uma vez.


# Exemplo 4 - Tratando erro dentro de uma função

dic = {'nome': 'Lucas'};

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave];
    except KeyError:
        return None;
    except TypeError:
        return None;

print(pega_valor(dic, 'nomes'));

