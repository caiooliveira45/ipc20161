#Introduçao a programaçao de computadores
#Professor: Jucimar Junior
#Bruno de Oliveira Freire - 1615310030
#Thiago Santos Borges - 1615310023
#Nickso Patrick Façanha Calheiros - 1615310059
#Matheus Mota de Souza - 1615310016
#Igor Menezes Sales Vieira - 1615310007
#Nadine da Cunha Brito - 1615310040
cont = 1
maior = menor = num_maior = num_menor = 0
while(cont<4):
    num = int(input("Digite a matricula do aluno: "))
    altura = float(input("Digite a altura em cm: "))
    if (cont==1):
        num_maior = num_menor = num
        maior = menor = altura
    elif altura >= maior:
        maior = altura
        num_maior = num
    elif altura<= menor:
        menor = altura
        num_menor = num
    cont = cont+1
print("Matricula do maior aluno: %d"%num_maior,"Altura(cm): ",maior)
print("Matricula do menor aluno: %d"%num_menor,"Altura(cm): ",menor)
