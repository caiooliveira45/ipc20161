#Introdu��o a Programa��o de Computadores
#Professor: Jucimar Junior
#Any Mendes Carvalho - 1615310044
#Kid Mendes de Oliveira Neto - 1615310011
#Victor Rafael da Silva e Silva - 1615310025
#Eduardo Maia Freire - 1615310003
#Luiz Alexandre Olivera de Souza-1615310057
#Matheus Palheta Barbosa -1615310019
#
#Fa�a um Programa que pergunte quanto voc� ganha por hora e o n�mero de horas trabalhadas no m�s. Calcule e mostre o total do seu sal�rio no referido m�s.

QntHora = input("Entre com o valor de seu rendimento por hora: ")  
hT = input("Entre com a quantidade de horas trabalhadas no m�s: ")  
  
Salario = round(QntHora*hT,2) 

print (("\n Voce ganhou %.2f reais neste mes") % (Salario))  




