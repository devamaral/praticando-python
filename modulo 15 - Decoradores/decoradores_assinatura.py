""" 
Decorators com diferentes assinaturas

Para resolver, utilizamos um parâmentro de projeto chamado Decorator Pattern


# Relembrando

def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper();
    return aumentar;


@gritar
def saudacao(nome):
    return f'Olá, eu sou o {nome}';

@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.';

# Testando

print(saudacao('Lucas'));


# A assinatura de uma função é representada pelo seu retorno, nome e parâmentros de entrada.

"""

# Utilizando Decorator Pattern - Refatorando funções acima

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper();
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o {nome}';

@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, gostaria de {principal}, acompanhado de {acompanhamento}, por favor.';


print(saudacao('Lucas'));
print(ordenar('picanha', 'Batata Frita'));
print(ordenar(acompanhamento='Farofa', principal='Carne de sol'));

# Decorator com argumentos

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}';
            return funcao(*args, **kwargs);
        return outra; 
    return interna;


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2;


print(soma_dez(10, 12));
print(soma_dez(1, 21));