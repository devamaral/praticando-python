"""
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer uso do módulo os.

os -> Operating System - Sistema Operacional
"""

# Importando

import os;
# import platform
import sys


# getcwd() -> current work directory
# Retorna o path (caminho) absoluto

print(os.getcwd());


# chdir() -> Mudando o diretório

os.chdir('..');
print(os.getcwd());


# Checando se o diretório é absoluto 
print(os.path.isabs('C:\\Users\\lucas')) # True

# OBS para user windows:
#   - Devera ter cuidado ao verificar diretórios, deve-se ter que usar carectere de escape. 


# Identificando o sistema operacional
print(os.name); # Posix -> Linux e mac | Nt -> Windows

# Para mais detalhes
# print(os.uname()); # Só funciona em alguns sistemas unix
# print(platform.uname()); # Tem que importa o platform
# print(sys.platform) 


# Juntando diretorio e alterando-o

print(os.getcwd()); # c:\Users\lucas\OneDrive\Área de Trabalho\Estudos\Praticando\Python
print(os.path.join(os.getcwd(), 'modulo 3')); # c:\Users\lucas\OneDrive\Área de Trabalho\Estudos\Praticando\Python\modulo 3
print(os.path.join(os.getcwd(), 'modulo 12 - Modulos', 'pacotes')); # c:\Users\lucas\OneDrive\Área de Trabalho\Estudos\Praticando\Python\modulo 12\pacotes


# Lista de arquivos
print(len(os.listdir('c:\\')));


import os

scanner = os.scandir();

# Diretorios com mais detalhes em lista
arquivos = list(scanner);

# print(dir(arquivos[0]));

print(arquivos[0].name); # Nome do arquivo
print(arquivos[0].inode()); # ??
print(arquivos[0].is_dir()); # é um Diretorio?
print(arquivos[0].is_file()); # é um Arquivo?
print(arquivos[0].is_symlink()); # é um Link Simbólico?
print(arquivos[0].path); # caminho até o arquivo
print(arquivos[0].stat()); # Estatísticas

# OBS: Quando utilizamos a função scandir() precisasse fechar-lá como abrir um arquivo.

scanner.close();