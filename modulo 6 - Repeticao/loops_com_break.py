"""
Saindo de loops com break

Funciona da mesma forma que outras linguagens de programação

Utilizamos o break para sair de loops de maneira projetada.


"""

numero = 1;

while numero < 11:
    if numero == 5:
        print();
        print('Encontrei o número sorteado');
        break;

    print(numero, end=' ');

    numero += 1;