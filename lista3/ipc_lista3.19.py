"""
#lista de repeti��o

#Antonio Rodrigues de Souza Neto --- matr�cula ----1615310028
#Gabriel Machado Moreira --- matr�cula ----1615310034
#Luiz Gustavo de Rocha Melo --- matr�cula ---- 1615310015
#Lucas Ferreira Soares --- 1615310014
#Calebe Roberto Chaves da Silva Rebello --- matr�cula---1615310043

"""

n = int(input("Digite um n�mero entre 0 e 1000: "))

maior = n 
menor = n
soma = n

while(n != 0):
    n = int(input("Digite um n�mero entre 0 e 1000 (ZERO para sair): "))
    if (n <= 0) or (n >= 1000):
        break
    if (n < menor):
        menor = n
    if (n > maior):
        maior = n
    soma += n

print("O menor n�mero �: %d" %menor)
print("O maior n�mero �: %d" %maior)
print("A soma �: %d" %soma)
