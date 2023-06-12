"""
StringIO - Não é built-in

Para ler ou escrever dados eem arquivos do sistema operacional o software precisa ter permissão: 
    - Permissão de Leitura -> Para ler o arquivo.
    - Permissão de escrita -> Para escrever o arquivo.

StringIO -> Utilizado para ler e criar arquivos em memória. (Não grava no disco e sim na memória do computador)
"""

# Importando stringIO

from io import StringIO;

mensagem = 'Está é apenas uma string normal';

# # Podemos criar um arquivo em memória, já com uma string inseria ou vazia.

# arquivo = StringIO(mensagem); # Mesma coisa que: arquivo = open('arquivo.txt', 'w');

# # OBS: Com a diferença que, quando utilizamos o StringIO o próprio SO gerá o nome do arquivo.

# # Lendo o arquivo
# print(arquivo.read());

# # Escrevendo no arquivo e movimentando o cursor
# arquivo.write('Outro texto');
# arquivo.seek(0);
# print(arquivo.read());

# StringIO com With e Close()

with StringIO(mensagem) as arquivo:
    print(arquivo.read());

print(arquivo.read()); # ValueError: I/O operation on closed file


arquivo = StringIO(mensagem);
arquivo.close();
print(arquivo.read()); # ValueError: I/O operation on closed file