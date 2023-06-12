"""
Len, Abs, Sum, Round

len() -> Retorna o tamanho de itens de um iterável.


# Exemplo len

print(len('Geek University'));
print(len([1, 2, 3, 4, 5]));
print(len((1, 2, 3, 4, 5)));
print(len({1, 2, 3, 4, 5}));
print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4}));
print(len(range(0, 10)));

# Por debaixo dos panos com o len, o python faz o seguinte:

# Dunder len
print('Geek University'.__len__());


# Exemplo abs

# abs() -> Retorna o valor absoluto de um número inteiro ou real. De forma básica, seria o seu valor real sem o sinal.

print(abs(-5));
print(abs(5));
print(abs(3.15));
print(abs(-3.15));


"""
# Sum

# sum() -> Recebe como parâmetro um iterável, podendo receber um vlaor inicial, e retorna a soma totoal dos elementos, incluindo o valor inicial

# OBS: O valor inicial default = 0

# Exemplo sum

print(sum([1, 2, 3, 4, 5]));
print(sum([1, 2, 3, 4, 5], 5));
print(sum([1, 2, 3, 4, 5], -5));
print(sum((1, 2, 3, 4, 5)));
print(sum({1, 2, 3, 4, 5}));
print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4}.values()));


# Round() -> Retorna um número arredondado para n digito de precisão após a casa decimal. Se aprecisão não for informada retorna o inteiro mais próximo da entrada.

print(round(10.2));
print(round(10.5));
print(round(10.6));
print(round(1.212121, 2));