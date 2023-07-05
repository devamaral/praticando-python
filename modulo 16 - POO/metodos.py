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


from passlib.hash import pbkdf2_sha256 as cryp


class Usuarios:
    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} usuário(s) no sistema')

    @staticmethod
    def definicao():
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuarios.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuarios.contador = self.__id
        print(f'Usuario criado: {self.__gera_usuarios()}')

    # def __corre__(self, metros):  # Não indicado
    #     print(f'Estou correndo {metros} metros')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False
    
    # Método privado
    def __gera_usuarios(self):
        return self.__email.split('@')[0]


# p1 = Produto('Playstation 4', 'Video Game', 2300)
# user1 = Usuarios('Lucas', 'Gabriel', 'lucas@gmail.com', '123')
# user2 = Usuarios('Claudio', 'Bezerra', 'claudiob@gmail.com', '321')

# print(p1.desconto(20))
# print(Produto.desconto(p1, 40))  # self e desconto

# print(user1.nome_completo())
# print(Usuarios.nome_completo(user2))

# print(f'Senha User 1: {user1._Usuarios__senha}')  # Acesso de forma errada de um atributo de classe privado
# print(f'Senha User 2: {user2._Usuarios__senha}')  # Acesso de fomra errada de um atributo de classe privado

# nome = input('Informa o nome: ')
# sobrenome = input('Informe o sobrenome: ')
# email = input('Informe o email: ')
# senha = input('Informe a senha: ')
# Confirmasenha = input('Confirme a senha: ')

# if senha == Confirmasenha:
#     user = Usuarios(nome, sobrenome, email, senha)
# else:
#     print('Senha não confere.')
#     exit(1)

# print('Usuário criado com sucesso!')

# senha = input('Informe a senha para acesso: ')

# if user.checa_senha(senha):
#     print('Acesso permitido')
# else:
#     print('Acesso negado')

# print(f'A senha cryptografada: {user._Usuarios__senha}') # Acesso errado


# Métodos de Classe

user = Usuarios('Lucas', 'Gabriel', 'lucas@gmail.com', '12345')

Usuarios.conta_usuarios()  # Forma correta
user.conta_usuarios()  # Possível, mas incorreta

# Métodos de Classe em Python são conhecidos como Métodos Estáticos em outra linguagem

print(user._Usuarios__gera_usuarios())  # Acesso, de forma ruim.


# Métodos Estático

print(Usuarios.contador)
print(Usuarios.definicao())
print(user.contador)
print(user.definicao())