""" 
Entendendo o *args

- O *args é um parâmetro, como outro qualquer. Isso significa que você poderá chamar de qualquer coisa, desde que começe com asterisco.

Exemplo:

*Xis

Mas por convenção, utizamos *args para definí-lo

Mas o que é o *args?

O Parâmentro *args utilizado em uma função, coloca os valores extras informados como entrada em uma tupla
"""

# Exemplos

def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3;

print(soma_todos_numeros(4, 6, 9))

# Entendendo o *args

def soma_todos_numeros(*args):
    total = 0;

    for numero in args:
        total = total + numero;

    return total;

# Melhorando a função com args

def soma_todos_numeros(*args):
    return sum(args);

print(soma_todos_numeros(3, 4, 5, 6));


# Outro exemplo de utilização do *args

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek!';
    return 'Eu não tenho certeza quem você é...';

print(verifica_info());
print(verifica_info(1, True, 'University', 'Geek'));
print(verifica_info(1, 'University', 3.145));

def soma_todos_numeros(*args):
    return sum(args);

numeros = [1, 2, 3, 4, 5, 6, 7];

# Desempactador

print(soma_todos_numeros(*numeros));

# OBS: O asterisco serve para que informemos ao Python que estamos passando como argumento uma coleção de dados. Desta forma, ele sabéra que é preciso antes desempacotar estes dados.