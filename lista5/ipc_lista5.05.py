#Introducao a programacao de computadores
#Professor: Jucimar Junior
#Nickso Patrick Façanha Calheiros - 1615310059
#
#

from matriz import*

m = int(input( ))
n = int(input( ))
matriz = []
matriz = gerar_matriz(m,n)
arrumar_matriz(matriz, m)
x = verificar_permutacao(matriz,m,n)
print(x)
