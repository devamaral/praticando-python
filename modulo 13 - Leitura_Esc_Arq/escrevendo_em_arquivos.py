"""
Escrevendo em arquivos

# OBS¹: Ao abrir um arquivo para leitura, não podemos realizar escritas nele. Apenas ler. Da mesma forma, se abrirmos um arquivo para escrita, não podemos lê-lo, somente escrever nele.

# OBS²: Ao abrir um arquivo para escrita, caso não exista ele é criado no SO.

Para escrever dados em um arquivo, após abrir utilizamos a função write(). Que recebe uma string como parâmetro.

Abrindo um arquivo para escrita com o modo 'w' se o arquivo não existir será criado, caso ele já exista, o anterior será apagado e um novo será criado. Dessa forma, todo o conteúdo no arquivo anterior é 
perdido

# Exemplo de escrita - modo='w' - write (escrita)
# Forma Pythonica

with open('texte.txt', 'w') as arquivo:
    arquivo.write('Escrevendo dados em arquivo \n');
    arquivo.write('Podemos colocar quantas linhas quisermos \n');


with open('geek.txt', 'w') as arquivo:
    arquivo.write('Geek ' * 1000);
""" 

with open('frutas.txt', 'w') as arquivo:
    while True:
        frutas = input('Informe uma fruta ou digite sair: ');

        if fruta != 'sair':
            arquivo.wripe(frutas);
        else:
            break;
    

