""" 
Reduce 

OBS: A partir do Python3+ a função reduce() não é mais uma função integrada (built-in). Significa que devemos importa e utilizar a partir do módulo 'functools'

Guido van Rossum: Utilize a função reduce() se você realmente precisar dela. Em todo caso, 99%¨das vezes um loop for é mais legível.

# Assim como map() e filter(), a função reduce() recebe dois parâmetro: a função e o iterável.

reduce(funcao, dados)


""" 

from functools import reduce

dados = [2, 3, 4, 5, 11, 23, 52, 12, 19];

# OBS: Para utilizar o reduce() nós precisamos de uma funçõa que recebe dois parâmetro

multi = lambda x, y: x + y;

res = reduce(multi, dados);
print(res);