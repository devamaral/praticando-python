""" 
Geradores

- Geradores (Generator) são Iterator (Iteradores)

OBS: O contrarío não é verdadeiro. Ou seja, nem todo iterator é generator.

Outras informações:
- Generators podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra reserva yield;
- Generators podem ser criados com Expressões Geradoras;

Diferenças entre Funções e Generator Functions
------------------------------------------------------------------------------------------
| Funções                                       | Generator Functions                    |
------------------------------------------------------------------------------------------
| Utilizam return                               | Utilizam yield                         |
| Retorna uma vez                               | Podem utilizar yield mútiplas vezes    |
| Quando executada, retorna um valor            | Quando executada, retorna um generator |

""" 

# Exemplo Generator Function

def conta_ate(valor_maximo):
    contador = 1;
    while contador <= valor_maximo:
        yield contador;
        contado = contador + 1;
# OBS: Uma Generator Function não é um Generator. Ela gera um generator.

print(type(conta_ate(5)));