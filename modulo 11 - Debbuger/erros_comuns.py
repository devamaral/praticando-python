""" 
Erros mais comuns em Python

É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução do nosso código.

Os erros mais comuns:

SyntaxError -> Ocorre quando Python encontra um erro de sintaxe. Ou sejam, você escreveu algo que o Python não reconhece como parti da linguagem.

Exemplos SyntaxError:

1 -
    def funcao:
        print('Lucas');

2-
    None = 1;

3- 
    return;


NameError -> Ocorre quando uma variável ou função não foi definida.

Exemplos NameError:

1- 
    print(nome);

2- 
    nome();

3- 
    a = 11;

    if a < 10:
        msg = 'É maior do que 10';

    print(msg);


TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado.

Exemplos TypeError:

1-
    print(len(5));

2- 
    print('Lucas' + []);


IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilização um indice inválido.

Exemplos IndexError:

1- 
    lista = ['Lucas'];
    print(lista[1]);


ValueError -> Ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo correto mas valor inapropriado.

Exemplos ValueError:

1- 
    print(int('1'));


KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe.

Exemplo KeyError:

1-
    dic = {'nome': 'Lucas'};
    print(dic['nom']);


AttributeError -> Ocorre quando uma variável não tem um atributo/função.

Exemplo AttributeError:

1- 
    tupla = (11, 5, 2, 10);
    print(tupla.sort());


IndentationError -> Ocorre quando não respeitamos a indentação do Python (4 espaços).

Exemplo IndentationError:

1-
    a = 11;

    if a < 10:
    msg = 'É maior do que 10';

    print(msg);

"""
