"""
Criando uma própria versão do loop

"""

def meu_for(iteravel):
    i = iter(iteravel);
    while True:
        try:
            print(next(i));
        except StopIteration:
            break;

meu_for([1, 2, 3, 4]);