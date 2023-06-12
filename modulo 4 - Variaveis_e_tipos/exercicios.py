#1

numero_inteiro = 10;

print(type(numero_inteiro));
print(numero_inteiro);


#2

numero_real = 2.2;

print(type(numero_real));
print(numero_real);


#3

numero1 = int(input('Digite o primeiro número: '));
numero2 = int(input('Digite o segundo numero: '));
numero3 = int(input('Digite o terceiro numero: '));

soma = numero1 + numero2 + numero3;

print(soma);


#6

temperatura_celsus = float(input('Digite a temperatura em Celsius: '));

fahrenheit = temperatura_celsus * (9.0 /5.0 ) + 32;

print(fahrenheit);


#7

temperatura_fahrenheit = float(input('Digite a temperatura em fahrenheit: '));

celsus = 5.0 * (temperatura_fahrenheit - 32.0) / 9.0;

print(celsus);



#10

velocidade_km = float(input('Digite a velocidade em km/h: '));

ms = velocidade_km / 3.6

print(ms);