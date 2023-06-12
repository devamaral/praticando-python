""" 
Any e ALl

all() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.
any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False
"""

# Exemplo do all():

print(all([0, 1, 2, 3, 4, 5])); # False -> 0 = False
print(all([1, 2, 3, 4, ])); # Verdadeiro 
print(all([])); # Verdadeiro 
print(all((1, 2, 3, 4, ))); # Verdadeiro 
print(all({1, 2, 3, 4, })); # Verdadeiro 

# OBS: Um iterável vazio convertido em boolean é False, mas o all() entende como True

