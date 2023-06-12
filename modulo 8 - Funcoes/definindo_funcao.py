""" 
Definindo Função

- Funções são pequenas parte de código que realizam tarefas específicas;
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito uteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela, é bom fazer uma verificação para que a função seja simplificada.

# Toda função que vem integrada no python é chamada de Built-in


# Exemplo de utilização de funções:

cores = ['Azul', 'Branco', 'Preto']

# Utilizando a função integrada (Built-in) do Python print()
# Algumas funções Built-in possuem dados de entradas e outras não.

# Com dados de entrada:

print(cores);

# Sem dados de entrada:

cores.clear();
"""

# Função integrada vem de um principio chamado DRY - Don't Repeat Yourself - Não repita você mesmo / Não repita seu código.

# Mas então, como definir funções:

def somador(num1, num2):
    return num1 + num2;

print(somador(5, 2));


# Funções com retorno

numeros = [1, 2, 3];

ret = numeros.pop();

print(ret);

# Função com retorno ²

def quadrado_de_7():
    return 7 * 7;

ret = quadrado_de_7();

print(ret)
