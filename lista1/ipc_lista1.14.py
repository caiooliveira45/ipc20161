#
#introdu��o a programa��o de computadores
#Professor: Jucimar JR
#EQUIPE 1
#
#Any Mendes Carvalho - 1615310044
#Kid Mendes de Oliveira Neto - 1615310011
#Victor Rafael da Silva e Silva - 1615310025
#Eduardo Maia Freire - 1615310003
#Luiz Gustavo de Rocha Melo - 1615310015
#Matheus Palheta Barbosa -1615310019
#
#Jo�o Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento di�rio de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de S�o Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. Jo�o precisa que voc� fa�a um programa que leia a vari�vel peso (peso de peixes) e verifique se h� excesso. Se houver, gravar na vari�vel excesso e na vari�vel multa o valor da multa que Jo�o dever� pagar. Caso contr�rio mostrar tais vari�veis com o conte�do ZERO.
#

peso = float(input("Informe o peso dos peixes: "))

if (peso > 50):
    excesso = peso - 50
    multa = excesso * 4.00
    print("Voc� excedeu" ,excesso, "kg do numero permitido de peixes \n  O valor \de sua multa e de R$",multa)

else:
    print("Voce nao excedeu o limite de peixes pescados")