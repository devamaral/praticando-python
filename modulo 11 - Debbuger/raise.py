""" 
Levantando os próprios erros com raise

raise -> Lança exceções

OBS: O raise não é uma função. É uma palavra reservada, assim como def ou qualquer outra.

Para simplificar, pense no raise como sendo útil para que possamos criar nossas próprias exceções e mensagens de erro.

A forma geral de utilização é: 

raise TipoDoErro('Mensagem de erro');

# Exemplo real

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string');
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string');

    print(f'O texto {texto} será impresso na cor {cor}');

colore('Hello World', True);
"""

# Exemplo real

def colore(texto, cor):
    cores = ('Verde', 'Amarelo', 'Azul', 'Branco');
    if cor not in cores:
        raise ValueError('Valor não está contindo em nossa tupla');
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string');
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string');

    print(f'O texto {texto} será impresso na cor {cor}');

colore('Hello World', 'Vermelho');