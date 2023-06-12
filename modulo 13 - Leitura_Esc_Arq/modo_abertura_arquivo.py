"""
Modos de Abertura de Arquivo

r -> Abre para leitura - padrão
w -> Abre para escrita - sobrescreve caso o arquivo já exista
x -> Abre para escrita somente se o arquivo não existir. Caso o arquivo exista, gera FileExistsError
a -> Abre para escrita, adicionando o conteúdo ao final do arquivo. 
    # OBS: Abrindo no modo 'a' -> append, se o arquivo não existir será criado. Caso exista o novo conteúdo será adicionado no final do arquivo SEMPRE 
    # OBS: Com o modo 'a' não controlamos o cursor.
+ -> Abre para ao modo de atualização - Leitura e Escrita 

https://docs.python.org/3/library/functions.html#open

try:
    with open('teste.txt', 'x') as arquivo:
        arquivo.write('Teste de conteudo');
except FileExistsError:
    print('Arquivo já existe')
""" 

with open('teste.txt', 'a') as files:
    while True:
        fruta = input('Digite o nome de uma fruta ou sair: ');
        if fruta != 'sair':
            files.write(fruta + '\n');
        else:
            break 