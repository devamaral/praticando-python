"""
Debuggando com PDB

PDB -> Python Debugger

Bug -> Inseto
"""

# OBS: Em vez de utilizar o print para debuggar código (que é uma pratica ruim), podemos utilizar o modo debugger;

# Utilizando o print para debuggar

# def dividir(a, b):
#     print(a, b);
#     try:
#         return int(a) / int(b);
#     except (ValueError, ZeroDivisionError) as err:
#         return f'Ocorreu um problema: {err}';

# print(dividir(2, 0));


# Utilizando o debug da IDE

# def dividir(a, b):
#     try:
#         return int(a) / int(b);
#     except (ValueError, ZeroDivisionError) as err:
#         return f'Aconteceu o seguinte erro: {err}'

# print(dividir(2, 0));


# Utilizando o PDB - Python Debugger

# Para utilizar o Python Debugger, precisamos importar a biblioteca pdb e entõa utilizar a função set_trace()

# Comandos básicos do PDB:
# l (listar onde estamos no código)
# n (proxíma linha)
# p (imprimir variável)
# c (continua a execução - finaliza o debugging)


# nome = 'Angelina';
# sobrenome = 'Jolie';
# # import pdb; pdb.set_trace();
# nome_completo = nome + ' ' + sobrenome;
# curso = 'Programação em Python: Essencial';
# final = nome_completo + ' Faz o curso ' + curso;
# print(final);


# A partir do Python 3.7, não é mais necessário importar a biblioteca pdb, pois o comando de debug foi incorporado como função built-in, chamada breakpoint()

nome = 'Angelina';
sobrenome = 'Jolie';
breakpoint()
nome_completo = nome + ' ' + sobrenome;
curso = 'Programação em Python: Essencial';
final = nome_completo + ' Faz o curso ' + curso;
print(final);