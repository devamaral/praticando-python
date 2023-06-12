"""
Estruturas lógicas: and, or, not, is

Operadores unários:
    - not
Operadoers binários:
    - and, or, is
"""
ativo = True
logado = True

if ativo and logado:
    print('Bem-vindo usuário');
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail');

print(ativo is False);