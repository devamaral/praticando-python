"""
POO - Métodos

- Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode realizar no seu sistema.

Em Python, dividimos os métodos, assim como os atributos porém contendo (três), em dois grupos: Métodos de instância e Métodos de Classe.

# Métodos de Instância

# O método dunder init __init__ é um método especial chamado de construtor e sua função é construir o objeto a partir da classe.

# OBS¹: Todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder (Double Underline)
# OBS²: Os métodos/funções dunder em Python são chamados de métodos mágicos.

# ATENÇÃO: Por mais que possamos criar nossas próprias funções utilizando dunder (underline no início e no fim) não é aconselhado. Python possui vários métodos com esta forma de nomesclatura e pode ser que mudemos o comportamento dessas funções mágicas internas da linguagem. Então, evite ao máximo. De preferência nunca o faça.

# Métodos são escritos em letras minúsculas. Se o nome for composto, o nome terá as palavras por underline.
"""


class Lampada:
    def __init__(self, cor, voltagem, luminosidade, ligada):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade 
        self.__ligada = False


class ContaCorrente:

    contador = 1234

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor

        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto"""
        return (self.__valor * (100 - porcentagem)) / 100


class Usuarios:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha

    def __corre__(self, metros):  # Não indicado
        print(f'Estou correndo {metros} metros')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


p1 = Produto('Playstation 4', 'Video Game', 2300)
user1 = Usuarios('Lucas', 'Gabriel', 'lucas@gmail.com', '123')
user2 = Usuarios('Claudio', 'Bezerra', 'claudiob@gmail.com', '321')

print(p1.desconto(20))
print(Produto.desconto(p1, 40))  # self e desconto

print(user1.nome_completo())
