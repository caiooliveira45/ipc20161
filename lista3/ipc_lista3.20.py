#Introdu��o a programa��o de computadores;
#Professor: Jucimar Junior
#Felipe Henrique Bastos Costa - 1615310032
#Lorene da Silva Marques - 1615310013
#Caio de Oliveira Martins - 1615310031
#Antonio Rodrigues de Souza Neto - 1615310028
#Calebe Roberto Chaves da Silva Rebello - 1615310043

while (1 == 1):
    cont = 1
    prod = 1   
    n = int(input("Digite um valor entre entre 0 e 15: "))
    if (n < 16) and (n >= 0):
        while (cont < n):
            prod = prod * (cont + 1)
            cont = cont + 1
        print("O valor de", n,"! � igual a: %3.f" %prod)
    else:
        print("VALOR INV�LIDO!")
        n = int(input("Digite um valor entre entre 0 e 15: "))
