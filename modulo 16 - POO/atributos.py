""" 
POO - Atributos

Atributos -> Representam as características do objeto. Ou seja, pelos atributos nós conseguimos representar computacionalmente os estados de um objeto

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de Instância;
    - Atributos de Classe;
    - Atributos Dinâmicos;

# Atributos de instância: São atributos declarados dentro do método construtor.
OBS: Método construtor: É um método especial utilizado para a construção do objeto.


# Classes com atributos de instancias publicos


class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:
    def __init__(self, nome, email, senha, teste):
        self.nome = nome
        self.email = email
        self.senha = senha


class Teste:
    def __init__(cerveja, nome, idade):
        cerveja.nome = nome
        cerveja.idade = idade

# OBS: Não é obrigatório utilizar 'self', podendo utilizar qualquer nome porém por conversão programadores pythonista usa o 'self'


# Execução de método construtor
ps4 = Produto('Playstation4', 'Vídeo Game', 2099)


# OBS: Em Python, por convenção, ficou estabelecido que, todo atributo de uma classe é público. Ou seja, pode ser acessado em todo o projeto.
# Caso queiramos demostrar que determinado atributo deve ser tratado como privado, ou seja, deve ser acessado/utilizado somente dentro da própria classe onde está declarado,
# Utiliza-se __ duplo underscore no início de seu nome.
# Conhecido também como Name MangLing.


# Classes com atributos de instancias privados
class Acesso:
    def __init__(self, email, senha):
        # self.__email = email
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)

# OBS: Lembra-se que isso é apenas uma convenção, ou seja, a linguagem Python não vai impedir que façamos acesos aos atributos sinalizados como privados fora da classe.

# Exemplos


user = Acesso('user@gmail.com', '123456')
print(user.email)
# print(user.__senha) # AtributeError
# print(dir(user))
print(user._Acesso__senha) # Temos acesso. Mas n´~ao deveriamos fazer este acesso. (Name MangLing)
user.mostra_senha()
user.mostra_email()


# O que significa atributos de instância?

# Significa, que ao criarmos instância/objetos de uma classe, todas as instância terão este atributo

user1 = Acesso('@user1@gmail.com', '12345')
user2 = Acesso('@user2@gmail.com', '678910')

user1.mostra_email()
user2.mostra_email()


# Atributos de Classe

p1 = Produto('Mesa', 'Mesa de jantar', 3000)
p2 = Produto('Caderno', 'Caderno escolar', 10)

# Atributos de Classe, são atributos, claro, que são declarados diretamente na classe, ou seja, fora do construtor. Geralmente já inicializamos um valor e este valor é compartilhado entre todas as instancias da classe

# Refatorando Classe Produto


class Produto:

    imposto = 1.05  # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


p1 = Produto('Mesa', 'Mesa de jantar', 3000)
p2 = Produto('Caderno', 'Caderno escolar', 10)


print(p1.imposto) # Acesso possível, mas incorreto de um atributo de classe;
print(p2.imposto) # Acesso possível, mas incorreto de um atributo de classe;

# OBS: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe.

print(Produto.imposto) # Acesso correto de um atributo de classe;
print(p1.id)
print(p2.id)

# OBS: Em linguagens como o Java, os atributos conhecidos como atributos de casse aqui em Python é conhecido como atributo estáticos;
"""


class Produto:

    imposto = 1.05  # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

# Atributos dinâmicos -> Um atributo de instância que pode ser criado em tempo de execução;

# OBS: O atributo dinâmico será exclusivo da instãncia que o criou.


p1 = Produto('Arroz', 'Alimento', 2.90)
p2 = Produto('Feijão', 'Alimento', 9.20)

# Criando um atributo dinamico em tempo de execução - Existe a possibilidade porém não é comum
p2.peso = '5Kg'

print(f'Produto: {p2.nome}, Descrição {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')  # Funcionou, porque adicionamos na linha 163 dinamicamente o atributo dinamicamente
# print(f'Produto: {p1.nome}, Descrição {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso}')  # Erro, porque note que na classe Produto não tem o atributo peso


# Deletando atributos

print(p1.__dict__)  # Estrutura do objeto 1 / Develve os atributos da classe inclusive os dinamicos, exceto atributos de classes para um dicionário
print(p2.__dict__)  # Estrutura do objeto 2 / Develve os atributos da classe inclusive os dinamicos, exceto atributos de classes para um dicionário
# print(Produto.__dict__)  # Estrutura da Classe

del p2.peso
print(p1.__dict__)