""" 
Módulo Collections - Deque

Podemos dizer que o deque é uma lista de alta perfomace.
"""

# importando
from collections import deque

# Criando deques

deq = deque('Lucas');

print(deq);

# Adicionando elementos no deque

deq.append('G'); # Adiciona no final
print(deq);

deq.appendleft('k'); # Adiciona no começo da lista
print(deq); 

# Removendo elementos

print(deq.pop());
print(deq.popleft());