""" 
Módulo Collections - Default Dict

# Recapitulando sobre Dicionários

dicionario = {'curso': 'Programação em Python: Essencial'};

print(dicionario);
print(dicionario['curso']);

Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default, podendo utilizar um lambda para isso, este valor será utilizado sempre que não houver um valor definido. Caso tentamos acessar uma chave que não existe, essa chave será criada e ovalor default será atribuído. 

OBS: lambdas são funções sem nome, que podem ou não receber parâmentros de entrada e retornar valor
"""

from collections import defaultdict

dicionario = defaultdict(lambda: None);
dicionario['curso'] = 'Programação em Python: Essencial';

print(dicionario['curso']);
print(dicionario['outro']);
print(dicionario);

