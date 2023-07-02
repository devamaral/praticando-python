"""
POO - Classes

Em POO, Classes nada mais são do que modelos dos objetos do mundo real sendo representados computacionalmente.

Classes podem conter:
    - Atributos -> Representam as características do objeto. Ou seja, pelos atributos conseguimos representar computacionalmente os estados de um objeto.
    - Métodos (funções) -> Representam os comportamoes do objeto. Ou seja, as ações que este objeto pode realizar no sistema.

Em Python, para definir uma classe utilizamos a palavra reservada class.
OBS¹: Podemos utilizar o 'pass' em Python quando temos um bloco de códgo que ainda não está implementado.
OBS²: Quando nomeamos nossa classe em Python utilizamos por convenção o nome com a inicial em maúsculo. Caso o nome seja composto, utiliza-se as iniciais de ambas as palavras em maúsculo.

Dicas: Em computação nõa utilizamos: Acentuação, caracteres especiais, espaços ou similares para nomes de classes, atributos, métodos, arquivos, diretórios e etc.

OBS³: Quando estamos planejando um software e definimos quais classes teremos que ter no sistema, chamamos estes objetos que serão mapeados para classes de entidade.
"""


class Lampada:
    pass


class ContaCorrente:
    pass


lamp = Lampada()

print(type(lamp))
