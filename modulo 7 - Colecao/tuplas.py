"""   
Tupla são parecidas com listas 

Existem basicamentes duas diferenças?

1- As tuplas são representadas por parênteses
2- As tuplas são imutáveis 

lista1 = (1, 4, 23, 2, 5);
lista2 = 1, 4, 23, 2, 5;

Conclusão: Os parênteses representa as tuplas porém as vírgulas é o que definem as tuplas 

lista3 = (4, );


# Desempacotando tuplas

tupla = ('Lucas', 'Gabriel');
nome, sobrenome = tupla;


# Sobrescrevendo tupla

tupla1 = tuple(range(1, 5)); 
tupla2 = tuple(range(5, 10));

tupla1 = tupla1 + tupla2;

# OBS: Tuplas são imutáveis, mas podemos sobrescrever seus valores


"""

# Contando elementos dentro de uma tupla

tupla = ('l', 'u', 'c', 'a', 's', 'g', 'a');

print(tupla.count('a'));


# Dicas na utilização de tuplas

# Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção

# Exemplo 1

meses = ('Janeiro', 'Fevereiro', 'Março')

print(meses.index('Janeiro'));

# Por que utilizar tuplas?

# - Tuplas são mais rápida do que listas. 
# - Tuplas deixam seu código mais seguro.  
#       Isso porque trabalhar com elementos imutáveis tras segurança para o código.


# Copiando uma tupla para outra

tupla = 1, 2 , 3

nova = tupla # Na tupla não temos o problema de Shallow Copy

outra = (4, 5, 6)

nova = nova + outra

print(nova)
print(tupla)

