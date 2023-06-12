"""
Try/Except/Else/Finally

Dica de quando e onde tratar código:

TODA ENTRADA DEVE SER TRATADA!

OBS: A função do usuário é DESTRUIR seu sistema.

num = None;

try: 
    num = int(input('Informe um número: '));
except ValueError:
    print('Usuário digitou um valor inválido.')

print(f'Você digitou {num}');

"""

# Exemplo 1 - Utilizando o else
# Else -> É executaod somento se não ocorrer o erro.

try: 
    num = int(input('Informe um número: '));
except ValueError:
    print('Usuário digitou um valor inválido.');
else:
    print(f'Você digitou {num}');


# Exemplo 2 - Utilizando o Finally
# Finally -> O bloco finally é SEMPRE executado. Independente se houve exceção ou não.
# O finally, geralmente, é utilizado para fechar ou desalocar recursos. (Exemplo abrir e fechar conexão de banco de dados)

try: 
    num = int(input('Informe um número: '));
except ValueError:
    print('Usuário digitou um valor inválido.');
else:
    print(f'Você digitou o número: {num}');
finally:
    print('Depois do bloco try/except');