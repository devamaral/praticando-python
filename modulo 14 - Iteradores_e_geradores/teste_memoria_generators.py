"""
Teste de memória com generators 

# Sequência de Fibonacci
1, 1, 2, 3, 5, 8, 13...

"""
 # 479.536k - Utilizando lista

def fib_lista(max):
    numbs = [];
    a, b = 0, 1;

    while len(numbs) < max:
        numbs.append(b);
        a, b = b, a + b;

    return numbs


# 69.392k - Utilizando generators

def fib_gen(max):
    a, b, contador = 0, 1, 0;
    while contador < max:
        a, b = b, a + b;
        yield a;
        contador = contador + 1;

for n in fib_gen(100000):
    print(n);
