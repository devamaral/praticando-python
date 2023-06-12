"""
Sistema de Arquivos - Manipulação


import os;

# Descobrindo se um arquivo ou diretório existe.
# Diretório
# Paths relativos

print(os.path.exists('arquivo.txt'));
print(os.path.exists('modulo 13 - Leitura_Esc_Arq\StringIO.py')); 
print(os.path.exists('modulo 13 - StringIO.py')); 


# Path absolutos

print(os.path.exists('C:\\Users\lucas\OneDrive\Área de Trabalho\Estudos\Praticando\Python\geek\modulo 13 - Leitura_Esc_Arq'));


# Criando arquivos

# Forma 1
open('arquivo_teste1.txt', 'w').close();

# Forma 2
open('arquivo._teste2.txt', 'a').close();

# Forma 3
with open('arquivo_teste3.txt', 'w') as arquivo:
    pass;


# Forma correta utilizando os
# os.mknod('arquivo_teste4.txt');

# OBS: Se você estiver utilizando no Mac OS, pode haver um erro de PermissionError


# Criando diretório

os.mkdir('templates');

# OBS: A função mkdir() cria um diretório se este não existir. Caso exista, teremos FileExistsError.
"""

import os 

# Criando mais de um diretório

os.makedirs('teste1/teste2/teste3', exist_ok=True);
 

# Renomear arquivos e diretorios
# os.rename('teste1', 'teste');
os.rename('teste/teste2/teste3', 'teste22');

# OBS: Se o diretório não existir teremos um FileNotFoundError
# OBS: Se o diretório que queremos renomear não estiver vazio, teremos um OSError