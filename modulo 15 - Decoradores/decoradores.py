""" 
Decoradores (Decorators)

O que são decorators?

- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos
- Decorators também são exemplos de Higher Order Functions;
- Decorators tem uma sintaxe própria, usando "@" (Syntact Sugar / Açucar Sintático);

"""

# Decorators como funções (Sintaxe não recomendada) / Sem Syntact Sugar

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!');
        funcao();
        print('Tenha um ótimo dia!');
    return sendo;


def saudacao():
    print('Seja bem-vindo(a)');


teste = seja_educado(saudacao);

teste();


# Decorators com sintax Sugar - Forma recomendada

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!');
        funcao();
        print('Tenha um excelente dia');
    return sendo_mesmo;

@seja_educado_mesmo
def apresentando():
    print('Meu nome é Lucas');


apresentando()