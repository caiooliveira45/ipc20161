#Introdução a programação de computadores;
#Professor: Jucimar Junior
#Felipe Henrique Bastos Costa - 1615310032
#Lorene da Silva Marques - 1615310013
#Caio de Oliveira Martins - 1615310031
#Antonio Rodrigues de Souza Neto - 1615310028
#Calebe Roberto Chaves da Silva Rebello - 1615310043

entrada = int(input("Digite um número positivo inteiro: "))

primo = 1
contador = 0

entrada1 = entrada/2

while primo <= entrada:
    if entrada % primo==0:
        primo = primo+1
        contador = contador+1
    if primo >= entrada1:
        primo = entrada
        primo = primo + 1
        contador = contador + 1
    else:
        primo = primo + 1
if contador==2:
    print("O número requisitado é primo!")
else:
    print("O número requisitado não é primo!")
