#Introdu��o a programa��o de computadores;
#Professor: Jucimar Junior
#Felipe Henrique Bastos Costa - 1615310032
#Lorene da Silva Marques - 1615310013
#Caio de Oliveira Martins - 1615310031
#Antonio Rodrigues de Souza Neto - 1615310028
#Calebe Roberto Chaves da Silva Rebello - 1615310043

n = int(input("Digite o valor de n: "))

produto = n
contador =  n-1

while contador > 1:
    produto = produto*contador
    contador = contador - 1

print(n, "!=", produto)
