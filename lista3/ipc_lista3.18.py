#Introdu��o a programa��o de computadores;
#Professor: Jucimar Junior
#Felipe Henrique Bastos Costa - 1615310032
#Lorene da Silva Marques - 1615310013
#Caio de Oliveira Martins - 1615310031
#Antonio Rodrigues de Souza Neto - 1615310028
#Calebe Roberto Chaves da Silva Rebello - 1615310043

n = int(input("Digite um n�mero (ZERO para sair): "))

maior = n 
menor = n
soma = n

while(n != 0):
    n = int(input("Digite um n�mero (ZERO para sair): "))
    if (n == 0):
        break
    if (n < menor):
        menor = n
    if (n > maior):
        maior = n
    soma += n

print("O menor n�mero �: %d" %menor)
print("O maior n�mero �: %d" %maior)
print("A soma �: %d" %soma)
