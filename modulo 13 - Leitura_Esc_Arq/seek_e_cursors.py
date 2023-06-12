"""
Seek e Cursors

seek() -> É utilizada para movimenta o cursor pelo arquivo.
    - Recebe um parâmentro indicando onde queremos colocar o cursor


arquivo = open('arquivo.txt');

print(arquivo.read());

arquivo.seek(0); # Seek 0

# Com a função read() podemos limitar a quantidade de caracteres a serem lidos no arquivo

print(arquivo.read());

"""
arquivo = open('arquivo.txt');

# readline() -> Função que lê o arquivo linha a linha

# print(arquivo.readline());

# readlines()

print(arquivo.readlines());
print(len(arquivo.readlines()));

# OBS: Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo no disco do sistema operacional e o nosso programa. Essa conexão é chamada de streaming. Ao finalizar os trabalhos com o arquivo devemos fechar essa conexão. Pra isso utilizamos a função close()

# Passos para se trabalhar com um arquivo:
#   1- Abrir o arquivo.
#   2- Trabalhar o arquivo.
#   3- Fechar o arquivo.

print(arquivo.closed()); # Verifica se o arquivo está aberto ou fechado

arquivo.close();
