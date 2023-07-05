""" 
Objetos -> São instâncias da classe. Ou seja, após o mapeamento do objeto do mundo real para sua representação computacional, devemos poder criar quantos objetos forem necessários. Podemos pensar objeto/instâncias de uma classe como variáveis do tipo definido na classe
"""


class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é {self.__cliente._Cliente__nome}')


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


# lampada1 = Lampada('branca', 110, 60)

# lampada1.ligar_desligar()
# print(f'A lâmpada está ligada: {lampada1.checa_lampada()}')

cliente1 = Cliente('Lucas', '119.288.242-09')
cc = ContaCorrente(5000, 1000, cliente1)

cc.mostra_cliente()