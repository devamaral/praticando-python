"""
Pacotes

Diferença entre Módulo e Pacotes:

Módulo -> É apenas um arquivo Python que pode ter diversas funções para utilizarmos;
Pacote -> É um diretório contendo uma coleção de módulos;

OBS: Nas versões 2.x do Python, um pacote Python deveria conter dentro dele um arquivo chamado __init__.py.

Nas versões do Python 3.x, não é mais obrigatório a utilização deste arquivo, mas normalmente ainda é utilizado para manter compatibilidade.

from pacotes import geek1;

print(geek1.pi);
print(geek1.funcao1(4, 6));
"""

from pacotes.geek1 import funcao1;

print(funcao1(6, 9));