"""
Módulos Externos

Para instalar pacotes/módulos externos utilizamos um gerenciador de pacote chamado -> pip - Python Installer Package

Todos os pacotes externos oficiais: https://pypi.org

Colorama -> É utilizado para permitir impressão de textos coloridos no terminal.
"""

from colorama import init
from colorama import Fore, Back, Style
from random import randint, choice

# for i in range(1, 11):
#     list_cor = [Fore.BLACK, Fore.BLUE, Fore.WHITE, Fore.GREEN, Fore.RED];
#     print(choice(list_cor), randint(1, 60), end=' ');
