#Introdu��o a programa��o de computadores;
#Professor: Jucimar Junior
#Felipe Henrique Bastos Costa - 1615310032
#Lorene da Silva Marques - 1615310013
#Caio de Oliveira Martins - 1615310031
#Antonio Rodrigues de Souza Neto - 1615310028
#Calebe Roberto Chaves da Silva Rebello - 1615310043

x = int(input("Digite um n�mero: "))
y = int(input("Digite outro n�mero: "))

c1 = x
c2 = y
soma = 0

if (c1 < c2):
    while (c1 < c2):
        print("N�mero %d"% c1)
        soma += c1
        c1 += 1

if (c2 < c1):
    while (c2 < c1):
        print("N�mero %d"% c2)
        soma += c2
        c2 += 1

print("A soma dos valores �",soma)
